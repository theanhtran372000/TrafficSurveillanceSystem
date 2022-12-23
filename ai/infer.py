import argparse
import yaml
import cv2
import torch
import time
from datetime import timedelta
import onnxruntime as onnxrt
from utils import to_onnx, to_PIL, apply_score, seed_everything
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
    
    # Convert model to onnx format
    print('Convert model to ONNX ... ')
    to_onnx(model, config['onnx_path'])
    
    # Inference
    print('Inferencing ...')
    
    start = time.time()
    
    in_path = 'saved/test6.mp4'
    out_path = 'saved/noncrop_gelu/result6.mp4'
    cap = cv2.VideoCapture(in_path)
    
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print('Input: ', in_path)
    print('Width: {} Height: {} FPS: {}'.format(frame_width, frame_height, frame_fps))
    print('Output: ', out_path)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, frame_fps, (frame_width, frame_height))
    
    onnx_session = onnxrt.InferenceSession(config['onnx_path'])
    
    running_avg = 0
    ratio = 0.8
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        new_frame = to_PIL(frame)
        new_frame = transforms(new_frame).unsqueeze(0)
        
        onnx_inputs = {'input': new_frame.numpy()}
        onnx_outputs = onnx_session.run(None, onnx_inputs)
        onnx_output = onnx_outputs[0]
        score = onnx_output[0][0]
        if running_avg == 0:
            running_avg = score
        score = running_avg * (1 - ratio) + score * ratio
        
        frame = apply_score(frame, score)

        out.write(frame)
        
    cap.release()
    out.release()
    
    time_elapsed = int(time.time() - start)
    print('Finish after {}!'.format(timedelta(seconds=time_elapsed)))
    print('FPS: {:.1f}'.format(frame_count / time_elapsed))
    

if __name__ == '__main__':
    # Parse CLI argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config/configs.yaml', help='Path to config file')
    args = parser.parse_args()
    
    # Main
    main(args)