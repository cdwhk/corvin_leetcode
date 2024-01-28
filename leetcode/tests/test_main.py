from leetcode.main import is_palindrome, fibonacci

def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False

def test_fibonacci():
    assert fibonacci(5) == 5
    assert fibonacci(7) == 13