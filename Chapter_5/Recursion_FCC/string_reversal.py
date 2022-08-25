# function to recursively reverse a given string

def reverse(string: str):
    # define base case
    if string == "":
        return ""
    # progress problem state towards base case
    # and call the function itself
    return reverse(string[1:]) + string[0]

# print(reverse("hello world"))