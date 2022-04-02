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

for l in tab_l :
    l.fillColor(0,0,0)

color_choice = ""
laumio_choice = -1

while(str(color_choice) != "9") :

    print("Selectionnez le laumio parmis les suivants :\n\
            0\t1\t2\t3\n\
            9\t\t\t4\n\
            8\t7\t6\t5")
        
    print("\nEntrez le laumio au choix : ")

    laumio_choice = int(input())

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

    if(color_choice == "1" 
    or color_choice == "2" 
    or color_choice == "3" 
    or color_choice == "4" 
    or color_choice == "5" 
    or color_choice == "6"
    or color_choice == "7"
    or color_choice == "8") :

        print(color_choice + "\n")

        match(color_choice):
            case "1" :
                print(tab_l[laumio_choice].fillColor(255,0,0))
            case "2" :
                tab_l[laumio_choice].fillColor(0,0,255)
            case "3" :
                tab_l[laumio_choice].fillColor(0,255,0)
            case "4" :
                tab_l[laumio_choice].fillColor(255,255,0)
            case "5" :
                tab_l[laumio_choice].fillColor(255,165,0)
            case "6" :
                tab_l[laumio_choice].fillColor(255,0,255)
            case "7" :
                tab_l[laumio_choice].fillColor(255,255,255)
            case "8" :
                tab_l[laumio_choice].fillColor(0,0,0)


    else : print("Saisie incorrecte")

    
    











