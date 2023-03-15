## 5. WAP that swaps values of two variables using a third variable.

- A WAP (write a program) is a task that requires writing code in a specific programming language to achieve a desired output or functionality.
- Swapping values of two variables means exchanging the data stored in the memory locations associated with the variables.
- Using a third variable means creating a temporary variable that can hold the value of one of the original variables during the swapping process.
- The general algorithm for swapping values of two variables using a third variable is:

  - Declare and initialize three variables: `a`, `b`, and `temp`.
  - Assign the value of `a` to `temp`.
  - Assign the value of `b` to `a`.
  - Assign the value of `temp` to `b`.
  - Print the values of `a` and `b` after swapping.

- The following is an example of a WAP that swaps values of two variables using a third variable in Python:

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

- The same WAP can be written in different programming languages, such as C, Java, or Ruby, with minor syntactical differences.