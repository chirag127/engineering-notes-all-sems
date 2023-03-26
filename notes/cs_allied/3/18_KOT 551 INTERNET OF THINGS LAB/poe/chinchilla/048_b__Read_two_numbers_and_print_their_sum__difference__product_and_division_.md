## Read two numbers and print their sum, difference, product and division.

When working with programming, it's important to know how to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. In this topic, we'll learn how to read two numbers from the user and print their sum, difference, product, and division using Python.

Here are the steps to perform this task:

1. Ask the user to enter the first number.
```python
num1 = float(input("Enter the first number: "))
```
In this step, we use the `input()` function to prompt the user to enter the first number. The `float()` function is used to convert the input string to a float value.

2. Ask the user to enter the second number.
```python
num2 = float(input("Enter the second number: "))
```
Similarly, we ask the user to enter the second number and convert it to a float value.

3. Calculate the sum of the two numbers.
```python
sum = num1 + num2
```
We add the two numbers and store the result in a variable called `sum`.

4. Calculate the difference between the two numbers.
```python
diff = num1 - num2
```
We subtract the second number from the first number and store the result in a variable called `diff`.

5. Calculate the product of the two numbers.
```python
prod = num1 * num2
```
We multiply the two numbers and store the result in a variable called `prod`.

6. Calculate the division of the two numbers.
```python
div = num1 / num2
```
We divide the first number by the second number and store the result in a variable called `div`.

7. Print the results.
```python
print("Sum:", sum)
print("Difference:", diff)
print("Product:", prod)
print("Division:", div)
```
Finally, we use the `print()` function to display the results to the user.

Here's the complete code:

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2

print("Sum:", sum)
print("Difference:", diff)
print("Product:", prod)
print("Division:", div)
```

With these simple steps, you can read two numbers from the user and perform basic arithmetic operations on them using Python.