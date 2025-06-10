from operator import floordiv

values: dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
                11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
                20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety",  100: "One Hundred", 1000 : "One Thousand",
                1000000: "One Million"}

def figureToWord(number: int) -> str:
    word:str = values.get(number)
    if word:
        return word
    else:
       word = formatWord(number)
    return word


def formatWord(figure: int) -> str:
    word: str = ""
    if 20 < figure < 30:
        word =  values.get(20) + " " + values.get(figure-20)
    elif 30 < figure < 40:
        word = values.get(30) + " " + values.get(figure-30)
    elif 40 < figure < 50:
        word = values.get(40) + " " + values.get(figure-40)
    elif 50 < figure < 60:
        word = values.get(50) + " " + values.get(figure-50)
    elif 60 < figure < 70:
        word = values.get(60) + " " + values.get(figure-60)
    elif 70 < figure < 80:
        word = values.get(70) + " " + values.get(figure-70)
    elif 80 < figure < 90:
        word = values.get(80) + " " + values.get(figure-80)
    elif 90 < figure < 100:
        word = values.get(90) + " " + values.get(figure-90)
    elif 100 < figure < 1000:
        word = values.get(100) + " and "
        if 20 < figure - 100 < 100:
            figure -= 100
            if 20 < figure < 30:
                word += values.get(20) + " " + values.get(figure - 20)
            elif 30 < figure < 40:
                word += values.get(30) + " " + values.get(figure - 30)
            elif 40 < figure < 50:
                word += values.get(40) + " " + values.get(figure - 40)
            elif 50 < figure < 60:
                word += values.get(50) + " " + values.get(figure - 50)
            elif 60 < figure < 70:
                word += values.get(60) + " " + values.get(figure - 60)
            elif 70 < figure < 80:
                word += values.get(70) + " " + values.get(figure - 70)
            elif 80 < figure < 90:
                word += values.get(80) + " " + values.get(figure - 80)
            elif 90 < figure < 100:
                word += values.get(90) + " " + values.get(figure - 90)
        elif figure > 199:
            count = 0
            while figure > 100:
                figure -= 100
                count += 1
            word = values.get(count) + " Hundred "
            if figure != 0:
                word += "and "
            if 20 < figure < 30:
                word += values.get(20) + " " + values.get(figure - 20)
            elif 30 < figure < 40:
                word += values.get(30) + " " + values.get(figure - 30)
            elif 40 < figure < 50:
                word += values.get(40) + " " + values.get(figure - 40)
            elif 50 < figure < 60:
                word += values.get(50) + " " + values.get(figure - 50)
            elif 60 < figure < 70:
                word += values.get(60) + " " + values.get(figure - 60)
            elif 70 < figure < 80:
                word += values.get(70) + " " + values.get(figure - 70)
            elif 80 < figure < 90:
                word += values.get(80) + " " + values.get(figure - 80)
            elif 90 < figure < 100:
                word += values.get(90) + " " + values.get(figure - 90)
            else:
                word += values.get(figure)
        else:
            word += values.get(figure-100)

    return word