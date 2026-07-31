Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write a program that swaps values of two variables using a third variable. Here is the content in markdown format:

## 5. WAP that swaps values of two variables using a third variable.

- Swapping values of two variables means exchanging their values, so that the variable that had the first value now has the second value, and vice versa.
- To swap values of two variables using a third variable, we need to follow these steps:
  - Declare and initialize three variables, such as `a`, `b`, and `temp`.
  - Assign the value of `a` to `temp`, so that `temp` now holds the first value.
  - Assign the value of `b` to `a`, so that `a` now holds the second value.
  - Assign the value of `temp` to `b`, so that `b` now holds the first value.
  - Print the values of `a` and `b` after swapping.
- Here is an example of a program that swaps values of two variables using a third variable in Python:

```python
# Declare and initialize three variables
a = 10
b = 20
temp = 0

# Print the values of a and b before swapping
print("Before swapping, a =", a, "and b =", b)

# Swap the values of a and b using temp
temp = a # temp now holds the first value
a = b # a now holds the second value
b = temp # b now holds the first value

# Print the values of a and b after swapping
print("After swapping, a =", a, "and b =", b)
```

- The output of the program is:

```
Before swapping, a = 10 and b = 20
After swapping, a = 20 and b = 10
```

- This program can swap values of any data type, such as integers, floats, strings, etc. as long as they are compatible with the assignment operator.