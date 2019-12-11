# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# Merge dictionaries


# logic
def merge_two_dicts(a, b):
    c = a.copy()
    c.update(b)
    return c


def merge_dicts(a, b):
    return {**a, **b}


# test
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_two_dicts(a, b))  # 1
print(merge_dicts(a, b))  # 2