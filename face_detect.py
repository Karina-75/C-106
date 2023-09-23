import cv2
img =cv2.imread('boy.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_classifier.detectMultiScale(gray, 1.1, 5)
print(faces)
for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi = img[y: y+h, x: x+w]
    cv2.imwrite('face.jpg', roi)

cv2.imshow('image', img)
cv2.waitKey(0)