import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

'''
    A basic script to graph test scores and calculate statistical data.
'''


def get_scores():

    # Gets test scores from text file
    try:
        with open('scores.txt') as data:
            return [int(x.strip()) for x in data.readlines()]
    except FileNotFoundError as e:
        from sys import exit
        print('scores.txt was not found.')
        exit()


def output(values):
    # Formats output
    df = pd.DataFrame(pd.Series([
        np.amin(values),
        np.amax(values),
        np.mean(values),
        np.median(values),
        np.var(values),
        np.std(values)
    ], [
        'Min',
        'Max',
        'Mean',
        'Median',
        'Variance',
        'Standard Deviation'
    ]),
        columns=[
            'Exam 1'
    ]
    )

    print()
    print(df)
    print()

    try:
        # Writes output to 'results.txt'
        with open('results.txt', 'w') as output:
            output.write(df.to_string())
    except Exception as e:
        print(e)
        # print('Something went wrong while writing to the file.')


def main():

    values = get_scores()
    output(values)

    # X-axis values
    x = np.array([i for i in range(min(values), max(values) + 1)])
    # Y-axis values
    y = np.array([0 for i in range(25)])

    # Adds up score quantities
    for j in values:
        y[j] += 1

    plt.bar(x, y[min(values):], label='Scores')
    plt.xlabel('Score')
    plt.ylabel('Quantity')
    plt.title('Exam 1 Scores')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
