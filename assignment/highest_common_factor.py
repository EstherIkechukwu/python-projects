# def get_highest_common_factor(first_number, second_number):
#     while second_number != 0:
#         remainder = first_number % second_number
#         first_number = second_number
#         second_number = remainder
#     return first_number

def get_highest_common_factor_2(*numbers):
    if not numbers:
        return 0
    numbers = [abs(num) for num in numbers]

    def get_common_factor(first_number, second_number):
        while second_number:
            first_number, second_number = second_number, first_number % second_number
        return first_number

    current_highest_common_factor = numbers[0]
    for num in numbers[1:]:
        current_highest_common_factor = get_common_factor(current_highest_common_factor, num)
        if current_highest_common_factor == 1:
            break

    return current_highest_common_factor
