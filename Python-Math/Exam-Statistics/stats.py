from matplotlib import pyplot as plt
from statistics import mean, median, mode, stdev, variance


def main():

    with open('scores.txt') as data:
        values = [int(x.strip()) for x in data.readlines()]

    x = [i for i in range(min(values), max(values) + 1)]
    y = [0 for i in range(25)]

    for j in values:
        y[j] += 1

    with open('results.txt', 'w') as output:
        content = 'Mean: {}\nMedian: {}\nMode: {}\nVariance: {}\nStandard Deviation: {}'.format(
            mean(values),
            median(values),
            mode(values),
            variance(values),
            stdev(values))
        print()
        print(content)
        output.write(content)

    plt.bar(x, y[min(values):], label='Occurrences')
    plt.xlabel('Score')
    plt.ylabel('Quantity')
    plt.title('Exam 1 Scores')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
