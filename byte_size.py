# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# Get length of string in bytes

# logic
def byte_size(string):
    return len(string.encode('utf-8'))

# test
print(byte_size(':-()'))
print(byte_size('Hello World!'))