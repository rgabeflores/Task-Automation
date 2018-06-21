import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sys

'''
    A basic script to graph test score quantities and calculate statistical data.
'''


def retrieve():

    # Gets test scores from text file passed as command line arg
    try:
        with open(sys.argv[1]) as data:
            return [int(x.strip()) for x in data.readlines()]
    except FileNotFoundError as e:
        sys.exit('\nFile was not found.\n')
    except Exception as e:
        sys.exit('''
            Something went wrong...
            Usage:
                python stats.py <file>
            ''')


def build(values, entry):
    '''
        Builds a DataFrame of the statistical results. The DataFrame is output to 
        both the console and a results.txt file
    '''
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

    print("\n", df, "\n")

    try:
        with open('results.txt', 'w') as output:
            output.write(df.to_string())
    except Exception as e:
        print(e)


def display(x, y, title=None):
    plt.bar(x, y, label='Scores')
    if title:
        plt.title(title)
    plt.xlabel('Score')
    plt.ylabel('Quantity')
    plt.legend()
    plt.show()


def main():
    values = retrieve()
    title = input('\n\tEnter a name for these scores:\n\t')
    build(values, title=title)

    # x is the domain of scores, y is the quantities of each score
    x = np.array([i for i in range(min(values), max(values) + 1)])
    y = np.array([0 for i in range(max(values) + 1)])

    # Adds up score quantities
    for j in values:
        y[j] += 1

    display(x, y[min(values):], title)


if __name__ == '__main__':
    main()
