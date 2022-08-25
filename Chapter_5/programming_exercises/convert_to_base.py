# function to convert decimal to given base

def convert_to_base(decimal: int, base: int):
    to_base_repr = "0123456789ABCDEF"
    # define base case
    if decimal == 0:
        return decimal
    # progress problem state towards base case
    # and call the function itself
    return f"{convert_to_base(decimal//base, base)}" + f"{to_base_repr[decimal % base]}"

# print(convert_to_base(233, 16))
# print(hex(233))