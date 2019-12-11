# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# difference

counter_list = []

# logic
def difference(lst1, lst2):
    return set(lst1) - set(lst2)


# test
print(difference([1, 2, 3], [1, 2, 4]))