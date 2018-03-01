import sys
from difflib import ndiff
'''
    Compares text in two files. Ignores whitespace.
'''


def main():

    try:
        with open(sys.argv[1]) as f1:
            lines1 = f1.readlines()
    except FileNotFoundError as e:
        sys.exit('The first file was not found.')
    try:
        with open(sys.argv[2]) as f2:
            lines2 = f2.readlines()
    except FileNotFoundError as e:
        sys.exit('The second file was not found.')

    results = ndiff(lines1, lines2)
    print(''.join(results))


if __name__ == '__main__':
    main()
