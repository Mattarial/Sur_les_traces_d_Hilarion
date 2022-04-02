from re import A
import sys
import os
import time

import laumio


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

    def unlock(id_cle_angle, cle_couleur, cle_angle) :
                

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

for l in tab_l :
    l.fillColor(0,0,0)

pos = [2,1]

score = 10

game_over = False

while(pos != [5,3] and game_over != True) :
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
        case "case_lente" :
            print("ok")
        case "case_verrou" :
            case_verrou.unlock(case_verrou.id_cle_angle, case_verrou.cle_couleur, case_verrou.cle_angle)
        case "case_border" :
            game_over = True
            score = 0
    print("\n",score)

