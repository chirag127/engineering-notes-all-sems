## 7. WAP to find the greatest of three numbers.

To find the greatest of three numbers, you can use the following algorithm:

1. Take three numbers as input from the user.
2. Compare the first two numbers and store the larger of the two in a variable.
3. Compare the third number with the value stored in the variable.
4. The larger of the two is the greatest of the three numbers.

Here is an example of how this can be implemented in Python:

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    greatest = num1
else:
    greatest = num2

if num3 > greatest:
    greatest = num3

print("The greatest of the three numbers is:", greatest)
```

This program takes three numbers as input from the user and compares them to find the greatest of the three. The result is then printed to the screen. You can modify this program to suit your needs.