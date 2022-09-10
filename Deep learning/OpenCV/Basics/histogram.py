import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Projects\Deep learning\OpenCV\Photos\cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
# Grayscale histogram

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)


# gray_hist = cv.calcHist(
#     images=[gray], channels=[0], mask=mask, histSize=[256], ranges=[0, 256]
# )

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# BGR Histogram
plt.figure()
plt.title("Colour histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ("b", "g", "r")

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()
cv.waitKey(0)
