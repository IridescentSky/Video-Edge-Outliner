import cv2
from functions.videoToFrames import videoToFrames
from functions.convertFrames import convertFrames
from functions.framesToVideo import framesToVideo

video_path = "videos/dandelion.mp4"
cap = cv2.VideoCapture(video_path)
# https://stackoverflow.com/questions/39953263/get-video-dimension-in-python-opencv
if cap.isOpened():
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)

frame_dir, frame_count, step = videoToFrames(video_path, "./frames")
convertFrames(frames_path=frame_dir, start=0, end=frame_count, step=step)
framesToVideo(frames_path=frame_dir, frame_count=frame_count, step=step, frame_width=int(width), frame_height=int(height), fps=int(fps))