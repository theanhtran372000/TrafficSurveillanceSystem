import argparse
import yaml
import glob
import random
import torch
import time
import os
from PIL import Image
import onnxruntime as onnxrt
from utils import to_PIL, seed_everything
from models import ViTModel
from data import get_datatransform


def main(args):
    # Load config
    with open(args.config, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    seed_everything(config['seed'])
    
    print('Load model checkpoint ...')
    model = ViTModel(config['backbone'])
    model.load_state_dict(torch.load(config['checkpoint']))
    model.eval()
    transforms = get_datatransform((0.5, 0.5, 0.5), (0.5, 0.5, 0.5), train=False)
    
    test_dir = 'crawl_data/data/train/1'
    onnx_path = 'saved/noncrop_gelu/model.onnx'
    n_samples = 100
    
    onnx_session = onnxrt.InferenceSession(onnx_path)
    
    samples = random.sample(glob.glob(os.path.join(test_dir, '*')), k=n_samples)
    
    time_elapsed = []
    
    for sample in samples:
        
        start = time.time()
        
        new_frame = Image.open(sample).convert('RGB')
        new_frame = transforms(new_frame).unsqueeze(0)
        
        onnx_inputs = {'input': new_frame.numpy()}
        onnx_outputs = onnx_session.run(None, onnx_inputs)
        onnx_output = onnx_outputs[0]
        score = onnx_output[0][0]
        
        time_elapsed.append(time.time() - start)
        
    time_elapsed = sum(time_elapsed) / len(time_elapsed)

    print('FPS: {:.1f}'.format(1 / time_elapsed))
    

if __name__ == '__main__':
    # Parse CLI argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config/configs.yaml', help='Path to config file')
    args = parser.parse_args()
    
    # Main
    main(args)