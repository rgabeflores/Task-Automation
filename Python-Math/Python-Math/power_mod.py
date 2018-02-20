'''
	@author Gabriel Flores
	A modular expression calculator that implements modular exponentiation.
'''


def dec_to_bin(x):
    '''
            Takes an integer and constructs a bit array for the binary representation of the integer.
    '''
    return list(map(int, bin(x)[2:]))


def pmod(b, e, m):
    '''
            Uses modular exponentiation to calculate modular expressions with large values.
    '''
    e_bin = dec_to_bin(e)

    x = 1
    power = b % m

    for i in range(len(e_bin) - 1, -1, -1):
        if e_bin[i]:
            x = (x * power) % m
        power = (power ** 2) % m

    return x


def main():

    try:
        print("\n\n")
        print("\n        Format:    \n")
        print("        b^e mod m    \n")

        b = int(input("    Enter b: "))
        e = int(input("    Enter e: "))
        m = int(input("    Enter m: "))

        result = pmod(b, e, m)
        print("\n    Result:", result, "\n")
    except ValueError as e:
        print("\n\n    Please enter a valid choice.\n")


if __name__ == "__main__":
    main()
