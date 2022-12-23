import os
import json
import random
import math
import glob
from tqdm import tqdm
from PIL import Image
from torch.utils.data import Dataset


class AccidentDataset(Dataset):
    def __init__(self, image_dir, anno_dir, train=True, val_ratio=0.2, transforms=None):
        self.image_dir = image_dir
        self.anno_dir = anno_dir
        self.transforms = transforms
        self.labellist = ['normal', 'abnormal']
        self.train = train
        self.val_ratio = val_ratio
        
        # Load image list and anno list
        self.images = []
        self.labels = []
        
        # Process data
        print('Creating {} dataset ...'.format('train' if train else 'valid'))
        
        # Split train val set
        video_list = os.listdir(self.image_dir)
        random.shuffle(video_list)
        n_videos = len(video_list)
        n_val_videos = math.ceil(val_ratio * n_videos)
        
        if train:
            video_list = video_list[: - n_val_videos]
        else:
            video_list = video_list[- n_val_videos :]
        
        for short_video in tqdm(video_list):
            video_dir = os.path.join(self.image_dir, short_video)
            
            # Load annotation file
            json_path = os.path.join(self.anno_dir, '{}.json'.format(short_video))
            with open(json_path, 'r') as f:
                anno = json.load(f)
                
            # Abnomaly frame range
            fstart = anno['anomaly_start']
            fend = anno['anomaly_end']
            
            for frame in os.listdir(video_dir):
                
                frame_id = int(frame.split('.')[0])
                frame_path = os.path.join(video_dir, frame)
                
                if frame_id >= fstart and frame_id <= fend:
                    label = self.labellist.index('abnormal')
                else:
                    label = self.labellist.index('normal')
                    
                self.images.append(frame_path)
                self.labels.append(label)
        
        print('Done!')
                
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, index):
        image_path = self.images[index]
        image = Image.open(image_path).convert('RGB')
        label = self.labels[index]
        
        if self.transforms:
            image = self.transforms(image)
            
        return image, label


class VietnamTrafficDataset:
    def __init__(self, data_dir, transforms=None):
        self.images = glob.glob(os.path.join(data_dir, '*', '*'))
        self.labels = [int(i) for i in os.listdir(data_dir)]
        self.transforms = transforms
        
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, index):
        image_path = self.images[index]
        image = Image.open(image_path).convert('RGB')
        label = int(image_path.split(os.path.sep)[-2])
        
        if self.transforms:
            image = self.transforms(image)
            
        return image, label

 
if __name__ == '__main__':
    # # Define data path
    # image_dir = r'D:\Labs\BKC\ATGT\TrafficIncidentRecognitionAndWarningSystem\DoTA\dataset\frames'
    # anno_dir = r'D:\Labs\BKC\ATGT\TrafficIncidentRecognitionAndWarningSystem\DoTA\dataset\annotations'
    
    # # Define dataset
    # dataset = AccidentDataset(image_dir, anno_dir)
    # print('Sample: ', dataset[0])
    # print('Len: ', len(dataset))
    
    # Define path
    data_dir = r'D:\Labs\BKC\ATGT\TrafficIncidentRecognitionAndWarningSystem\crawl_data\data\train'
    dataset = VietnamTrafficDataset(data_dir)
    print('Sample: ', dataset[0])
    print('Len: ', len(dataset))
        