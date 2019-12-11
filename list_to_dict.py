# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# Convert two lists to dictionaries


# logic
def to_dict(keys, values):
    return dict(zip(keys, values))


# test
keys = ['a', 'b', 'c']
values = [2, 3, 4]
print(to_dict(keys, values))