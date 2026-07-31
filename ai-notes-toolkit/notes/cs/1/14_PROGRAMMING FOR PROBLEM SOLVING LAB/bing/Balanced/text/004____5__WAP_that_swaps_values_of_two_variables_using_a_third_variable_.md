## 5. WAP that swaps values of two variables using a third variable.

- A WAP (write a program) is a task that requires writing code in a specific programming language to achieve a desired output or functionality.
- Swapping values of two variables means exchanging the data stored in the memory locations associated with the variable names.
- Using a third variable means creating a temporary variable that can hold the value of one of the original variables during the swapping process.
- The general algorithm for swapping values of two variables using a third variable is:

  - Declare and initialize two variables with some values, for example `a = 10` and `b = 20`.
  - Declare a third variable, for example `temp`.
  - Assign the value of `a` to `temp`, i.e. `temp = a`.
  - Assign the value of `b` to `a`, i.e. `a = b`.
  - Assign the value of `temp` to `b`, i.e. `b = temp`.
  - Print the values of `a` and `b` after swapping, i.e. `a = 20` and `b = 10`.

- The following is an example of a WAP that swaps values of two variables using a third variable in Python:

```python
# WAP that swaps values of two variables using a third variable

# Declare and initialize two variables
a = 10
b = 20

# Print the values of a and b before swapping
print("Before swapping:")
print("a =", a)
print("b =", b)

# Declare a third variable
temp = 0

# Swap the values of a and b using temp
temp = a # temp holds the value of a
a = b # a gets the value of b
b = temp # b gets the value of temp

# Print the values of a and b after swapping
print("After swapping:")
print("a =", a)
print("b =", b)
```

- The output of the above program is:

```
Before swapping:
a = 10
b = 20
After swapping:
a = 20
b = 10
```