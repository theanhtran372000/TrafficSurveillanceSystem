import time
import math
import copy
import torch
import wandb
import torch.nn as nn
import torch.optim as optim
from datetime import timedelta

class Trainer:
    def __init__(self, config):
        self.config = config
        self.best_acc = 0.0
        self.best_model_wts = None
    
    def prepare_training(self, model):
        criterion = nn.MSELoss()
        optimizer = optim.Adam(model.parameters(), lr=self.config['lr'], betas=(0.9, 0.99))
        
        if self.config['scheduler'] == 'cosine':
            scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=10, eta_min=1e-5, verbose=1)
        else:
            scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.5, verbose=1)
        
        return criterion, optimizer, scheduler
        
    def fit(self, model, dataloaders):
        print('Start training')
        since = time.time()
        
        criterion, optimizer, scheduler = self.prepare_training(model)
        model.to(self.config['device'])
        
        self.best_model_wts = copy.deepcopy(model.state_dict())
        self.best_acc = 0.0
        self.best_loss = 1000
        patience = 0
        
        for epoch in range(self.config['n_epochs']):
            print('=== Epoch {} / {} ==='.format(epoch + 1, self.config['n_epochs']))
            
            if epoch == self.config['unfreeze_from']:
                print('Unfreeze {} last blocks'.format(self.config['n_unfreeze']))
                model = self.unfreeze_layers(model, self.config['n_unfreeze'])
            
            for phase in ['train', 'val']:
                
                # Config model behavior
                if phase == 'train':
                    model.train()
                else:
                    model.eval()
                    
                running_loss = 0.0
                running_corrects = 0
                
                # Iterate over data
                for i, (images, labels) in enumerate(dataloaders[phase]):
                    
                    if (i + 1) % self.config['console_log_every'] == 0:
                        total_iters = math.ceil(len(dataloaders[phase].dataset) / self.config['batch_size'])
                        print('- Iteration {} / {}'.format(i + 1, total_iters))
                    
                    images = images.to(self.config['device'])
                    labels = labels.to(self.config['device'])
                    
                    with torch.set_grad_enabled(phase == 'train'):
                        # Forward pass
                        outputs = model(images)
                        preds = torch.round(outputs).int()
                        loss = criterion(outputs, labels.view(-1, 1).float())
                        
                        # Backward pass: only in training phase
                        if phase == 'train':
                            optimizer.zero_grad()
                            loss.backward()
                            optimizer.step()
                        
                    # Add iteration loss to epoch loss
                    running_loss += loss.item() * images.size(0)
                    running_corrects += torch.sum(preds.view(-1) == labels.int())
                    
                    if self.config['dev_run']:
                        break
                    
                # Update learning rate at the end of epochs
                if phase == 'train':
                    scheduler.step()
                    
                epoch_loss = running_loss / len(dataloaders[phase].dataset)
                epoch_acc = running_corrects / len(dataloaders[phase].dataset)
                
                # Log to console
                print('[{}] Loss: {:.4f} Acc: {:.4f}'.format(
                    phase.rjust(5, ' '),
                    epoch_loss,
                    epoch_acc
                ))
                
                # Log to wandb
                if 'wandb_name' in self.config:
                    wandb.log(
                        {
                            '{}/loss'.format(phase): epoch_loss,
                            '{}/accuracy'.format(phase): epoch_acc
                        },
                        step=epoch
                    )
            
            # Update best after val phase
            if epoch_loss < self.best_loss:
                print('Update best loss from {:.4f} to {:.4f}'.format(self.best_loss, epoch_loss))
                self.best_acc = epoch_acc
                self.best_loss = epoch_loss
                self.best_model_wts = copy.deepcopy(model.state_dict())
                patience = 0
            else:
                patience += 1
                if patience >= self.config['es_patience']:
                    print('Early stopping after {} epochs waiting!'.format(self.config['es_patience']))
                    break
                else:
                    print('Patience {}/{}'.format(patience, self.config['es_patience']))
            
        time_elapsed = timedelta(seconds=int(time.time() - since))
        print('Finish training after {}!'.format(str(time_elapsed)))
        print('Best loss: {:.4f}'.format(self.best_loss))
        print('Accuracy: {:.2f}'.format(self.best_acc))
        
        model.load_state_dict(self.best_model_wts)
        return model
    
    def save(self, path):
        print('Save model to {}!'.format(path))
        torch.save(self.best_model_wts, path)
        
    def load(self, model, path):
        print('Load model from {}!'.format(path))
        return model.load_state_dict(torch.load(path))
    
    def freeze_backbone (self, model):
        # Freeze all except head layers
        for n, p in model.named_parameters():
            if 'head' not in n:
                p.requires_grad = False

        return model
    
    def unfreeze_layers(self, model, n_blocks):
        total_blocks = len(model.model.blocks)
        
        # unfreeze n_blocks last attention blocks
        for i in range(total_blocks - n_blocks, total_blocks):
            block = model.model.blocks[i]
            for p in block.parameters():
                p.requires_grad = True
        return model