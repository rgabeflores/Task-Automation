'''
	@author Gabriel Flores
	Implementations of binary to decimal and decimal to binary conversions.
	Binary is represented as a boolean array.
'''
from ux import get_user_choice

OPTIONS = ("Decimal -> Binary", "Binary -> Decimal")


def dec_to_bin(x):
    '''
            Takes an integer and constructs a boolean array for the binary representation of the integer.
    '''
    return list(map(bool, bin(x)[2:]))


def bin_to_dec(binary):
    '''
            Takes a boolean array as a binary representation and calculates the integer value.
    '''
    dec = 0
    e = len(binary) - 1
    for i in binary:
        if i:
            dec += 2 ** e
        e -= 1
    return dec


def parse_bin(binary_str):
    '''
            Parses a string of bits into a boolean array.
    '''
    return list(map(int, binary_str))


def print_bin(binary):
    for i in binary:
        if i:
            print("1", end="")
        else:
            print("0", end="")
    print("\n")


def main():

    choice = get_user_choice(OPTIONS)
    print("\n\n")
    if choice == 1:
        a = int(input("    Enter an integer in decimal: "))
        result = dec_to_bin(a)

        # Output
        print("\n    Decimal:", a, "\n")
        print("\n    Binary: ", end="")
        print_bin(result)
    elif choice == 2:
        a = input("    Enter a binary string: ")
        a_bin = parse_bin(a)
        result = bin_to_dec(a_bin)

        # Output
        print("\n    Binary: ", end="")
        print_bin(a_bin)
        print("\n    Decimal:", result, "\n")


if __name__ == "__main__":
    main()
