# Source
# https://medium.com/better-programming/25-useful-python-snippets-to-help-in-your-day-to-day-work-d59c636ec1b
# check if a string is palindrome

# logic
def check_string_palindrome(string):
    return string == string[::-1]

# test
print(check_string_palindrome('kayak'))

