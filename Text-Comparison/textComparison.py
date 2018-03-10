import sys
from difflib import ndiff
'''
    Compares text in two files. Made for testing generated output from student
    assignment submissions against expected output from correct code.
'''


def main():

    content = []

    for arg in sys.argv[1:]:
        try:
            with open('./'.format(arg)) as f:
                content.append(f.readlines())
        except FileNotFoundError as e:
            sys.exit('One of the files is missing or misplaced.')
        except Exception as e:
            sys.exit('Something went wrong.')

    results = ndiff(content[0], content[1])
    print(''.join(results))


if __name__ == '__main__':
    main()
