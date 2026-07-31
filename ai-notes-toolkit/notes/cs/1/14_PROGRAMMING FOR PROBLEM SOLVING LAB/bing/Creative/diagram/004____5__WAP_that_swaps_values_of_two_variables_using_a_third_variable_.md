Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that swaps values of two variables using a third variable. Here is the content in markdown format:

## 5. WAP that swaps values of two variables using a third variable.

- Swapping values of two variables means exchanging their values, so that the first variable holds the value of the second variable and vice versa.
- To swap values of two variables using a third variable, we need to follow these steps:
  - Declare and initialize three variables, say `a`, `b`, and `temp`. Assign some values to `a` and `b`, and leave `temp` empty.
  - Store the value of `a` in `temp`. This way, we have a copy of `a`'s value in `temp`.
  - Assign the value of `b` to `a`. This way, `a` now holds the value of `b`.
  - Assign the value of `temp` to `b`. This way, `b` now holds the value of `a` that was stored in `temp`.
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

# Store the value of a in temp
temp = a

# Assign the value of b to a
a = b

# Assign the value of temp to b
b = temp

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

- This is how we can swap values of two variables using a third variable.