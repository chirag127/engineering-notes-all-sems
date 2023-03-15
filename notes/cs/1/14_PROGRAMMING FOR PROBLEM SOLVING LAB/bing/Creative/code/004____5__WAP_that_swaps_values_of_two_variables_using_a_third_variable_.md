Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that swaps values of two variables using a third variable. Here is the content in markdown format:

## 5. WAP that swaps values of two variables using a third variable.

- Swapping values of two variables means exchanging their values, so that the first variable holds the value of the second variable, and vice versa.
- To swap values of two variables using a third variable, we need to follow these steps:
  - Declare and initialize three variables: `a`, `b`, and `temp`. Assign some values to `a` and `b`, and leave `temp` empty.
  - Assign the value of `a` to `temp`, so that `temp` holds the same value as `a`.
  - Assign the value of `b` to `a`, so that `a` holds the same value as `b`.
  - Assign the value of `temp` to `b`, so that `b` holds the same value as `temp`, which is the original value of `a`.
  - Print the values of `a` and `b` after swapping.
- Here is an example of a program that swaps values of two variables using a third variable in Python:

```python
# Declare and initialize three variables
a = 10
b = 20
temp = 0

# Print the values of a and b before swapping
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap the values of a and b using temp
temp = a # temp holds the value of a
a = b # a holds the value of b
b = temp # b holds the value of temp, which is the original value of a

# Print the values of a and b after swapping
print("After swapping:")
print("a =", a)
print("b =", b)
```

- The output of the program is:

```
Before swapping:
a = 10
b = 20
After swapping:
a = 20
b = 10
```

- This program can be written in other programming languages as well, with some minor changes in syntax and style. The logic of swapping values of two variables using a third variable remains the same.