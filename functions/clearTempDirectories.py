import shutil
import os

def clearTempDirectories(frames_path: str):
    # Clearing temp frame directories
    original_dir = os.path.join(frames_path, "original")
    canny_dir = os.path.join(frames_path, "canny")

    shutil.rmtree(original_dir)
    shutil.rmtree(canny_dir)