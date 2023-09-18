# 1
# What is 5 to the power of 5?
x = 5 ** 5 # 5^5
print(x) # 3125

# 2
# What is the remainder from dividing 73 by 6?
x = 73 % 6 # 73/6
print(x) # 1

# 3
# How many times does the whole number 3 go into 123? What is the remainder of dividing 123 by 3?
x = 123 // 3 # 123/3
print(x) # 41

# 4
# Split the following string into a list by splitting on the space character:
s = "MDS is going virtual!"
x = s.split(" ")
print(x) # ['MDS', 'is', 'going', 'virtual!']

# 5
# Given the following variables:
thing = "light"
speed = 299792458  # m/s
# Use f-strings to print:
    # The speed of light is 299792458 m/s.
print(f"The speed of {thing} is {speed} m/s.") # The speed of light is 299792458 m/s.

# 6
# Given this nested list, use indexing to grab the word “MDS”:
l = [10, [3, 4], [5, [100, 200, ["MDS"]], 23, 11], 1, 7]
print(l[2][1][2][0]) # MDS

# 7
# Given this nest dictionary grab the word “MDS”:
d = {
    "outer": [
        1,
        2,
        3,
        {"inner": ["this", "is", "inception", {"inner_inner": [1, 2, 3, "MDS"]}]},
    ]
}
print(d["outer"][3]["inner"][3]["inner_inner"][3]) # MDS

# 8
# Why does the following cell return an error?
t = (1, 2, 3, 4, 5)
t[-1] = 6
# Because tuples are immutable

# 9
# Use string methods to extract the website domain from an email, e.g., from the string "tomas.beuzen@fakemail.com", you should extract "fakemail".
email = "tomas.beuzen@fakemail.com"
x = email.split("@")[1].split(".")[0]
print(x) # fakemail

# 10
# Given the variable language which contains a string, use if/elif/else to write a program that:
    # return “I love snakes!” if language is "python" (any kind of capitalization)

    # return “Are you a pirate?” if language is "R" (any kind of capitalization)

    # else return “What is language?” if language is anything else.

language = "Python"
if language.lower() == "python":
    print("I love snakes!")
elif language.lower() == "r":
    print("Are you a pirate?")
else:
    print("What is language?")
# Output: I love snakes!
