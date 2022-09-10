import cv2 as cv

img = cv.imread("Photos\group 2.jpg")
cv.imshow("Group", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier("ComputerVision/Models/haar_face.xml")
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f"{len(faces_rect)} face(s) detected")

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected face(s)", img)
cv.waitKey(0)
