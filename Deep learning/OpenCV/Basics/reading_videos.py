import cv2 as cv

# 0 refers to 0th camera plugged in
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    # Stops when d is pressed cv.waitKey is interval between frames
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
