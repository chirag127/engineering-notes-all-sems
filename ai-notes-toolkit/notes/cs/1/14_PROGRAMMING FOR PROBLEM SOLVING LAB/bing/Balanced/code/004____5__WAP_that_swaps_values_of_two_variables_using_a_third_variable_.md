## 5. WAP that swaps values of two variables using a third variable.

- A WAP (Write a Program) is a task that requires writing a computer program in a specific programming language to achieve a desired output or functionality.
- Swapping values of two variables means exchanging the data stored in the variables, so that the variable that had the first value now has the second value, and vice versa.
- Using a third variable means creating a temporary variable that can store one of the values during the swapping process, so that the original value is not lost or overwritten.
- Here is an example of a WAP that swaps values of two variables using a third variable in Python:

```python
# Declare and initialize two variables with some values
x = 10
y = 20

# Print the original values of x and y
print("Before swapping:")
print("x =", x)
print("y =", y)

# Create a third variable and assign it the value of x
temp = x

# Assign the value of y to x
x = y

# Assign the value of temp (which is the original value of x) to y
y = temp

# Print the swapped values of x and y
print("After swapping:")
print("x =", x)
print("y =", y)
```

- The output of this program is:

```
Before swapping:
x = 10
y = 20
After swapping:
x = 20
y = 10
```