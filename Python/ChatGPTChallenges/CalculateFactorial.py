"""
Write a Python program that asks the user to enter a non-negative integer (n) and 
calculates the factorial of that number. The factorial of a non-negative integer n, 
denoted as n!, is the product of all positive integers less than or equal to n.

For example, the factorial of 5 (denoted as 5!) is calculated as:

5! = 5 x 4 x 3 x 2 x 1 = 120

Your program should:

1. Prompt the user to enter a non-negative integer.
2. Check if the input is a non-negative integer.
3. alculate and print the factorial of that number.
4. Handle the case when the user enters a negative number gracefully.
"""

def factorial(n):
        result = 1
        if n < 0:
            return "Please choose a positive number"
        
        if n == 0:
            return result
        
        for i in range(1, n+1, 1):
            result *= i
        
        return result

while True:
    userInput = int(input("Please write a positive number to calculate the factorial of the number: "))
    print(factorial(userInput))