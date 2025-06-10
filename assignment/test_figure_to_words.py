import unittest

from figure_to_words_tobi import figureToWord


class MyTestCase(unittest.TestCase):

    def test_something(self):
        ten: int = 10
        actual: str = "Ten"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testConvertOneInFigureToWord(self):
        ten: int = 1
        actual: str = "One"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testConvertTwoInFigureToWord(self):
        ten: int = 2
        actual: str = "Two"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testConvertThreeInFigureToWord(self):
        ten: int = 3
        actual: str = "Three"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testConvertTwentyTwoInFigureToWord(self):
        ten: int = 22
        actual: str = "Twenty Two"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testConvertTwentyNineInFigureToWord(self):
        ten: int = 29
        actual: str = "Twenty Nine"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testConvertThirtyFiveInFigureToWord(self):
        ten: int = 35
        actual: str = "Thirty Five"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testConvertThirtyNineInFigureToWord(self):
        ten: int = 39
        actual: str = "Thirty Nine"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testConvertFortyOneInFigureToWord(self):
        ten: int = 41
        actual: str = "Forty One"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testConvertNinetyNineInFigureToWord(self):
        ten: int = 99
        actual: str = "Ninety Nine"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testThatConvertOneHundredAndOneInFigureToWord(self):
        ten: int = 101
        actual: str = "One Hundred and One"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testThatConvertOneHundredAndThirtyFiveInFigureToWord(self):
        ten: int = 135
        actual: str = "One Hundred and Thirty Five"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testThatConvertOneHundredAndNinetyNineInFigureToWord(self):
        ten: int = 199
        actual: str = "One Hundred and Ninety Nine"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testThatConvertTwoHundredAndOneInFigureToWord(self):
        ten: int = 201
        actual: str = "Two Hundred and One"
        expected: str = figureToWord(ten)
        self.assertEqual(expected, actual)

    def testThatConvertTwoHundredAndTwentyTwoInFigureToWord(self):
        figure: int = 222
        actual: str = "Two Hundred and Twenty Two"
        expected: str = figureToWord(figure)
        self.assertEqual(expected, actual)

    def testThatConvertThreeHundredAndThirtyThreeInFigureToWord(self):
        figure: int = 333
        actual: str = "Three Hundred and Thirty Three"
        expected: str = figureToWord(figure)
        self.assertEqual(expected, actual)

    def testThatConvertNineHundredAndNinetyNineInFigureToWord(self):
        figure: int = 999
        actual: str = "Nine Hundred and Ninety Nine"
        expected: str = figureToWord(figure)
        self.assertEqual(expected, actual)

    def testOneThousandAndOneInFigureToWord(self):
        figure: int = 1001
        actual: str = "One Thousand and One"
        expected: str = figureToWord(figure)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
