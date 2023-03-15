## 13. WAP to find the factorial of a given number.

Factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, the factorial of 5 is 120, or 5! = 5 x 4 x 3 x 2 x 1 = 120.

Here is an example of a program that calculates the factorial of a given number:

```python
n = int(input('Enter a number: '))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f'The factorial of {n} is {factorial}')
```

This program prompts the user to enter a number, then calculates the factorial of that number using a for loop. The loop iterates from 1 to n, multiplying the value of the factorial variable by the current value of i at each iteration. Finally, the program prints the result.