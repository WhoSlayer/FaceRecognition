# FaceRecognition
Monitors screen time by utilising the camera to observe and issues a notification to remind the user every x minutes.

main.py - Utilises video capture to monitor face in front of the screen, if the user remains seated in front of the computer for 20 minutes, a Windows notification to take a break will be displayed. If they move away before 20 minutes, the timer will reset.

eye icon2.jpg - Used as an icon in notification to take a break.

haarcascade_frontalface_default.xml - the algorithm used to detect objects in images (in this case to monitor the face).
