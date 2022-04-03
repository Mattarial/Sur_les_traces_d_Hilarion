# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:18:08 2022

@author: alexa
"""

import aruco_4x4_100_utils.py
import time

def compareLists(L1, L2):
    res = True;
    for i in range(4):
        if L1[i]!=L2[i]:
            res = False
    return res


def unlock(id1, angle1, L):
    
    locked = True
    keyAngleState = 0  #1 : wrong angle
    keyColorState = False;
    
    while(locked):
        time.sleep(0.08)
        
        frame = vs.read()
    	frame = imutils.resize(frame, width=1000)
        
        (corners, ids, rejected) = cv2.aruco.detectMarkers(frame,
    		arucoDict, parameters=arucoParams)
        
        if len(corners) > 0:
            ids = ids.flatten()
            for (markerCorner, markerID) in zip(corners, ids):    
                """corners = markerCorner.reshape((4, 2))
    			(topLeft, topRight, bottomRight, bottomLeft) = corners
                #topRight = (int(topRight[0]), int(topRight[1]))
    			bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
    			#bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
    			topLeft = (int(topLeft[0]), int(topLeft[1]))
                diag = np.array(bottomRight) - np.array(topLeft)
                finalAngle,_ = math.atan2(diag[0],diag[1])*57,2958"""
                
                if markerID==id1: #sur la clé d'angle
                
                    dictAngle = {}
                    dictAngle = getAngleFromCorner(markerCorner, markerID, dictAngle)
                    finalAngle = dictAngle[markerID]
                    
                    if int(finalAngle) < 0:
                        temp=180+int(finalAngle)
                        angle=180+temp
                    
                     #angle unlock state check
                
                    if angle1 + angle < 10 or angle1 - angle < 10:
                        keyAngleState = 3 #angle unlocked
                    elif 10 <= angle1 + angle < 30 or 10 <= angle1 - angle < 30:
                        keyAngleState = 2 #angle almost unlocked
                    elif 30 <= angle1 + angle < 90 or 30 <= angle1 - angle < 90:
                        keyAngleState = 1
                    angleLockLights(keyAngleState) #change la cadence de clignotement des lampes
                                          
                #color unlock state check
                colors = detectColors(markerID)  #renvoie une liste de 4 lettres
                if compareLists(L, colors):
                    keyColorState = True;
                    
                #global unlock state check
                if keyColorState and keyAngleState == 3 :
                    locked = False
                    break
            
