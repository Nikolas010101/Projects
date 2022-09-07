import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3))
cv.imshow("Blank", blank)

blank[:, :, :] = 0, 255, 0
cv.imshow("Green", blank)

blank[200:300, 300:400, :] = 0, 0, 255
cv.imshow("Square", blank)

cv.rectangle(
    img=blank,
    pt1=(0, 0),
    pt2=(blank.shape[1] // 2, blank.shape[0] // 3),
    color=(0, 0, 0),
    thickness=cv.FILLED,
)
cv.imshow("Rectangle", blank)

cv.circle(
    img=blank,
    center=(blank.shape[1] // 2, blank.shape[0] // 3),
    radius=40,
    color=(0, 0, 255),
    thickness=-1,
)
cv.imshow("Circle", blank)

cv.line(
    img=blank,
    pt1=(0, 0),
    pt2=(blank.shape[1] // 2, blank.shape[0] // 2),
    color=(255, 0, 0),
    thickness=3,
)
cv.imshow("Line", blank)

cv.putText(
    img=blank,
    text="Hello",
    org=(255, 255),
    fontFace=cv.FONT_HERSHEY_TRIPLEX,
    fontScale=1.0,
    color=(255, 255, 25),
    thickness=3,
)
cv.imshow("Text", blank)
cv.waitKey(0)
