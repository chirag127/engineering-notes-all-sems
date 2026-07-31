## 7. WAP to find the greatest of three numbers.

- A program to find the greatest of three numbers is a common problem in programming that can be solved using various methods such as conditional statements, logical operators, or functions.
- One possible method is to use the `if-else` statement to compare the three numbers and print the largest one. For example, in Python, the program can be written as:

```python
# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers and print the largest one
if num1 > num2 and num1 > num3:
    print(num1, "is the greatest number.")
elif num2 > num1 and num2 > num3:
    print(num2, "is the greatest number.")
else:
    print(num3, "is the greatest number.")
```

- Another possible method is to use the `max()` function to find the maximum value among the three numbers and print it. For example, in Python, the program can be written as:

```python
# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum value using the max() function and print it
max_num = max(num1, num2, num3)
print(max_num, "is the greatest number.")
```

- These are some of the ways to write a program to find the greatest of three numbers. The output of the program will depend on the input values given by the user. For example, if the user enters 10, 20, and 30, the output will be 30 is the greatest number.