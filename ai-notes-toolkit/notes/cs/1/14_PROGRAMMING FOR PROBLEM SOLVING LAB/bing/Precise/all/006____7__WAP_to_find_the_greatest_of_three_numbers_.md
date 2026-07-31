## 7. WAP to find the greatest of three numbers.

To find the greatest of three numbers, we can use the following algorithm:

1. Take three numbers as input from the user.
2. Compare the first two numbers and store the greater number in a variable.
3. Compare the third number with the variable and update the variable if the third number is greater.
4. The variable now contains the greatest of the three numbers.

Here is an example of a program in Python that implements this algorithm:

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

This program takes three numbers as input from the user and compares them to find the greatest number. The result is then printed to the screen. This program can be easily modified to find the greatest of any number of numbers.