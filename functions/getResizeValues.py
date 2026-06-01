DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720

def getResizeValues(width: float, height: float) -> tuple[int, int]:
    if width <= DEFAULT_WIDTH and height <= DEFAULT_HEIGHT:
        return int(width), int(height)
    
    elif width/height <= DEFAULT_WIDTH/DEFAULT_HEIGHT:
        width *= DEFAULT_HEIGHT/height
        height = DEFAULT_HEIGHT
        return int(width), int(height)
    
    else:
        height *= DEFAULT_WIDTH/width
        width = DEFAULT_WIDTH
        return int(width), int(height)