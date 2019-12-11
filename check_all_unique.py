# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# Check if all items in list are unique

#logic
def all_unique(lst):
    return len(lst) == len(set(lst))


# test
x = [1,2,3,4,5,2,8]
print(all_unique(x))