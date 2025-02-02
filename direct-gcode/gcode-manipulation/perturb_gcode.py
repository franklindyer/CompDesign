import sys
import re
import random

MAX_PERTURBANCE = 2

filename = sys.argv[1]
new_gcode = ""

with open(filename) as file:
    for line in file:
        match = re.match("G1 X([0-9\.]+) Y([0-9\.]+) E([0-9\.]+)", line)
        if match:
            qx = float(match[1])
            qy = float(match[2])
            qe = float(match[3])
            qx += MAX_PERTURBANCE * (2*random.random() - 1)
            new_command = "G1 X" + str(qx) + " Y" + str(qy) + " E" + str(qe) + "\n"
            new_gcode += new_command
        else:
            new_gcode += line

print(num_moves)
new_file = open("perturbed.gcode", 'w')
new_file.write(new_gcode)
new_file.close()
