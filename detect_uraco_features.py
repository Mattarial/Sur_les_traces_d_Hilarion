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

from laumio import *

tab_l =  [Laumio("192.168.1.31"),
          Laumio("192.168.1.25"),
          Laumio("192.168.1.27"),
          Laumio("192.168.1.30"),
          Laumio("192.168.1.23"),
          Laumio("192.168.1.24"),
          Laumio("192.168.1.26"),
          Laumio("192.168.1.28"),
          Laumio("192.168.1.21"),
          Laumio("192.168.1.29")]


def gradient(laumio: Laumio, o_r, o_g, o_b, val):
	nouv = abs(val*255/180)
	diff_r = abs(o_r-nouv)
	diff_g = abs(o_g-nouv)
	diff_b = abs(o_b-nouv)
	temp_r = o_r
	temp_g = o_g
	temp_b = o_b

	for i in range(0, 10):
		temp_r -= diff_r * 0.1
		temp_g -= diff_g * 0.1
		temp_b -= diff_b * 0.1
		laumio.fillColor(abs(int(temp_r)), abs(int(temp_g)), abs(int(temp_b)))

	return [int(temp_r), int(temp_g), int(temp_b)]

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

			rotation = angleDict[markerID]

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
			poles = poleColorsDict[markerID]

			colorsNorth = poles["Nord"]
			tab_l[2].fillColor(colorsNorth[0],colorsNorth[1],colorsNorth[2])

			colorsNorth = poles["Sud"]
			tab_l[4].fillColor(colorsNorth[0], colorsNorth[1], colorsNorth[2])

			colorsNorth = poles["Est"]
			tab_l[6].fillColor(colorsNorth[0], colorsNorth[1], colorsNorth[2])

			colorsNorth = poles["Ouest"]
			tab_l[8].fillColor(colorsNorth[0], colorsNorth[1], colorsNorth[2])

			#gradient(tab_l[2], colorsNorth[0], colorsNorth[1], colorsNorth[2], rotation)
			time.sleep(0.1)

			#displayPoleColors(markerID, frame, dir, cX, cY, poleColorsDict,pole_centers)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
