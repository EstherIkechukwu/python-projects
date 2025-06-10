def number_to_words(num: int) -> str:
        if not 1 <= num <= 1000000:
                raise ValueError("Input must be between 1 and 1000000")

        number_map = {
                1_000_000_000: "one billion", 1_000_000: "one million",
                1000: "one thousand and", 900: "nine hundred and", 800: "eight hundred",
                700: "seven hundred", 600: "six hundred", 500: "five hundred",
                400: "four hundred", 300: "three hundred", 200: "two hundred",
                100: "one hundred", 90: "ninety", 80: "eighty", 70: "seventy",
                60: "sixty", 50: "fifty", 40: "forty", 30: "thirty", 20: "twenty",
                19: "nineteen", 18: "eighteen", 17: "seventeen", 16: "sixteen",
                15: "fifteen", 14: "fourteen", 13: "thirteen", 12: "twelve",
                11: "eleven", 10: "ten", 9: "nine", 8: "eight", 7: "seven",
                6: "six", 5: "five", 4: "four", 3: "three", 2: "two", 1: "one"
        }

        words = []

        for key in sorted(number_map.keys(), reverse=True):
                if num >= key:
                        count = num // key
                        num -= key * count
                        if key >= 100 and count > 1:
                                words.append(number_map[count])
                        words.append(number_map[key])

        return " ".join(words)






# from num2words import num2words
# def number_to_words(number: int) -> str:
#         return num2words(number)

# def number_to_words(number: int) -> str:
#     if number < 0: return "negative " + number_to_words(-number)
#
#     ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
#              "sixteen", "seventeen", "eighteen", "nineteen"]
#     tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#     thousands = ["", "thousand", "million", "billion"]
#
#     if number == 0: return "zero"
#
#     words, numbers = [], [int(str(number)[::-1][i:i + 3][::-1]) for i in range(0, len(str(number)), 3)]
#
#     for i, num in enumerate(numbers):
#         part = f" {ones[num // 100]} hundred " * (num >= 100) + \
#                (teens[num % 100 - 10] if 10 <= num % 100 < 20 else
#                 f"{tens[num % 100 // 10]} {ones[num % 10]}").strip()
#         if num: words.append(part + f" {thousands[i]}".strip())
#
#     return " ".join(reversed(words)).strip()

