# Read two numbers and print their sum, difference, product, and division

When programming, it is essential to be able to perform basic arithmetic operations on numerical values. One of the most common tasks is to read two numbers from the user and then perform various calculations on them. In this guide, we will learn how to read two numbers from the user and then print their sum, difference, product, and division.

## Reading Input from the User

Before we can perform any calculations, we need to read two numbers from the user. In most programming languages, we can use a built-in function or method to read input from the user. For example, in Python, we can use the `input()` function to read a string of characters from the user. We can then convert this string to a numerical value using the `int()` or `float()` function.

Here's an example of how we can read two numbers from the user in Python:

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
```

In this example, we use the `input()` function to read two strings from the user. We then use the `float()` function to convert these strings to floating-point values (i.e., decimal numbers).

## Performing Arithmetic Operations

Once we have read the two numbers from the user, we can perform various arithmetic operations on them. Here are some examples:

### Sum

To calculate the sum of two numbers, we simply add them together:

```python
sum = num1 + num2
print("The sum is:", sum)
```

### Difference

To calculate the difference between two numbers, we subtract the second number from the first:

```python
diff = num1 - num2
print("The difference is:", diff)
```

### Product

To calculate the product of two numbers, we multiply them together:

```python
prod = num1 * num2
print("The product is:", prod)
```

### Division

To calculate the division of two numbers, we divide the first number by the second:

```python
div = num1 / num2
print("The division is:", div)
```

## Putting It All Together

Here's the complete Python code that reads two numbers from the user and then prints their sum, difference, product, and division:

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2

print("The sum is:", sum)
print("The difference is:", diff)
print("The product is:", prod)
print("The division is:", div)
```

## Conclusion

In this guide, we have learned how to read two numbers from the user and then perform various arithmetic operations on them. By following these steps, you can add basic arithmetic functionality to your programs and perform calculations on numerical data.