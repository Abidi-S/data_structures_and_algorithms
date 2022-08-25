def factorial(n):
    # define base case
    if n == 1:
        return 1
    # progress problem state towards base case
    # and call the function recursively
    return n * factorial(n-1)

# print(factorial(5))