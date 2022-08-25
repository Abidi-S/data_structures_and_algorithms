# function to recursively calculate the sum of n natural numbers

def recursive_sum(n: int):
    # define base case
    if n == 1:
        return 1
    # progress problem state towards base case
    # and call the function itself
    return n + recursive_sum(n-1)

# print(recursive_sum(10))