from re import A
import sys
import os
import time

import laumio
import aruco_4x4_100_utils.py

sys.path.append(os.path.dirname(sys.argv[0])+'/../')
from laumio import *

def print_usage():
    print(
"Usage: "+sys.argv[0]+"\n\
\n\
    example:\n\
        "+sys.argv[0]+"\n\
")
    sys.exit(1)


if len(sys.argv) != 1:
    print(len(sys.argv))
    print_usage()


class case_mur :
    r = 64
    g = 64
    b = 64

    diag_r = 64
    diag_g = 64
    diag_b = 64

class case_normale :
    r = 255
    g = 255
    b = 255

    diag_r = 0
    diag_g = 255
    diag_b = 0

class case_instable :
    r = 255
    g = 255
    b = 255

    diag_r = 255
    diag_g = 0
    diag_b = 0

class case_lente :
    r = 255
    g = 255
    b = 255

    diag_r = 0
    diag_g = 0
    diag_b = 255

class case_verrou :
    r = 255
    g = 255
    b = 255

    diag_r = 255
    diag_g = 255
    diag_b = 0

    id_cle_angle = 24
    id_cle_couleur = 96
    cle_couleur = ["J","V","B","R"]
    cle_angle = 45

class case_border :
    r = 0
    g = 0
    b = 0

    diag_r = 0
    diag_g = 0
    diag_b = 0

map = [[case_border,       case_border,    case_border,    case_border,     case_border,        case_border],
       [case_border,       case_normale,   case_instable,  case_normale,    case_mur,           case_border],
       [case_border,       case_normale,   case_mur,       case_verrou,     case_normale,       case_border],
       [case_border,       case_mur,       case_mur,       case_mur,        case_instable,      case_border],
       [case_border,       case_mur,       case_mur,       case_lente,      case_normale,       case_border],
       [case_border,       case_border,    case_border,    case_normale,    case_border,        case_border]]

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

laumio_up = [Laumio("192.168.1.26"),
             Laumio("192.168.1.28")]

laumio_down = [Laumio("192.168.1.27"),
               Laumio("192.168.1.25")]

laumio_left = Laumio("192.168.1.23")

laumio_right = Laumio("192.168.1.29")

laumio_diag = [Laumio("192.168.1.24"),
               Laumio("192.168.1.21"),
               Laumio("192.168.1.30"),
               Laumio("192.168.1.31")]


"""
def compareLists(L1, L2):
    res = True
    for i in range(4):
        if L1[i]!=L2[i]:
            res = False
    return res
"""
        #Fonction unlock
def unlock(id1, angle1, L):
    
    locked = True
    keyAngleState = 0  #1 : wrong angle
    
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
                """                           
                #color unlock state check
                colors = detectColors(markerID)  #renvoie une liste de 4 lettres
                if compareLists(L, colors):
                    keyColorState = True
                    
                #global unlock state check
                if keyColorState and keyAngleState == 3 :
                    locked = False
                    break"""
                if(keyAngleState == 3):
                    locked = False
#FIN fonction unlock

#Origine avec API
get_pos =[400,50] #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
ORIGINE_ABSOLUE = [get_pos[0] - 30, get_pos[1] - 10]


        # Fonction de clignotement
def clignotte(l1, l2, l3, l4, dodo) :
    # Clignotement en jaune
    temp_r = 0
    temp_g = 0
    b = 0

    for i in range(0,10) :  #ON
        temp_r += 255*0.1
        temp_g += 255*0.1
        laumio.fillColor(int(temp_r),int(temp_g),b)
        time.sleep(dodo)

    for i in range(0,10) :  #OFF
        temp_r += 0*0.1
        temp_g += 0*0.1
        laumio.fillColor(int(temp_r),int(temp_g),b)
        time.sleep(dodo)
#FIN clignotte

        #   Dans la case verrou
def angleLockLights(state) :
    while (state != 3) :    
        match (state) :
            case 0 :           
                speed = 0.8
            case 1 :           
                speed = 0.6
            case 2 :           
                speed = 0.4
            case 3 :           
                speed = 0.2
            
        clignotte(laumio_diag[0], laumio_diag[1], laumio_diag[2], laumio_diag[3], 0.5)
#FIN angleLockLights

        #Fonction check_around
def check_around():
    case_up = map[pos[0] - 1][pos[1]]
    case_down = map[pos[0] + 1][pos[1]]
    case_left = map[pos[0]][pos[1] - 1]
    case_right = map[pos[0]][pos[1] + 1]
    case_here = map[pos[0]][pos[1]]

    print("\t",case_up.__name__)
    print(case_left.__name__,"\t\t",case_right.__name__)
    print("\t",case_down.__name__)

    for i in range(0,2) :
        laumio_up[i].fillColor(case_up.r, case_up.g, case_up.b)

    for i in range(0,2) :
        laumio_down[i].fillColor(case_down.r, case_down.g, case_down.b)

    laumio_left.fillColor(case_left.r, case_left.g, case_left.b)

    laumio_right.fillColor(case_right.r, case_right.g, case_right.b)

    for i in range(0,5) :
        laumio_diag[i].fillColor(case_here.r, case_here.g, case_here.b)
# FIN check_around




# Determination vitesse
def get_speed(pos1, pos2):
    distance = abs(pos2-pos1)
    frame_time = 1 # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    vitesse = distance/frame_time



# FIN deter vitesse







def Victoire():
    for i in range(0,10):
        tab_l[i].rainbow()

def Defaite():
    for l in range(0,10):
        for j in range(0,5) :
            for i in range(0, 3):
                tab_l[l].fillRing(i, 123, 0, 250)
                time.sleep(0.1)
                tab_l[l].fillRing(i, 0, 0, 0)
                time.sleep(0.05)



# Partie principale
for l in tab_l :
    l.fillColor(0,0,0)
pos = [2,1]
score = 10
game_over = False

while(pos != [5,3] and game_over != True) :

    check_around()

    choix_movement = input("1 - Up\n\
2 - Down\n\
3 - Left\n\
4 - Right\n\
Saisir deplacement : ")

    match(choix_movement) :
        case "1" :
            pos = [pos[0] - 1,pos[1]]
        case "2" :
            pos = [pos[0] + 1,pos[1]]
        case "3" :
            pos = [pos[0],pos[1] - 1]
        case "4" :
            pos = [pos[0],pos[1] + 1]

    match(map[pos[0]][pos[1]].__name__) :
        case "case_mur" :
            score -= 1



        case "case_instable" :
            print("ok")
            # fonction get position
           # pos1 = get_position
            #pos2 = get_position

        case "case_lente" :
            print("ok")





        case "case_verrou" :
            """for i in range(0,2) :
                laumio_up[i].fillColor(255, 255, 0) #jaune
            for i in range(0,2) :
                 laumio_down[i].fillColor(255, 255, 255) #blanc
            laumio_left.fillColor(255, 0, 0) #rouge
            laumio_right.fillColor(0, 255, 0) #vert"""

            # Appel fonction
            unlock(id_cle_angle, cle_angle, cle_couleur)
            check_around()

        case "case_border" :
            game_over = True
            score = 0
    print("\n",score)



    if (game_over != True) :
        Victoire()

    else :
        Defaite()