# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# remove falsy values like False, None, 0 and '' from a list by filter

lst = [0, 1, False, 2, '', 3, 'a', 's', 34, None]
print(list(filter(None, lst)))  # 1 filter(function, sequence) function as None
print(list(filter(lambda x: x not in [0, False, None, ''], lst)))  # 2 lambda function

