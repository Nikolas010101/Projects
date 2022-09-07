import cv2 as cv


def rescale_frame(frame, scale=0.75):
    # Works for images, videos and live video
    height = frame.shape[0] * scale
    width = frame.shape[1] * scale
    dimensions = (int(width), int(height))
    return cv.resize(frame, dimensions)


def change_res(width, height):
    # Live video only
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread("Projects\Deep learning\OpenCV\Photos\cat_large.jpg")
cv.imshow("Cat", img)
cv.imshow("Resized cat", rescale_frame(img, 0.3))

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)
    print(frame.shape)
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)
