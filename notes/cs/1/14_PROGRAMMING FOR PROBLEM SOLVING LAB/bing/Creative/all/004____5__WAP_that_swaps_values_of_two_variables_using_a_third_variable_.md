## 5. WAP that swaps values of two variables using a third variable.

- A WAP (write a program) is a task that requires writing a computer code that performs a specific function or solves a problem.
- To swap values of two variables using a third variable means to exchange the data stored in the two variables by using another variable as a temporary storage.
- For example, if we have two variables `a` and `b` with values `10` and `20` respectively, we want to swap their values so that `a` becomes `20` and `b` becomes `10`.
- To do this, we can use a third variable `c` to store the value of `a` temporarily, then assign the value of `b` to `a`, and finally assign the value of `c` to `b`.
- The pseudocode for this algorithm is:

```
c = a
a = b
b = c
```

- The code can be written in different programming languages, such as Python, C, Java, etc. Here is an example of Python code that swaps values of two variables using a third variable:

```python
# declare and initialize two variables
a = 10
b = 20

# print the original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# use a third variable to swap the values
c = a # store the value of a in c
a = b # assign the value of b to a
b = c # assign the value of c to b

# print the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
```

- The output of this code is:

```
Before swapping:
a = 10
b = 20
After swapping:
a = 20
b = 10
```