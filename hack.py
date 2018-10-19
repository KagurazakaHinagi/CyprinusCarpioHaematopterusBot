import time
import random

status = 0
luckyNumber = 1020
Cool_down = 5

lasthack = 0
current = int(time.time())

class Hack():
	def __init__():
		if status == 0:
			return -2

		if(current >= lasthack + Cool_down):
			hackNumber = random.randint(1000,1999)
			if hackNumber == luckyNumber:
				return 1;
			else:
				lasthack = current
				return 0;
		else:
			return -1;

class Control():
	def __init__(number):
		status = number