def calculate(numbers):
    symbols = []
    operands = []
    num = ""

    for char in numbers:
        if char.isdigit() or char == ".":
            num += char
        else:
            if num:
                operands.append(int(num))
                num = ""
            if char in "%*+-/":
                symbols.append(char)

    if num:
        operands.append(int(num))

    result = operands[0]
    for i in range(len(symbols)):
        if symbols[i] == "+":
            result += operands[i + 1]
        elif symbols[i] == "-":
            result -= operands[i + 1]
        elif symbols[i] == "*":
            result *= operands[i + 1]
        elif symbols[i] == "/":
            result /= operands[i + 1]
        elif symbols[i] == "%":
            result %= operands[i + 1]

    return result


print(calculate("9 + 4 * 2"))
