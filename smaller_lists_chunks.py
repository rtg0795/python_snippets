# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# list to specified size smaller lists

# logic
def chunk(list, size):
    return [list[i: i + size] for i in range(0, len(list), size)]

# test
print(chunk([1, 2, 3, 4, 5, 6, 7], 2))