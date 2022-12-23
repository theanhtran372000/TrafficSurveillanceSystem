from torch.utils.data import DataLoader
import torchvision.transforms as transforms

# Get dataloader
def get_dataloader(dataset, batch_size, train=True, num_workers=1):
    return DataLoader(
        dataset, 
        batch_size=batch_size, 
        shuffle=train, 
        num_workers=num_workers
    )

# Get data transform
def get_datatransform(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225], jitter=0.2, train=True):
    if train:
        # return transforms.Compose([
        #     transforms.ToTensor(),
        #     transforms.RandomHorizontalFlip(p=0.3),
        #     transforms.Resize((256, 256)),
        #     transforms.CenterCrop(224),
        #     transforms.Normalize(mean, std)
        # ])
        
        return transforms.Compose([
            transforms.ToTensor(),
            transforms.RandomHorizontalFlip(p=0.3),
            transforms.Resize((224, 224)),
            transforms.ColorJitter(
                brightness=jitter,
                contrast=jitter 
            ),
            transforms.Normalize(mean, std)
        ])
        
    else:
        return transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize((224, 224)),
            transforms.Normalize(mean, std)
        ])