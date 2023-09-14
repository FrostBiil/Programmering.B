# 1
# Create a function website() that grabs the website domain from a url string. For example, if your function is passed "www.google.com", it should return "google".
"""def website(url):    
    pass  # Remove this line and add your answer here. """
url = "www.google.com"
def website(url):
    return url.split(".")[1]
print(website(url))

# 2
# Create a function divisible(a, b) that accepts two integers (a and b) and returns True if a is divisble by b without a remainder. For example, divisible(10, 3) should return False, while divisible(6, 3) should return True.
"""def divisible(a, b):
    pass  # Remove this line and add your answer here."""

def divisible(a, b):
    return a % b == 0
print(divisible(10, 3))

# 3
# Use list comprehension to square every number in the following list of numbers.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def square_numbers(l):
    return [num**2 for num in l]
print(square_numbers(l))

# 4
# For the following list of names, write a list comprehension that creates a list of only words that start with a capital letter (hint: str.isupper()).
names = ['Steve Irwin', 'koala', 'kangaroo', 'Australia', 'Sydney', 'desert']

def cap_names(names):
    return [name for name in names if name[0].isupper()]
print(cap_names(names))

# 5
# For the following list of keys and vals use dictionary comprehension to create a dictionary of the form {'key-0': 0, 'key-1': 1, etc} (hint: zip() can help you combine two lists into on object to be used for comprehension/looping).
keys = [f"key-{k}" for k in range(10)]
vals = range(10)

def key_vals(keys, vals):
    return {key: val for key, val in zip(keys, vals)}
print(key_vals(keys, vals))

# 6
# This question is a little harder. Create a generator function called listgen(n) that yields numbers from 0 to n, in batches of lists of maximum 10 numbers at a time. For example, your function should behave as follows:
"""g = listgen(100)
next(g)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
next(g)
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
next(g)
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
etc.

g = listgen(5)
next(g)"""

def listgen(n):
    for i in range(0, n, 10):
        yield list(range(i, i+10))
g = listgen(100)
print(next(g))
print(next(g))
print(next(g))
g = listgen(5)
print(next(g))

# 7
# Write a try/except to catch the error generated from the following code and print “I caught you!”. Make sure you catch the specific error being caused, this is typically better practice than just catching all errors!
try:
    5 / 0
except ZeroDivisionError:
    print("I caught you!")

# 8
# Create a function lucky_sum() that takes all the integers a user enters and returns their sum. However, if one of the values is 13 then it does not count towards the sum, nor do any values to its right.

"""For example, your function should behave as follows:

lucky_sum(1, 2, 3, 4)
10

lucky_sum(1, 13, 3, 4)
1

lucky_sum(13)
0"""

def lucky_sum(*args):
    sum = 0
    for num in args:
        if num == 13:
            break
        sum += num
    return sum
print(lucky_sum(1, 2, 3, 4))
print(lucky_sum(1, 13, 3, 4))
print(lucky_sum(13))