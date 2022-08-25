def is_palindrome(string: str):
    # define base case
    if string == "" or len(string) == 1:
        return True
    # progress towards base case
    # and call the function recursively
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])

    # in case given string is not a palindrome
    return False

# print(is_palindrome("kayak"))