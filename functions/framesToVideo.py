import cv2
import os
import numpy as np
from tqdm import tqdm

# Code based off https://www.geeksforgeeks.org/python/saving-a-video-using-opencv/
def framesToVideo(frames_path: str, frame_count: int, step: int, frame_width: int, frame_height: int, fps: int) -> None:
    frames_path = os.path.normpath(frames_path)
    
    # Save Path
    head, tail = os.path.split(frames_path)
    os.makedirs(os.path.join("./", "output"), exist_ok=True)

    # Find file name without the file type code
    period_index = tail.rfind('.')
    if period_index != -1:
        file_name = tail[:period_index]

    save_path = os.path.join("./",  "output", str(file_name) + "_output.mp4")

    fourcc = cv2.VideoWriter.fourcc(*'mp4v')
    out = cv2.VideoWriter(save_path, fourcc, fps, (frame_width, frame_height), isColor=True)

    print("Writing to Video...")
    for index in tqdm(range(0, frame_count, step)):
        frame_path = os.path.join(frames_path, "canny", "{:010d}.jpg".format(index))
        frame = cv2.imread(frame_path, cv2.IMREAD_COLOR)
        if frame is None:
            raise(FileNotFoundError("Frame cannot be found at", frame_path))
        
        out.write(frame)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cv2.destroyAllWindows
    out.release()