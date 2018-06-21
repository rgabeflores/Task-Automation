import sys
import logging
from difflib import ndiff, context_diff

'''
    Compares text in two files. Made for testing generated output from student
    assignment submissions against expected output from correct code.

    Prints results to screen and logs to file.
'''
logging.basicConfig(filename='results.log', level=logging.INFO)


def main():

    content = []

    for arg in sys.argv[1:]:
        try:
            with open('./{}'.format(arg)) as f:
                content.append(f.readlines())
        except FileNotFoundError as e:
            sys.exit('\nOne of the files is missing or misplaced.\n')
        except Exception as e:
            sys.exit('\nSomething went wrong.\n')

    results = ''.join(ndiff(content[0], content[1]))
    print(results)
    logging.info(results)


if __name__ == '__main__':
    main()
