#!/usr/bin/python3
for i in range(0, 100):
    if i < 10 or i < int(str(i)[1] + str(i)[0]):
        print("{:02d}".format(i), end=(", ", "\n")[i == 89])
