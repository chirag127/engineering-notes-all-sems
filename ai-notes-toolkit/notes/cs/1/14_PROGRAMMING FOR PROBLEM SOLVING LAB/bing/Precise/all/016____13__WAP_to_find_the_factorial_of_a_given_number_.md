## 13. WAP to find the factorial of a given number.

Factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, the factorial of 5 is 120, or 5! = 5 × 4 × 3 × 2 × 1 = 120.

Here is an example of a program that calculates the factorial of a given number:

```python
n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(f"The factorial of {n} is {factorial}")
```

This program prompts the user to enter a number, then checks if the number is negative, zero, or positive. If the number is negative, the program prints an error message. If the number is zero, the program prints that the factorial of 0 is 1. If the number is positive, the program calculates the factorial by multiplying all the numbers from 1 to the entered number, then prints the result.