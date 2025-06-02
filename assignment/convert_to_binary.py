def binary_to_decimal(binary):
    decimal = 0
    for i, digit in enumerate(reversed(binary)):
        decimal += int(digit) * (2 ** i)
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    return binary if binary else "0"

binary1 = input("Enter the first binary number: ")
binary2 = input("Enter the second binary number: ")

decimal1 = binary_to_decimal(binary1)
decimal2 = binary_to_decimal(binary2)

decimal_sum = decimal1 + decimal2


binary_sum = decimal_to_binary(decimal_sum)

print(f"The sum of {binary1} and {binary2} in binary is: {binary_sum}")