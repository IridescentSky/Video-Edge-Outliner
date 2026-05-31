import cv2
import os
import numpy as np
import ffmpeg
import subprocess
from tqdm import tqdm

# Code based off https://www.geeksforgeeks.org/python/saving-a-video-using-opencv/
def framesToVideo(frames_path: str, frame_count: int, step: int, frame_width: int, frame_height: int, fps: int) -> None:
    frames_path = os.path.normpath(frames_path)
    
    fourcc = cv2.VideoWriter.fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height), isColor=True)

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

    # # Compressing - https://stackoverflow.com/questions/64421177/how-to-compress-a-video-using-ffmpeg-in-python
    # print("Compressing Output to 800k Bit Rate")
    # subprocess.run('ffmpeg -i output.mp4 -b 800k output_compressed.mp4')