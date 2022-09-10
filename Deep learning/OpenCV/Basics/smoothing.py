import cv2 as cv

img = cv.imread("Projects\Deep learning\OpenCV\Photos\cats.jpg")
cv.imshow("Cats", img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow("Average", average)

# Gaussian blur
gaussian = cv.GaussianBlur(img, (7, 7), sigmaX=0)
cv.imshow("Gaussian", gaussian)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

# Bilateral
bilateral = cv.bilateralFilter(img, d=5, sigmaColor=15, sigmaSpace=15)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
