# function to recursively convert given decimal to its binary repr

def convert_to_bin(decimal: int):
    # define base case
    if decimal == 0:
        return decimal
    # progress problem state towards base case
    # and call the function itself
    return f"{convert_to_bin(decimal//2)}" + f"{decimal % 2}"

# print(convert_to_bin(233))
# print(bin(233))