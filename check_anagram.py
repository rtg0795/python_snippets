# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# check if both lists have same items

from collections import Counter


# logic
def anagram(first, second):
    return Counter(first) == Counter(second)


# test
one = 'abcd3'
two = '3cabd'
print(anagram(one, two))