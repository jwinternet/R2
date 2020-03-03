#!/usr/bin/python3
"""
Collatz Sequence Program
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

def collatz(number):
	if number % 2 == 0:
		print(number // 2)
		return number // 2
	elif number % 2 == 1:
		result = 3 * number + 1
		print(result)
		return result


###############################################################################

something = input("Enter in a number: ")
while something != 1:
	something = collatz(int(something))