# Source
# https://medium.com/better-programming/25-useful-python-snippets-to-help-in-your-day-to-day-work-d59c636ec1b
# Union of lists

import itertools

# logic
def union_of_lists(*args):
    union = []
    for item in itertools.chain([arg for arg in args]):
        [union.append(item[i]) for i in range(len(item))]
    return list(set(union))

# test
print(union_of_lists([1, 2, 5], [5, 4, 3, 9, 1], [10, 55]))
