import cv2
import time
import mediapipe as mp
import os
import time
from winotify import Notification, audio


# Setting up file in a virtual environment - activate file: 
# * .venv\Scripts\activate.bat

max = 15
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_detection = mp.solutions.face_detection.FaceDetection()

cap = cv2.VideoCapture(0) # or filename for a video saved
starting_time = time.time()

noti = Notification(app_id="Eye Protection",
					title="Reminder!",
					msg="You have been facing the screen for 20 minutes. Please take a break.",
					duration="long",
					icon=r"C:\Users\muzam\Downloads\works\eye icon2.jpg")
noti.set_audio(audio.SMS, loop=False)
while True:
	ret, img = cap.read() # read a video file, cap.read returns flag if frame was read correctly and the frame
	width,height,channels = img.shape
	if not ret:
		break
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	faces = face_cascade.detectMultiScale(gray, 1.1,4)

	results = face_detection.process(gray)
	if results.detections:
		elapsed_time = int(time.time() - starting_time)
		if elapsed_time > max:
			print("TAKE A BREAK")
			noti.show() 
			#os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
			#win32api.MessageBox(0, 'It has been 5 minutes, take a break!', 'Reminder', 0x00001000)
			time.sleep(1)
			starting_time = time.time()

	else:
		starting_time = time.time()
	k = cv2.waitKey(33)	
	if k == 27:
		break

		
cap.release() #esc to escape
cv2.destroyAllWindows()
