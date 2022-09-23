def most_common_value(number_list):
    """ returns the most common element of the list
    """
    most_occurences_count = {}

    for num in range(number_list):
        most_occurences_count[num] = 0

    for each_num in most_occurences_count():
        real_count = most_occurences_count.count(each_num)
        most_occurences_count[each_num] = real_count

    most_common_num = None
    num_occured = 0

    for n in most_occurences_count.keys():
        if most_occurences_count[n] > num_occured:
            most_common_num = n
            num_occured = most_occurences_count[n]
    
    return most_common_num



if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
