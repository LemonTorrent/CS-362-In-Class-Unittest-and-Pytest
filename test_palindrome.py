import unittest
import palindrome

class testCaseAdd(unittest.TestCase):
    def test_bambmab(self):
        self.assertEqual(palindrome.isPalindrome("bambmab"), True)

    def test_fooffoof(self):
        self.assertEqual(palindrome.isPalindrome("baMbmaB"), True)

    def test_greentea(self):
        self.assertEqual(palindrome.isPalindrome("greentea"), False)



if __name__ == '__main__':
    unittest.main()
