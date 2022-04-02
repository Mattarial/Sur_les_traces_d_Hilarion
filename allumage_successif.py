from msilib.schema import tables
from re import L
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

stop = ""

while(stop != "0") :

    print(tab_l[0].fillColor(255,0,0))
    time.sleep(1)
    print(tab_l[1].fillColor(0,0,255))
    time.sleep(1)
    print(tab_l[2].fillColor(255,165,0))
    time.sleep(1)
    print(tab_l[3].fillColor(255,0,255))
    time.sleep(1)
    print(tab_l[4].fillColor(0,255,0))
    time.sleep(1)
    print(tab_l[5].fillColor(255,0,0))
    time.sleep(1)
    print(tab_l[6].fillColor(0,0,255))
    time.sleep(1)
    print(tab_l[7].fillColor(255,0,255))
    time.sleep(1)
    print(tab_l[8].fillColor(255,165,0))
    time.sleep(1)
    print(tab_l[9].fillColor(255,255,0))

    stop = input("Entrez 0 pour arreter :")

    for l in tab_l :
        l.fillColor(0,0,0)
        time.sleep(0.5)
