import cv2 as cv
import numpy as np

img = cv.imread("Projects\Deep learning\OpenCV\Photos\park.jpg")
cv.imshow("Boston", img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


translated = translate(img, 100, 100)
cv.imshow("Translated", translated)
rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

# Flipping
flip = cv.flip(img, 0)
cv.imshow("Flipped", flip)
cv.waitKey(0)