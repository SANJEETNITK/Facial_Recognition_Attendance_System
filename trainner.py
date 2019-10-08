import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'

def getImagesWithID(path):
	imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
	# print(imagePath)

	faces = []
	ids = []

	for imagePath in imagePaths:
		face = Image.open(imagePath).convert('L')
		faceNp = np.array(face,'uint8')

		# ID = (os.path.split(imagePath)[-1].split('-')[0]) # Only name
		# print(ID)

		ID = os.path.split(imagePath)[-1].split('-') #ID
		userid = ID[0].split('.') #username
		# print(userid[0][4:]) #user_id
		data = userid[0][4:]
		intData = int(data)
		faces.append(faceNp)
		ids.append(intData)
		
		# print(type(intData))
		cv2.imshow("training",faceNp)
		cv2.waitKey(10)

	return faces, ids

faces, ids = getImagesWithID(path)
recognizer.train(faces,np.array(ids))
recognizer.save('trainingData.yml')
cv2.destroyAllWindows()