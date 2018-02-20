'''
	@author Gabriel Flores
	Checks the primality of an integer.
'''

def is_prime(x):
	'''
		Checks the primality of an integer.
	'''
	sqrt = int(x ** (1/2))
	for i in range(2, sqrt, 1):
		if x % i == 0:
			return False
	return True

def main():

	try:
		print("\n\n")
		a = int(input("    Enter an integer to check if it is prime: "))
		if is_prime(a):
			print("\n   ",a,"is a prime number.\n")
		else:
			print("\n   ",a,"is not a prime number.\n")
	except ValueError as e:
		print("\n\n    Please enter a valid choice.\n")


if __name__ == "__main__":
	main()