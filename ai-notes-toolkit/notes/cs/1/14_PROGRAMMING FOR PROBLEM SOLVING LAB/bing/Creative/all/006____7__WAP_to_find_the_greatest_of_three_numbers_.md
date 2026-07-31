## 7. WAP to find the greatest of three numbers.

- A program to find the greatest of three numbers is a common problem in programming that can be solved using conditional statements.
- The basic idea is to compare the three numbers and find the one that is larger than the other two.
- There are different ways to write a program to find the greatest of three numbers, depending on the programming language and the logic used.
- Here is one possible way to write a program to find the greatest of three numbers in Python:

```python
# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers and find the greatest one
if num1 > num2 and num1 > num3:
    # If num1 is greater than both num2 and num3, then num1 is the greatest
    print(num1, "is the greatest number.")
elif num2 > num1 and num2 > num3:
    # If num2 is greater than both num1 and num3, then num2 is the greatest
    print(num2, "is the greatest number.")
else:
    # If none of the above conditions are true, then num3 is the greatest
    print(num3, "is the greatest number.")
```

- The program takes three numbers as input from the user and stores them in variables num1, num2, and num3.
- The program then uses if-elif-else statements to compare the numbers and find the greatest one.
- The program prints the greatest number as the output.