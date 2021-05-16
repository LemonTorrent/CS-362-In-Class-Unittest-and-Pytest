import wordcount

def test_5words():
    values = ("I like to eat cheese")
    val = wordcount.wordCount(values)
    assert val == 5

def test_spaces_only():
    values = ("    ")
    val = wordcount.wordCount(values)
    assert val == 0

def test_double_spaces():
    values = ("It  was  sunny  today")
    val = wordcount.wordCount(values)
    assert val == 4
