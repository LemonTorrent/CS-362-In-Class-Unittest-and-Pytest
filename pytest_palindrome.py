import palindrome

def test_palindrome():
    values = ("bambmab")
    val = palindrome.isPalindrome(values)
    assert val == 1

def test_capital_palindrome():
    values = ("baMbmaB")
    val = palindrome.isPalindrome(values)
    assert val == 1

def test_false_palindrome():
    values = ("greentea")
    val = palindrome.isPalindrome(values)
    assert val == 0
