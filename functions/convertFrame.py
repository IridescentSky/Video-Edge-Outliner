import cv2
import numpy

# Significant portions of code taken from on https://learnopencv.com/edge-detection-using-opencv/
# and https://www.geeksforgeeks.org/machine-learning/implement-canny-edge-detector-in-python-using-opencv/

def convertFrame() -> numpy.ndarray:
    frame = cv2.imread('images/dandelion.jpeg')
    if frame is None:
        raise FileNotFoundError("Frame cannot be detected")
    
    frame_resized = cv2.resize(frame, (1001, 668))
    frame_gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    frame_blur = cv2.GaussianBlur(frame_gray, (3,3), 0)
    # frame_blur_median = cv2.medianBlur(frame_gray, 5)
    # frame_blur_bilateral = cv2.bilateralFilter(frame_gray, 15, 150, 150)

    frame_canny = cv2.Canny(image=frame_blur, threshold1=50, threshold2=200)
    # frame_laplacian = cv2.Laplacian(src=frame_blur, ddepth=cv2.CV_64F, ksize=3)

    return frame_canny
