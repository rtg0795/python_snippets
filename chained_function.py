# Source
# https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
# Chained Function call



# logic
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

# test
a, b = 4, 5
print((substract if a > b else add)(a, b))
