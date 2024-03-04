
def compare(digit):
    if digit < 7:
        return 'DOWN'
    elif digit == 7:
        return 'EQUAL'
    else:
        return 'UP'


def main():
    test_cases = int(input('Enter no. of test cases: '))
    array = []
    while (test_cases > 0):
        number = int(input(''))
        array.append(compare(number))
        test_cases -= 1
    for result in array:
        print(result, '\n')


if __name__ == '__main__':
    main()
