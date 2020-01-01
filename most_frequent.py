# Source
# https://medium.com/better-programming/25-useful-python-snippets-to-help-in-your-day-to-day-work-d59c636ec1b
# frequent element in list

from collections import Counter

# logic
def most_frequent(lst):
    return max(set(lst), key=lst.count)
# test
print(most_frequent([1, 2, 3, 2, 4, 2, 1, 2, 4, 6, 1, 1, 4, 5]))