import os
import sys

with open("Dicc.txt","w+") as arch:
    for i in range(10000000):
        arch.write("tele-"+str(i).zfill(7)+"\n")

cadena="aircrack-ng -w Dicc.txt "+sys.argv[1]
os.system(cadena)

os.remove("Dicc.txt")