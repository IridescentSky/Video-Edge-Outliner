import cv2
from functions.convertFrame import convertFrame

frame_canny = convertFrame()
cv2.imshow("Canny", frame_canny)
cv2.waitKey(0)
# cv2.imshow("Laplacian", frame_laplacian)
# cv2.waitKey(0)
cv2.destroyAllWindows()