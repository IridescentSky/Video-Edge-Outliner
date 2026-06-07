import shutil
import os

def clearTempDirectories(frames_path: str):
    shutil.rmtree(frames_path)