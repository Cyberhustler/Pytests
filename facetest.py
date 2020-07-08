# https://github.com/Cyberhustler
# https://images.unsplash.com/photo-1591867192864-
# fed3a1622179?ixlib=rb-1.2.1&ixid=eyJhcHBf
# aWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80

import cv2

imagePath = "/home/gowtham/test/png"
cascPath = "/home/gowtham/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)


print('Found {0} faces'.format((len(faces))))

# draw a rectangle around the user faces
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)

