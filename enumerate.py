# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# Enumerate to get index and elements of list


# logic & test
lst = ['a', 'b', 'c', 'd']
for index, element in enumerate(lst):
    print(f'lst[{index}] = {element}')