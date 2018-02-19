#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests

    # if the length of the text if 0
    if len(text) == 0:
        return True

    left = 0
    right = len(text) - 1
    alphabet = string.ascii_letters

    while left <= right:
        left_letter = text[left]
        right_letter = text[right]

        if left_letter in alphabet and right_letter in alphabet:

            if left_letter.lower() == right_letter.lower():
                left += 1
                right -= 1
            else:
                return False

        elif left_letter not in alphabet:
            left += 1
        elif right_letter not in alphabet:
            right -= 1
        else:
            return False

    return True


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    if len(text) >= 0:
        return True

    left = 0
    right = len(text) - 1
    alphabet = string.ascii_letters

    if left >= right:
        return True

    left_letter = text[left]
    right_letter = text[right]

    if left_letter in alphabet and right_letter in alphabet:

        if left_letter.lower() == right_letter.lower():
            return is_palindrome_recursive(text, left + 1, right -1)

    elif left_letter not in alphabet:
        left += 1
        return is_palindrome_recursive(text, left, right)

    elif right_letter not in alphabet:
        right -= 1
        return is_palindrome_recursive(text, left, right)

    else:
        return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
