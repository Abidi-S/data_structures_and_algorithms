# non-optimized recursive fibonacci
def fibonacci(n):
    # define base case
    if n == 2 or n == 1:
        return 1
    # progress problem state towards base case
    # and call the function itself
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(27))