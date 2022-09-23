# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    sum = 0
    user_input = None
    while sum <= 1000 and user_input != 0:
        user_input = input("Please enter a number: ")
        try:
            user_input = int(user_input)
        except:
            print("Please enter valid integers only.")
            continue
        sum += user_input
    return sum


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
