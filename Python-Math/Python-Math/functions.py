'''
	@author Gabriel Flores
	Various mathematical functions concatenated into one script. This script allows
	the user to choose which functions to use.
'''

import check_prime
import decimal_binary
import euclidean_algorithm
import power_mod
import reverse_number
import statistics
import ux

OPTIONS = ["Check Prime", "Decimal/Binary Conversions", "Greatest Common Divisor", "Power Mod Calculation", "Reverse Integer", "Data Set Statistics"]

a = check_prime.main
b = decimal_binary.main
c = euclidean_algorithm.main
d = power_mod.main
e = reverse_number.main
f = statistics.main

def switch(x):
	{
		1: a,
		2: b,
		3: c,
		4: d,
		5: e,
		6: f
	}[x]()

def main():

	def main_loop():
		choice = ux.get_user_choice(OPTIONS)

		switch(choice)

	ux.to_continue(main_loop)


if __name__ == "__main__":
	main()