from math import floor


input_array = [42, 564, 5775, 34, 123, 454, 1, 5, 45, 3556, 23442]


def has_even_digit(digit):
    count = 0
    while floor(digit) != 0:
        digit = digit/10
        count += 1
    if (count % 2 == 0):
        return True
    else:
        return False


def find_even_digits(array):
    even_digits = []
    for digit in array:
        if has_even_digit(int(digit)):
            even_digits.append(digit)

    return even_digits


def main():
    test_cases = int(input('Enter no. of test cases: '))
    array = []
    while test_cases > 0:
        user_input = input('')
        user_input = user_input.split(' ')
        user_input = user_input[1:]
        array.append(find_even_digits(user_input))
        test_cases -= 1

    for result in array:
        print('\n')
        for digits in result:
            print(digits, end=' ')


if __name__ == '__main__':
    main()
