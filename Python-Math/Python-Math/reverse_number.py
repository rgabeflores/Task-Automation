'''
	@author Gabriel Flores
	Reverses the digits of an integer.
'''

def reverse_num(num):
	'''
		Takes an integer and returns the integer with reversed digits.
	'''
	final = 0

	while(num != 0):
		r = num % 10
		num = int(num / 10)
		final = (final * 10) + r

	return final

def main():

	try:
		print("\n\n")
		a = int(input("    Enter an integer to reverse: "))
		_a = reverse_num(a)
		# Output
		print("\n\tOriginal", a)
		print("\tReversed", _a)
		print("\n")

	except ValueError as e:
		print("\n\n    Please enter a valid choice.\n")

if __name__ == "__main__":
	main()