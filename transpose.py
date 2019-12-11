# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# transpose array with zip

# logic & test
array = [['a', 'b'], ['c', 'd'], ['e', 'f']] # each row and column should be same length
print(list(zip(*array)))