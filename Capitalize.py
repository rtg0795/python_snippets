# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# Capitalize first letters in string

# logic & test
s = 'programming is awesome'
print(s.title())  # method 1
print(' '.join([word.capitalize() for word in s.split()]))  # method 2