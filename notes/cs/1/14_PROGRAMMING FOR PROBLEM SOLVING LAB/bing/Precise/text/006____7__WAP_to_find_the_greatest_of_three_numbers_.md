## 7. WAP to find the greatest of three numbers.

To find the greatest of three numbers, we can use the `if-else` statement in programming. Here is an example of how to do this in Python:

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
```

In this example, we take three numbers as input from the user and store them in the variables `num1`, `num2`, and `num3`. Then, we use the `if-else` statement to compare the three numbers and find the largest among them. The largest number is then stored in the variable `largest` and printed to the screen.