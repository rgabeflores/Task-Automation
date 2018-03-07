import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sys

'''
    A basic script to graph test scores and calculate statistical data.
'''


def get_scores():

    # Gets test scores from text file passed as command line arg
    try:
        with open(sys.argv[1]) as data:
            return [int(x.strip()) for x in data.readlines()]
    except FileNotFoundError as e:
        print('File was not found.')
        sys.exit()
    except Exception as e:
        print('''
            Something went wrong...
            Usage:
                python stats.py <file>
            ''')
        sys.exit()


def frame(values, entry):
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
            entry
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


def display(x, y, title):
    plt.bar(x, y, label='Scores')
    plt.xlabel('Score')
    plt.ylabel('Quantity')
    plt.title(title)
    plt.legend()
    plt.show()


def main():

    values = get_scores()
    title = input('Enter a name for these scores:\n')
    frame(values, title)

    x = np.array([i for i in range(min(values), max(values) + 1)])
    y = np.array([0 for i in range(max(values) + 1)])

    # Adds up score quantities
    for j in values:
        y[j] += 1

    display(x, y[min(values):], title)


if __name__ == '__main__':
    main()
