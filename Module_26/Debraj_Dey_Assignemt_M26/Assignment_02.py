

def average_weight(weights):
    weights = weights.split(' ')
    sum = 0
    for weight in weights:
        sum += int(weight)
    return (sum/10)


def main():
    array = input('')
    print(average_weight(array))


if __name__ == '__main__':
    main()
