# importing
import cv2
import numpy as np 
import time
from tkinter import ttk
from tkinter import *

class ColorDetect:

	# color detect
	def otd(self,col):
	
		# blue
		if col == 0:
			l = [110,50,50]
			u = [130,255,255]

		# red
		if col == 1:
			l = [0,50,50]
			u = [10,255,255]

		# yellow
		if col == 2:
			l = [20,110,110]
			u = [40,255,255]

		# Connecting to the Camera
		cap = cv2.VideoCapture(0)

		# blue range
		lower = np.array(l)
		upper = np.array(u)

		#repeating frames
		while True:
			# Converting the Input Into HSV Format
			ret, frame = cap.read()
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

			# Filtering Out Yellow Pixels
			mask = cv2.inRange(hsv, lower, upper)
			
			# Finding Contours
			contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

			# Getting the Coordinates of the Rectangle Bounding the Contour
			for contour in contours: 		
				area = cv2.contourArea(contour)
				k = 0

				if(area > 800):
					x,y,w,h = cv2.boundingRect(contour)
					
					# circle size
					z =((w+h)/2)
					z= int(z)

					# direction
					if x <= 200:
						xd="Left"
					if x < 400 and x > 200:
						xd="Center"
					if x > 400:
						xd = "Right"
					if y > 150 and y < 275:
						yd="Middle"
					if y < 150:
						yd="Top"
					if y > 275:
						yd="Bottom"

					# print
					point=yd+" "+xd
					print(point)
					
					# text
					frame =cv2.putText(frame,point,(0,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(40, 116, 166 ))
					
					# circle formation
					frame = cv2.circle(frame, (x,y),z,(0,0,255),2)
					cv2.putText(frame,point, (0,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))	
			
			#showing
			cv2.imshow("Object Tracking", frame)

			# break
			k = cv2.waitKey(1) & 0XFF 
			if k == 27:
				break

		# destroy
		cv2.destroyAllWindows()
		cap.release()