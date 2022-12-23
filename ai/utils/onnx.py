import numpy as np
import torch
import onnxruntime as onnxrt


def to_onnx(model, onnx_path, input_size=(1, 3, 224, 224)):
        
    dummy_input = torch.randn(*input_size)
    input_names = ['input']
    output_names = ['output']
    
    torch.onnx.export(
        model,
        dummy_input,
        onnx_path,
        input_names=input_names,
        output_names=output_names,
        export_params=True
    )
    
    # Check if model is ok
    real_output = model(dummy_input).detach().numpy()
    
    onnx_session = onnxrt.InferenceSession(onnx_path)
    onnx_inputs = {'input': dummy_input.numpy()}
    onnx_outputs = onnx_session.run(None, onnx_inputs)
    onnx_output = onnx_outputs[0]
    
    max_err = np.max(np.abs(onnx_output - real_output))
    print('Max error: {:.6f}'.format(max_err))
