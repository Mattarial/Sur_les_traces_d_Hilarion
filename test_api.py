from re import A
import sys
import os
import time

import laumio


sys.path.append(os.path.dirname(sys.argv[0])+'/../')


from laumio import *

def gradient(laumio : Laumio,o_r,o_g,o_b,c_r,c_g,c_b) :
    
    diff_r = c_r - o_r
    diff_g = c_g - o_g
    diff_b = c_b - o_b

    temp_r = o_r
    temp_g = o_g
    temp_b = o_b

    for i in range(0,10) :

        temp_r += diff_r*0.1
        temp_g += diff_g*0.1
        temp_b += diff_b*0.1

        laumio.fillColor(int(temp_r),int(temp_g),int(temp_b))

        time.sleep(0.05)

        print(int(temp_r),"\t",int(temp_g),"\t",int(temp_b))

    return [int(temp_r),int(temp_g),int(temp_b)]


def fluid_column(laumio : Laumio,o_r,o_g,o_b,c_r,c_g,c_b) :

    tab_color_c = [[o_r,o_g,o_b],
                   [o_r,o_g,o_b],
                   [o_r,o_g,o_b],
                   [o_r,o_g,o_b]]

    diff_r = c_r - o_r
    diff_g = c_g - o_g
    diff_b = c_b - o_b
    
    tab_temp_color_c = tab_color_c
    
    temp_r = o_r
    temp_g = o_g
    temp_b = o_b

    for i in range(0,10) :

        temp_r += diff_r*0.1
        temp_g += diff_g*0.1
        temp_b += diff_b*0.1

        #laumio.fillColor(int(temp_r),int(temp_g),int(temp_b))

        for j in range(0,4) :

            laumio.fillColumn(j,int(temp_r),int(temp_g),int(temp_b))

            time.sleep(0.05)


        print(int(temp_r),"\t",int(temp_g),"\t",int(temp_b))

    return [int(temp_r),int(temp_g),int(temp_b)]


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

tab_color_l = [[0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0]]

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

r = 0
g = 255
b = 0

for i in range(0,12) :
    maj_color = gradient(tab_l[laumio_choice],tab_color_l[laumio_choice][0],tab_color_l[laumio_choice][1],tab_color_l[laumio_choice][2],r,g,b)

    tab_color_l[laumio_choice] = maj_color

    #maj_color = gradient(tab_l[laumio_choice],tab_color_l[laumio_choice][0],tab_color_l[laumio_choice][1],tab_color_l[laumio_choice][2],0,0,0)

    #tab_color_l[laumio_choice] = maj_color

    r, g, b = g, b, r


"""
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
"""

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