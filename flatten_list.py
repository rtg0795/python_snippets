# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
#  flatten nested list with recursion

counter_list = []


# logic
def deep_flatten(lst):
    for x in lst:
        if isinstance(x, list):
            deep_flatten(x)
        else:
            counter_list.append(x)
    return counter_list


# test
print(deep_flatten([1, [2], [[3], 4, 5, [4, 6, 8]]]))