import cv2
import argparse
import sys
from functions.getResizeValues import getResizeValues
from functions.videoToFrames import videoToFrames
from functions.convertFrames import convertFrames
from functions.framesToVideo import framesToVideo
from functions.clearTempDirectories import clearTempDirectories

# Input from Terminal
parser = argparse.ArgumentParser(
    prog='Video-Edge-Outliner',
    description= \
    'Python script to convert videos to a video map of the object edges. It will open a cv2 window showing output frames as it processes.' ,
    epilog='Run "python main.py <VIDEO_NAME> --low-threshold=<OPTIONAL_ARG_VALUE> --high-threshold=<OPTIONAL_ARG_VALUE>',
)

parser.add_argument('filename')
parser.add_argument('--low_threshold', type=int)
parser.add_argument('--high_threshold', type=int)
args = parser.parse_args()

video_path = args.filename
low_threshold = args.low_threshold
high_threshold = args.high_threshold

if low_threshold == None:
    low_threshold = 50
if high_threshold == None:
    high_threshold = 120
    
# Pipeline
cap = cv2.VideoCapture(video_path)
# https://stackoverflow.com/questions/39953263/get-video-dimension-in-python-opencv
if cap.isOpened():
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)

width, height = getResizeValues(width=width, height=height)
frame_dir, frame_count, step = videoToFrames(video_path=video_path, frames_dir="./frames", new_width=int(width), new_height=int(height))
convertFrames(frames_path=frame_dir, start=0, end=frame_count, step=step)
framesToVideo(frames_path=frame_dir, frame_count=frame_count, step=step, frame_width=int(width), frame_height=int(height), fps=int(fps))
clearTempDirectories(frames_path=frame_dir)