import timm
import torch
import torch.nn as nn
from PIL import Image
from data import get_datatransform


class ViTModel(nn.Module):
    def __init__(self, model, pretrained=True):
        super().__init__()
        self.model = timm.create_model(model, pretrained=pretrained)
        
        if 'tiny' in model:
            feature_dim = 192
        elif 'small' in model:
            feature_dim = 384
        elif 'base' in model:
            feature_dim = 768
        
        self.model.head = nn.Sequential(
            nn.Linear(feature_dim, 10),
            nn.GELU(),
            nn.Linear(10, 1)
        )
        
    def forward(self, x):
        out = self.model(x)
        return out

  
if __name__ == '__main__':
    seed = 2022
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)

    model = ViTModel('vit_tiny_patch16_224')
    
    # image
    path = r'D:\Labs\BKC\ATGT\TrafficIncidentRecognitionAndWarningSystem\crawl_data\data\train\1\000325.jpg'
    img = Image.open(path)
    datatransform = get_datatransform()
    img = datatransform(img).unsqueeze(0)
    
    # forward
    output = model(img)
    print(output)