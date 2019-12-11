# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# Decapitalize first letter in string


# logic
def de_capitalize(string):
    return string[0].lower() + string[1:]


# test
print(de_capitalize('Foobar'))