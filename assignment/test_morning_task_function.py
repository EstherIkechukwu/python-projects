import unittest
import morning_task_function
import highest_common_factor


class MyTestCase(unittest.TestCase):
    def test_that_compare_strings_exist(self):
        word1 = "abcde"
        word2 = "cdeab"
        actual = morning_task_function.compare_strings(word1, word2)
        expected = True
        self.assertEqual(actual, expected)

    def test_that_compare_strings_returns_correct_value(self):
        word1 = "cba"
        word2 = "abc"
        actual = morning_task_function.compare_strings(word1, word2)
        expected = False
        self.assertEqual(actual, expected)

    def test_that_compare_strings_returns_correct_value_2(self):
        word1 = "13456"
        word2 = "45613"
        actual = morning_task_function.compare_strings(word1, word2)
        expected = True
        self.assertEqual(actual, expected)

    def test_that_compare_strings_returns_correct_value_3(self):
        word1 = "ab"
        word2 = "ba"
        actual = morning_task_function.compare_strings(word1, word2)
        expected = True
        self.assertEqual(actual, expected)

    def test_that_compare_strings_returns_correct_value_4(self):
        word1 = "12356"
        word2 = "35612"
        actual = morning_task_function.compare_strings(word1, word2)
        expected = True
        self.assertEqual(actual, expected)

    def test_for_hcf(self):
        actual = highest_common_factor.get_highest_common_factor(20, 30, 10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_for_hcf_2(self):
        actual = highest_common_factor.get_highest_common_factor_2( 30, 15)
        expected = 15
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
