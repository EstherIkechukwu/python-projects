def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    for bit in reversed(binary_str):
        decimal += int(bit) * (2 ** power)
        power +=1
    return decimal

def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary_str = ''
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str
        n = n // 2
    return binary_str

# def binary_sum(*numbers):
#     total = 0
#     for binary in numbers:
#         total += binary_to_decimal(binary)
#
#     return decimal_to_binary(total)

binary1 = input("Enter the first binary number: ")
binary2 = input("Enter the second binary number: ")

decimal1 = binary_to_decimal(binary1)
decimal2 = binary_to_decimal(binary2)

decimal_sum = decimal1 + decimal2

binary_sum = decimal_to_binary(decimal_sum)

print(f"The sum of {binary1} and {binary2} in binary is: {binary_sum}")

final_sum = binary_sum(binary1, binary2)


