import cv2
import glob

def face_detection(picture):
    detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imp_img = cv2.VideoCapture(picture)

    res, img = imp_img.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+w), (255, 255, 0), 2)

    cv2.imshow("Elon Image", img)

    cv2.waitKey(0)
    imp_img.release()
    cv2.destroyAllWindows()

all_images = glob.glob("*.jpg")
for image in all_images: 
    face_detection(image)
