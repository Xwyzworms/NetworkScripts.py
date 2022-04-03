import subprocess
import argparse
import random
from typing import List

def get_interface():
	pass

def change_the_mac():
	pass


def generate_random_mac() ->  str:
	"""
	This Fun Will genereate Random Mac Address, 
	"""
	rand : List = [
		random.randint(0xA, 0x64) for i in range(6)
	]
	new_mac= ""
	for i in range(len(rand) - 1):
		new_mac = new_mac + str(rand[i]) + "::"
	new_mac = new_mac + str(rand[-1])
	return new_mac

if __name__ =="__main__":
	#interface = get_interface()
	generate_random_mac()
	new_mac = "22:12:12:23:33:44"

	#subprocess.run([""])
