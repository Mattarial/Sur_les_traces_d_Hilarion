import sys
import os
import time


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


l = Laumio("192.168.1.21")


l.fillColor(0,0,0)

color_choice = ""

while(str(color_choice) != "7") :

    print("Selectionnez la couleur parmis les suivantes :\n\
    1 - Rouge\n\
    2 - Bleu\n\
    3 - Vert\n\
    4 - Jaune\n\
    5 - Orange\n\
    6 - Magenta\n\
    7 - Blanc\n\
    8 - Noir\n\
    9 - Stop")

    print("\nEntrez la couleur au choix : ")

    color_choice = input()

    if("0" < color_choice and color_choice < "10") :

        print(color_choice + "\n")

        match(color_choice):
            case "1" :
                print(l.fillColor(255,0,0))
            case "2" :
                l.fillColor(0,0,255)
            case "3" :
                l.fillColor(0,255,0)
            case "4" :
                l.fillColor(255,255,0)
            case "5" :
                l.fillColor(255,165,0)
            case "6" :
                l.fillColor(255,0,255)
            case "7" :
                l.fillColor(255,255,255)
            case "8" :
                l.fillColor(0,0,0)


    else : print("Saisie incorrecte")

    
    











