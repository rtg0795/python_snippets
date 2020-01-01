# Source
# https://medium.com/better-programming/25-useful-python-snippets-to-help-in-your-day-to-day-work-d59c636ec1b
# Average of list of numbers

import itertools

# logic
def average(lst):
    return float((sum(lst)) / len(lst))

# test
print(average([1, 2, 3, 2, 4]))