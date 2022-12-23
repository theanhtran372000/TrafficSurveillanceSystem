import argparse
import yaml
import wandb
import os

from data import AccidentDataset, VietnamTrafficDataset, get_dataloader, get_datatransform
from utils import seed_everything, Trainer
from models import ViTModel


def main(args):
    
    # Load config
    with open(args.config, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        
    # Init wandb
    if 'wandb_name' in config:
        wandb.init(
            project=config['wandb_project'],
            entity=config['wandb_entity'],
            name=config['wandb_name'],
            config=config
        )
        
    print('All configs')
    print(config)
    
    # Fix random seed
    seed_everything(config['seed'])
    
    # Get data transforms
    datatransforms = {
        'train': get_datatransform((0.5, 0.5, 0.5), (0.5, 0.5, 0.5), train=True),
        'val': get_datatransform((0.5, 0.5, 0.5), (0.5, 0.5, 0.5), train=False)
    }
    
    # Create dataset
    datasets =  {
        'train': VietnamTrafficDataset(
            config['data_train_dir'],
            transforms=datatransforms['train']
        ),
        'val': VietnamTrafficDataset(
            config['data_val_dir'],
            transforms=datatransforms['val']
        )
    }
    
    # Create dataloader
    dataloaders = {
        'train': get_dataloader(datasets['train'], config['batch_size'], train=True, num_workers=config['n_workers']),
        'val': get_dataloader(datasets['val'], config['batch_size'], train=False, num_workers=config['n_workers'])
    }
    
    # Define model
    model = ViTModel(config['backbone'])
    
    # Trainer
    trainer = Trainer(config)
    model = trainer.freeze_backbone(model)
    trainer.fit(model, dataloaders)
    
    # Save model
    trainer.save(config['checkpoint'])


if __name__ == '__main__':
    # Parse CLI argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config/configs.yaml', help='Path to config file')
    args = parser.parse_args()
    
    # Main
    main(args)