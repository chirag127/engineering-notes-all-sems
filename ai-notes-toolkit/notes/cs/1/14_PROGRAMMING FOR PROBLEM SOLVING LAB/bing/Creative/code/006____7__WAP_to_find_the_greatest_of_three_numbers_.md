## 7. WAP to find the greatest of three numbers.

- A program to find the greatest of three numbers is a common problem that can be solved using conditional statements.
- The program can take three numbers as input from the user and compare them using the `>` operator.
- The program can print the largest number as the output or display a message if all the numbers are equal.
- Here is an example of such a program in Python:

```python
# Take three numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers using the > operator
if num1 > num2 and num1 > num3:
    # Print num1 as the largest number
    print(num1, "is the greatest of the three numbers.")
elif num2 > num1 and num2 > num3:
    # Print num2 as the largest number
    print(num2, "is the greatest of the three numbers.")
elif num3 > num1 and num3 > num2:
    # Print num3 as the largest number
    print(num3, "is the greatest of the three numbers.")
else:
    # Print a message if all the numbers are equal
    print("All the numbers are equal.")
```