from math import floor


def sum_of_digits(digit):
    sum = 0
    while floor(digit) > 0:
        remainder = int(digit) % 10
        sum += remainder
        digit = digit / 10
    return sum


def main():
    test_cases = int(input('Enter no of test cases: '))
    results = []
    while (test_cases > 0):
        number = int(input(''))
        results.append(sum_of_digits(number))
        test_cases -= 1

    for result in results:
        print('\n', result)


if __name__ == '__main__':
    main()
