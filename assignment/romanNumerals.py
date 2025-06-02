def int_to_roman(num: int) -> str:
    if not 1 <= num <= 100:
        raise ValueError("Input must be between 1 and 100")

    values = [
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = []
    for value, numeral in values:
        while num >= value:
            result.append(numeral)
            num -= value
    return ''.join(result)


print(int_to_roman(1))
print(int_to_roman(8))

