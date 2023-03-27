import cv2
import face_recognition
import time
import os
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    if not ret:
        print("Failed to grab the photo, check if the camera is connected properly")
        break
    cv2.imshow("Face Recognition", frame)

    a = cv2.waitKey(1)
    if a%256 == 32:
        img_name = "faceReco.jpg"
        cv2.imwrite(img_name, frame)
        break
#spacebar for taking photo

img = cv2.imread("Put your desired photo here for it to be the main photo to be which it want to be verified.")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("faceReco0.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]  

result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Grand Results: ",result)

if result == "[True]":
    Speak("Identity Verified")
else:
    Speak("Not Verified")

cv2.imshow("IMG", img2)


time.sleep(4)
os.remove("faceReco.jpg")

engine.runAndWait()
cam.release()
cv2.destroyAllWindows()
