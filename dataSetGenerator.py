import cv2
import numpy as np
import sqlite3


def insertOrUpdate(Id,Name):
	conn = sqlite3.connect("FaceBase.db")
	cmd = "SELECT * FROM People WHERE ID="+str(Id)
	parmas = (Id,Name,'')
	cursor = conn.execute(cmd)

	isRecordExist = 0

	for row in cursor:
		isRecordExist = 1

	if isRecordExist==1:
		print("ID already exists")
		return False
	else:
		conn.execute("Insert INTO People VALUES(?,?,?)",parmas)
		conn.commit()
	conn.close()
	return True

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)


id = input("Enter your id ")
name = input("Enter your name ")
flag = insertOrUpdate(id,name)

count = 0
while True:
	ret, frame = cam.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = detector.detectMultiScale(gray,1.5,5)
	for x,y,w,h in faces:
		count += 1
		cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)
		cv2.imwrite("dataset/user"+id+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])

	cv2.imshow("image",gray)

	if cv2.waitKey(3)==13 or count>1000:
		break


cam.release()
cv2.destroyAllWindows()
