from PIL import Image
import cv2
import numpy as np


def to_PIL(cv_image):
        return Image.fromarray(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB))
    
def to_CV2(pil_image):
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)