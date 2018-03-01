import sys
'''
    Compares text in two files. Ignores whitespace.
'''


def elim_white_space(lines_of_main, lines_of_second):
    # GETS RID OF WHITESPACE, RETURNS A LIST OF TWO LISTS
    lists = [lines_of_main, lines_of_second]
    for i in range(len(lines_of_main)):
        lists[0][i] = lists[0][i].split()
        lists[1][i] = lists[1][i].split()
    return lists


def compare_words(words_of_main, words_of_second):
    # COMPARES NON-WHITESPACE STRINGS, RETURNS LIST WITH NUMBER OF ERRORS AS FIRST ELEMENT AND
    # A LIST OF THE POSITIONS OF ERRORS IN EACH LINE
    false_count = [0, []]
    for i in range(len(words_of_main)):
        if (words_of_main[i] != words_of_second[i]):
            false_count[1].append(i)
            false_count[0] += 1
    return false_count


def compare_lines(first, second):
    # COMPARES NON-WHITESPACE STRINGS OF EACH LINE, RETURNS LIST WITH TOTAL NUMBER OF LINES
    # WITH ERRORS AS FIRST ELEMENT, A LIST WITH THE LOCATIONS OF LINES WITH ERRORS AS SECOND ELEMENT,
    # AND A LIST WITH THE NUMBER OF ERRORS IN EACH LINE
    false_count = [0, [], []]  # [number of errors, locations of lines with errors, number of errors in each line]

    i, j = next(first), next(second)
    while i and j:
        compared = compare_words(i, j)
        if (compared[0] > 0):
            false_count[1].append(i)
            false_count[2].append(compared[0])
            false_count[0] += 1  # Counts number of lines with errors
        i, j = next(first), next(second)
    return false_count


def main():

    try:
        with open(sys.argv[1]) as f1:
            lines1 = (x.strip().split() for x in f1.readlines())  # generator for list of lists
    except FileNotFoundError as e:
        print('The first file was not found.')
        sys.exit()
    try:
        with open(sys.argv[2]) as f2:
            lines2 = (x.strip().split() for x in f2.readlines())  # generator for list of lists
    except FileNotFoundError as e:
        print('The second file was not found.')
        sys.exit()

    results = compare_lines(lines1, lines2)

    print(results)  # [number of errors, locations of lines with errors, number of errors in each line]


if __name__ == '__main__':
    main()
