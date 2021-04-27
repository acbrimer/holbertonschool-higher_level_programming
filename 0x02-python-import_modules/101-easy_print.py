#!/usr/bin/python3
import os
if __name__ == '__main__':
	outfd = os.fdopen(1, 'w')
	outfd.write("#pythoniscool\n")
	outfd.close()
