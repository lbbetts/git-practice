def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """

    max_testing = numbers[0]

    for n in range(numbers):
        if numbers[n] > max_testing:
            max_testing = numbers[n]

    return max_testing

    


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
