from matplotlib import pyplot
import random as r
import re
import ux

options = ("Test Random Numbers", "Input Values")


def mean(a):
    '''
            Gets the average of an array of numbers.
    '''

    total = 0

    for i in a:
        total += i

    return total / len(a)


def median(a):
    '''
            Implements Divide & Conquer technique to find the middle element of an array.
    '''
    a.sort()
    if len(a) % 2 == 0:
        return (a[int(len(a) / 2)] + a[int(len(a) / 2) - 1]) / 2
    else:
        return a[int(len(a) / 2)]


def mode(a):
    '''
            Finds the most commonly recurring element in an array.
            Returns None if there is no element with more than one isntance.
    '''
    totals = {"_": 0}

    for i in a:
        if i in totals:
            totals[i] += 1
        else:
            totals[i] = 1

    temp = "_"

    for key in totals:
        if totals[key] > totals[temp]:
            temp = key

    if totals[temp] > 1:
        return temp
    else:
        return None


def variance(a, average=None):
    if average is None:
        average = mean(a)

    total = 0
    for i in a:
        total += (average - i) ** 2

    return total / len(a)


def std_dev(a, average=None, var=None):
    '''
            Finds the the standard deviation of elements in an array.
    '''
    if average is None:
        average = mean(a)
    if var is None:
        var = variance(a, average)

    return var ** 0.5


def randomTest():

    n = int(input("\tEnter the size of the list to test: "))

    values = [r.randint(0, 100) for i in range(n)]

    return values


def userInputTest(values=None):
    if values is None:
        user_input = input("    Enter the values separated by commas or spaces: ")
        values = [int(x.strip()) for x in re.split(' |, |\n', user_input)]

    return values


def main(x):

    def main_loop():
        choice = ux.get_user_choice(options)

        print("\n")

        if choice == 1:
            values = randomTest()
        elif choice == 2:
            if x is None:
                values = userInputTest()
            else:
                values = userInputTest(values=x)

        print("\n\tValues:", values, "\n")

        results = {
            "HIGH": max(values),
            "LOW": min(values),
            "MEAN": mean(values),
            "MEDIAN": median(values),
            "MODE": mode(values),
            "VARIANCE": variance(values),
            "STANDARD DEVIATION": std_dev(values)
        }

        for key in results.keys():
            print("\t\t{}: {}".format(key, results[key]))
        print("\n\n")

        pyplot.plot(values)

        for key in results.keys():
            if key != 'VARIANCE':
                pyplot.plot([results['{}'.format(key)] for i in range(len(values))], label=key)
        # pyplot.plot([_mean for i in values], label="Mean")
        # pyplot.plot([_median for i in values], label="Median")
        # pyplot.plot([_mode for i in values], label="Mode")
        # # pyplot.plot([_variance for i in values], label="Variance")
        # pyplot.plot([_std_dev for i in values], label="Standard Deviation")

        pyplot.legend()
        pyplot.show()

    ux.to_continue(main_loop)


if __name__ == "__main__":
    main()
