import numpy
import cv2
import os
from decord import VideoReader, gpu, cpu
from tqdm.contrib import tzip

# Code taken from https://medium.com/@haydenfaulkner/extracting-frames-fast-from-a-video-using-opencv-and-python-73b9b7dc9661
def videoToFrames(video_path: str, frames_dir: str, step: int = 1) -> tuple[str, int, int]:
    """
    Converts video to frames, saving the frames in directory and returning a tuple of (output_path, frame_count)
    """
    video_path = os.path.normpath(video_path)
    frames_dir = os.path.normpath(frames_dir)

    if not os.path.exists(video_path):
        raise FileNotFoundError
    
    video_dir, video_filename = os.path.split(video_path)

    os.makedirs(os.path.join(frames_dir, video_filename, "original"), exist_ok=True)

    print("Extracting frames from ", video_path, "...")
    frame_count = extractFrames(video_path, frames_dir, step)
    
    return os.path.join(frames_dir, video_filename), frame_count, step

def extractFrames(video_path: str, frames_dir: str, step: int = 1) -> int:
    video_path = os.path.normpath(video_path)
    frames_dir = os.path.normpath(frames_dir)

    if not os.path.exists(video_path):
        raise FileNotFoundError
    
    video_dir, video_filename = os.path.split(video_path)

    vr = VideoReader(video_path, ctx=cpu(0))

    frames_list = list(range(0, len(vr), step))
    saved_count = 0

    frames = vr.get_batch(frames_list).asnumpy()

    for index, frame in tzip(frames_list, frames):
        save_path = os.path.join(frames_dir, video_filename, "original", "{:010d}.jpg".format(index))
        cv2.imwrite(save_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        saved_count += 1

    return saved_count
