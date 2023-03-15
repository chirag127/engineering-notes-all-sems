## 5. WAP that swaps values of two variables using a third variable.

Here is a program that swaps the values of two variables using a third variable:

```python
# initialize variables
x = 5
y = 10

# print initial values
print("Initial values:")
print("x =", x)
print("y =", y)

# swap values using a third variable
temp = x
x = y
y = temp

# print swapped values
print("Swapped values:")
print("x =", x)
print("y =", y)
```

This program first initializes the values of `x` and `y` to `5` and `10`, respectively. Then, it prints their initial values. Next, it uses a third variable `temp` to swap the values of `x` and `y`. Finally, it prints the swapped values of `x` and `y`.

The output of this program is:

```
Initial values:
x = 5
y = 10
Swapped values:
x = 10
y = 5
```

This program can be easily modified to swap the values of any two variables. The key idea is to use a third variable to temporarily store the value of one of the variables, so that its value can be replaced by the value of the other variable. Then, the value of the other variable can be replaced by the value stored in the third variable, effectively swapping the values of the two variables.