from matplotlib import pyplot as plt
from statistics import mean, median, mode, stdev, variance

'''
	A basic script to graph test scores and calculate statistical data.
'''


def get_scores():

    # Gets test scores from text file
    try:
        with open('scores.txt') as data:
            values = [int(x.strip()) for x in data.readlines()]
    except FileNotFoundError as e:
        from sys import exit
        print('scores.txt was not found.')
        exit()
    else:
        return values


def output(values):
        # Formats output
    content = 'Mean: {}\nMedian: {}\nMode: {}\nVariance: {}\nStandard Deviation: {}'.format(
        mean(values),
        median(values),
        mode(values),
        variance(values),
        stdev(values))
    print()
    print(content)
    # Writes output to 'results.txt'
    try:
        with open('results.txt', 'w') as output:
            output.write(content)
    except:
        print('Something went wrong while writing to the file.')


def main():

    values = get_scores()
    output(values)

    # X-axis values
    x = [i for i in range(min(values), max(values) + 1)]
    # Y-axis values
    y = [0 for i in range(25)]

    # Adds up score quantities
    for j in values:
        y[j] += 1

    plt.bar(x, y[min(values):], label='Occurrences')
    plt.xlabel('Score')
    plt.ylabel('Quantity')
    plt.title('Exam 1 Scores')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
