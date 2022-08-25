def recursive_reverse(listicle):
    # define a base case
    if len(listicle) == 0:
        return list()
    # progress program state towards base case
    # and call the function itself
    return recursive_reverse(listicle[1:]) + [listicle[0]]

# new_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(recursive_reverse(new_list))