def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """

    highest = float('-inf')
    for i in range(len(numbers)):
        if numbers[i] > highest:
            highest = numbers[i]
    return highest


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
