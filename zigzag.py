#!/usr/bin/python3
"""
Test2-20-1
"""
###############################################################################

__author__ = "Jared Winter"
__copyright__ = "Copyright 2020, jwinternet"
__credits__ = ""
__license__ = "GNU GPL v3"
__version__ = "0.0.1"
__updated__ = "2/25/2020"
__email__ = "jaredwinter2015@outlook.com"
__contributors__ = ""
__status__ = "DEV"

###############################################################################

import time, sys

indent = 0  # How many spaces to indent.
indentIncreasing = True  # Whether the indentation is increasing or not.

try:
	while True:  # The main program loop.
		print(' ' * indent, end='')
		print('********')
		time.sleep(0.1)  # Pause for 1/10 of a second.

		if indentIncreasing:
			# Increase the number of spaces:
			indent = indent + 1
			if indent == 20:
				# Change direction:
				indentIncreasing = False

		else:
			# Decrease the number of spaces:
			indent = indent - 1
			if indent == 0:
				# Change direction:
				indentIncreasing = True
except KeyboardInterrupt:
	sys.exit()


###############################################################################

#if __name__ == "__main__":
#	error_handling()