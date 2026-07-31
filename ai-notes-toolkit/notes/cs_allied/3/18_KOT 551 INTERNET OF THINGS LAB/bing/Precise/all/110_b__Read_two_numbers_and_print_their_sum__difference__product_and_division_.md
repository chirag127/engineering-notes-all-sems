# b) Read two numbers and print their sum, difference, product and division.

1. To read two numbers, we can use the `input()` function in Python. This function reads a line from input, converts it to a string, and returns it. We can then convert this string to an integer using the `int()` function.

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
```

2. To calculate the sum of the two numbers, we can use the `+` operator.

```python
sum = num1 + num2
print("The sum of the two numbers is:", sum)
```

3. To calculate the difference of the two numbers, we can use the `-` operator.

```python
difference = num1 - num2
print("The difference of the two numbers is:", difference)
```

4. To calculate the product of the two numbers, we can use the `*` operator.

```python
product = num1 * num2
print("The product of the two numbers is:", product)
```

5. To calculate the division of the two numbers, we can use the `/` operator.

```python
division = num1 / num2
print("The division of the two numbers is:", division)
```

6. The complete code to read two numbers and print their sum, difference, product and division is as follows:

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
print("The sum of the two numbers is:", sum)

difference = num1 - num2
print("The difference of the two numbers is:", difference)

product = num1 * num2
print("The product of the two numbers is:", product)

division = num1 / num2
print("The division of the two numbers is:", division)
```