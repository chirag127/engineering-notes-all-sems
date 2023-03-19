## 5. WAP that swaps values of two variables using a third variable.

In computer programming, it is often necessary to swap the values of two variables. This can be done using a temporary or third variable to store the value of one variable while the other variable's value is assigned to it. Here are the steps to write a program in Python that swaps the values of two variables using a third variable:

1. Declare three variables, let's say `a`, `b`, and `temp`.
2. Assign values to `a` and `b`.
3. Print the original values of `a` and `b` for reference.
4. Assign the value of `a` to `temp`.
5. Assign the value of `b` to `a`.
6. Assign the value of `temp` to `b`.
7. Print the new values of `a` and `b`.

Here's the Python code:

```python
a = 10
b = 20

print("Original values:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("Swapped values:")
print("a =", a)
print("b =", b)
```

Output:
```
Original values:
a = 10
b = 20
Swapped values:
a = 20
b = 10
```

Note:
- The temporary variable `temp` is used to store the value of `a` before it is overwritten by the value of `b`.
- After `temp` is assigned to `b`, the values of `a` and `b` have been swapped.

In summary, swapping the values of two variables using a third variable is a simple and effective way to exchange the values of two variables. By using a temporary variable, we can easily swap the values without losing any data.