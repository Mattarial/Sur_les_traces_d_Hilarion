#!/usr/bin/env python

# import the necessary packages
import math

import numpy as np
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import sys
import os
import glob

def calcCenter(p1,p2):
	tlx, tlY = p1
	trx, trY = p2
	return [(tlx + trx) / 2, (tlY + trY) / 2]

def initCvFor4x4():
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-t", "--type", type=str,
					default="DICT_4X4_100",
					help="type of ArUCo tag to detect")
	args = vars(ap.parse_args())

	# define names of each possible ArUco tag OpenCV supports
	ARUCO_DICT = {
		"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
		"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	}

	# verify that the supplied ArUCo tag exists and is supported by
	# OpenCV
	if ARUCO_DICT.get(args["type"], None) is None:
		print("[INFO] ArUCo tag of '{}' is not supported".format(
			args["type"]))
		sys.exit(0)

	# load the ArUCo dictionary and grab the ArUCo parameters
	print("[INFO] detecting '{}' tags...".format(args["type"]))
	arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
	arucoParams = cv2.aruco.DetectorParameters_create()

	return ap,args,arucoDict,arucoParams,ARUCO_DICT

def getTops(markerCorner):
	corners = markerCorner.reshape((4, 2))
	(topLeft, topRight, bottomRight, bottomLeft) = corners

	topRight = (int(topRight[0]), int(topRight[1]))
	bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
	bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
	topLeft = (int(topLeft[0]), int(topLeft[1]))

	return topRight,topLeft,bottomRight,bottomLeft

def drawRectangleOnAruco(frame,topRight,topLeft,bottomRight,bottomLeft,color):
	cv2.line(frame, topLeft, topRight, color, 2)
	cv2.line(frame, topRight, bottomRight, color, 2)
	cv2.line(frame, bottomRight, bottomLeft, color, 2)
	cv2.line(frame, bottomLeft, topLeft, color, 2)

def getAngleFromCorner(markerCorner,id,dict):
	topRight, topLeft, bottomRight, bottomLeft = getTops(markerCorner)
	diag = np.array(bottomRight) - np.array(topLeft)
	finalAngle, _ = math.atan2(diag[0], diag[1]) * 57, 2958

	dict[markerID] = finalAngle

	return dict

def displayAngleOnAruco(frame,angleDict,topLeft):
	cv2.putText(frame, "Angle : " + str(int(angleDict[markerID])),
				(topLeft[0], topLeft[1] - 55),
				cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (0, 255, 0), 2)

def computeCenters(markerID,topLeft,bottomRight,dico):
	cX = int((topLeft[0] + bottomRight[0]) / 2.0)
	cY = int((topLeft[1] + bottomRight[1]) / 2.0)

	dico[markerID] = (cX,cY)

	return dico

def drawId(frame,markerID,topLeft):
	cv2.putText(frame, "ID : " + str(markerID),
				(topLeft[0], topLeft[1] - 30),
				cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (0, 255, 0), 2)

def getDirection(markerID,lastPoint,dicoDist):
	if markerID in lastPoint:
		lpX, lpY = lastPoint.get(markerID)
	else:
		lastPoint[markerID] = (cX, cY)
		lpX, lpY = lastPoint.get(markerID)

	vectDist = np.array([cX, cY]) - np.array([lpX, lpY])

	dicoDist[markerID] = vectDist

	return dicoDist

def drawDirection(frame,markerID,cX,cY,dicoDist,color):
	cv2.line(frame, (cX, cY), ((cX + dicoDist[markerID][0]), (cY + dicoDist[markerID][1])), color, 2)

def getPoleCenters(topRight,topLeft,bottomRight,bottomLeft):
	poles = ["NORD", "SUD", "EST", "OUEST"]
	pole_centers = []
	for pole in poles:
		if (pole == "NORD"):
			pole_centers.append(calcCenter(topLeft, topRight))
		if (pole == "SUD"):
			pole_centers.append(calcCenter(bottomLeft, bottomRight))
		if (pole == "EST"):
			pole_centers.append(calcCenter(bottomRight, topRight))
		if (pole == "OUEST"):
			pole_centers.append(calcCenter(topLeft, bottomLeft))

	return pole_centers


ap,args,arucoDict,arucoParams,ARUCO_DICT = initCvFor4x4()

lastPoint = {}
angleDict = {}
dicoDist = {}
allCenters = {}

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")

# src is useful to modify the video input
vs = VideoStream(src=0).start()
time.sleep(2.0)
firstTime = True

# loop over the frames from the video stream
while True:
	time.sleep(0.08)
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 600 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=1000)

	# detect ArUco markers in the input frame
	(corners, ids, rejected) = cv2.aruco.detectMarkers(frame,
		arucoDict, parameters=arucoParams)

	# verify *at least* one ArUco marker was detected
	if len(corners) > 0:
		# flatten the ArUco IDs list
		ids = ids.flatten()

		# loop over the detected ArUCo corners
		for (markerCorner, markerID) in zip(corners, ids):

			topRight,topLeft,bottomRight,bottomLeft = getTops(markerCorner)

			# draw the bounding box of the ArUCo detection
			drawRectangleOnAruco(frame,topRight,topLeft,bottomRight,bottomLeft,(0, 255, 0))

			angleDict = getAngleFromCorner(markerCorner,markerID,angleDict)

			displayAngleOnAruco(frame,angleDict,topLeft)

			allCenters = computeCenters(markerID,topLeft,bottomRight,allCenters)
			print(allCenters)
			cX,cY = allCenters[markerID]

			cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)

			drawId(frame,markerID,topLeft)

			dicoDist = getDirection(markerID,lastPoint,dicoDist)

			drawDirection(frame,markerID,cX,cY,dicoDist,(255, 0, 0))

			lastPoint[markerID] = (cX,cY)

			pole_centers = getPoleCenters(topRight,topLeft,bottomRight,bottomLeft)

			coeff = 1.73
			i = 0
			for center in pole_centers:
				square_center = np.array([cX,cY])
				np_center = np.array(center)
				np_center = square_center + (np_center - square_center)*coeff

				if np_center[1] <750 and np_center[0] < 1000 :
					pixels = frame[int(np_center[1]),int(np_center[0])]
				else:
					pixels = [0, 0, 0]

				match i:
					case 0:
						dir = "Nord"
					case 1:
						dir = "Sud"
					case 2:
						dir = "Est"
					case 3:
						dir = "Ouest"

				new_coeff = 3
				center_new = np.array(center)
				new_center = square_center + (center_new - square_center) * new_coeff
				cv2.putText(frame, dir,
							(int(new_center[0]), int(new_center[1])),
							cv2.FONT_HERSHEY_SIMPLEX,
							0.5, (int(pixels[0]), int(pixels[1]), int(pixels[2])), 2)

				if i == 3:
					i = 0
				else:
					i+=1

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
