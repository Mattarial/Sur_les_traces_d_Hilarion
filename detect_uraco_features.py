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

from aruco_4x4_100_utils import displayPoleColors, getAllPoleColors, getPoleCenters, drawDirection, getDirection, \
	drawId, computeCenters, displayAngleOnAruco, getAngleFromCorner, drawRectangleOnAruco, getTops, initCvFor4x4

ap,args,arucoDict,arucoParams,ARUCO_DICT = initCvFor4x4()

lastPoint = {}
angleDict = {}
dicoDist = {}
allCenters = {}
poleColorsDict = {}

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

			displayAngleOnAruco(frame,markerID,angleDict,topLeft)

			allCenters = computeCenters(markerID,topLeft,bottomRight,allCenters)

			cX,cY = allCenters[markerID]

			cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)

			drawId(frame,markerID,topLeft)

			dicoDist = getDirection(markerID,lastPoint,cX,cY,dicoDist)

			drawDirection(frame,markerID,cX,cY,dicoDist,(255, 0, 0))

			lastPoint[markerID] = (cX,cY)

			pole_centers = getPoleCenters(topRight,topLeft,bottomRight,bottomLeft)

			poleColorsDict = getAllPoleColors(frame,markerID,pole_centers,cX,cY,poleColorsDict)

			displayPoleColors(markerID, frame, dir, cX, cY, poleColorsDict,pole_centers)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
