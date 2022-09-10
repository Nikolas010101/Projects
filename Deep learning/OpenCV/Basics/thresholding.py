import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Projects\Deep learning\OpenCV\Photos\cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresholded inverse", thresh_inv)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9
)
cv.imshow("Adaptive thresholding", adaptive_thresh)

cv.waitKey(0)
