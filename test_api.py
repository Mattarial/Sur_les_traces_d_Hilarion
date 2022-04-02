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

print("Selectionnez le laumio parmis les suivants :\n\
        0\t1\t2\t3\n\
        9\t\t\t4\n\
        8\t7\t6\t5")
        
print("\nEntrez le laumio au choix : ")

laumio_choice = int(input())

tab_l[laumio_choice].fillColor(25,0,0)
time.sleep(0.1)
tab_l[laumio_choice].fillColor(50,0,0)
time.sleep(0.1)
tab_l[laumio_choice].fillColor(75,0,0)
time.sleep(0.1)
tab_l[laumio_choice].fillColor(100,0,0)
time.sleep(0.1)
tab_l[laumio_choice].fillColor(125,0,0)
time.sleep(0.1)
tab_l[laumio_choice].fillColor(150,0,0)
time.sleep(0.1)
tab_l[laumio_choice].fillColor(175,0,0)
time.sleep(0.1)
tab_l[laumio_choice].fillColor(200,0,0)
time.sleep(0.1)
tab_l[laumio_choice].fillColor(225,0,0)
time.sleep(0.1)
tab_l[laumio_choice].fillColor(250,0,0)
time.sleep(0.1)

#tab_l[laumio_choice].fillColor(255,0,0)
#tab_l[laumio_choice].colorWipe(0,0,255,25)

#tab_l[laumio_choice].rainbow()

#tab_l[laumio_choice].fillColor(127,0,0)
#time.sleep(2)
#tab_l[laumio_choice].fillColor(255,0,0)

#tab_l[laumio_choice].fillColumn(0,0,0,255)
#tab_l[laumio_choice].fillColumn(1,255,255,255)
#tab_l[laumio_choice].fillColumn(2,255,255,255)
#tab_l[laumio_choice].fillColumn(3,0,0,255)

#for j in range(0,5) :
 #   for i in range(0, 3):
  #      tab_l[laumio_choice].fillRing(i, 123, 0, 250)
   #     time.sleep(0.1)
    #    tab_l[laumio_choice].fillRing(i, 0, 0, 0)
     #   time.sleep(0.05)