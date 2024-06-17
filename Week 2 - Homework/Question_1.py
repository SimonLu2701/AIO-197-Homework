# Q1
def is_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False


def user_input_k():
    k = input("Input k (k must be number from 0 to 10): ")
    if is_number(k) == True:
        k = int(k)
        print("List of max number:", find_max_number_list(k))
    else:
        print("k must be number from 0 to 10")


def find_max_number_list(k):
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    kernel_list = []
    max_number_list = []

    for value in num_list:
        kernel_list.append(value)
        if len(kernel_list) == k:

            max_number = max(kernel_list)
            max_number_list.append(max_number)

            del (kernel_list[0])
    return max_number_list


user_input_k()
