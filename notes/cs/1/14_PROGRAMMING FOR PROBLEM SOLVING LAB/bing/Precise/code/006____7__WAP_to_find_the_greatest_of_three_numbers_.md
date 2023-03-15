## 7. WAP to find the greatest of three numbers.

To find the greatest of three numbers, you can use the following algorithm:

1. Take three numbers as input from the user.
2. Compare the first two numbers and store the greater number in a variable.
3. Compare the third number with the variable containing the greater number.
4. The greater number among the three numbers is the result.

Here is an example of a program in Python that implements this algorithm:

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    greater = num1
else:
    greater = num2

if num3 > greater:
    greater = num3

print("The greatest number is:", greater)
```

This program takes three numbers as input from the user and compares them to find the greatest number. The result is then printed to the screen. You can modify this program to suit your needs.