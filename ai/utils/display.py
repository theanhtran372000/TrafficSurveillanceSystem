import cv2


# Apply score
def apply_score(image, score):
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # org
    org = (10, 40)
    
    # fontScale
    fontScale = 0.6
    
    # Blue color in BGR
    color = (0, 255, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    # Using cv2.putText() method
    image = cv2.putText(image, 'Score: {:.4f}'.format(score), org, font, fontScale, color, thickness, cv2.LINE_4)
    
    return image