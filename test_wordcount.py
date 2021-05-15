import unittest
import wordcount

class testCaseAdd(unittest.TestCase):
    def test_5words(self):
        self.assertEqual(wordcount.wordCount("I like to eat cheese"), 5)

    def test_spaces_only(self):
        self.assertEqual(wordcount.wordCount("    "), 0)

    def test_double_spaces(self):
        self.assertEqual(wordcount.wordCount("It  was  sunny  today"), 4)


if __name__ == '__main__':
    unittest.main()
