import cv2
import numpy
import os
from tqdm import tqdm

def convertFrames(frames_path: str, start: int, end: int, step: int) -> int:
    """
    Convert frames from original video to canny frames, returning the number of saved frames
    """
    frames_path = os.path.normpath(frames_path)
    os.makedirs(os.path.join(frames_path, "canny"), exist_ok=True)
    saved_count = 0

    print("Converting Frames...")
    for index in tqdm(range(start, end, step)):
        frame_canny = convertFrame(os.path.join(frames_path, "original", "{:010d}.jpg".format(index)))
        save_path = os.path.join(frames_path, "canny", "{:010d}.jpg".format(index))
        cv2.imwrite(save_path, cv2.cvtColor(frame_canny, cv2.COLOR_BGR2RGB))
        saved_count += 1
    
    return saved_count

# Significant portions of code taken from on https://learnopencv.com/edge-detection-using-opencv/
# and https://www.geeksforgeeks.org/machine-learning/implement-canny-edge-detector-in-python-using-opencv/
def convertFrame(frame_path: str) -> numpy.ndarray:
    """
    Runs canny edge detection on a frame to return a edge map image.
    """
    frame = cv2.imread(frame_path)
    if frame is None:
        raise FileNotFoundError("Frame cannot be detected")
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_blur = cv2.GaussianBlur(frame_gray, (3,3), 0)
    # frame_blur_median = cv2.medianBlur(frame_gray, 5)
    # frame_blur_bilateral = cv2.bilateralFilter(frame_gray, 15, 150, 150)

    frame_canny = cv2.Canny(image=frame_blur, threshold1=50, threshold2=120)
    # frame_laplacian = cv2.Laplacian(src=frame_blur, ddepth=cv2.CV_64F, ksize=3)

    return frame_canny
