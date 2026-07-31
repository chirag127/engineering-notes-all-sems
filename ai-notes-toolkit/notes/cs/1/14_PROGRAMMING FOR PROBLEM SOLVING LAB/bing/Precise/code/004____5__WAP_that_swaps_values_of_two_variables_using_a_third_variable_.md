## 5. WAP that swaps values of two variables using a third variable.

Here is an example of a program that swaps the values of two variables using a third variable:

```python
# initialize variables
x = 5
y = 10

# print initial values
print("Initial values:")
print(f"x = {x}")
print(f"y = {y}")

# swap values using a third variable
temp = x
x = y
y = temp

# print swapped values
print("Swapped values:")
print(f"x = {x}")
print(f"y = {y}")
```

This program initializes two variables, `x` and `y`, with the values `5` and `10`, respectively. It then uses a third variable, `temp`, to swap the values of `x` and `y`. The value of `x` is first assigned to `temp`, then the value of `y` is assigned to `x`, and finally the value of `temp` is assigned to `y`. This results in the values of `x` and `y` being swapped.

The program then prints the initial and swapped values of `x` and `y` to the console. The output of this program would be:

```
Initial values:
x = 5
y = 10
Swapped values:
x = 10
y = 5
```

This is one way to swap the values of two variables using a third variable. There are other ways to achieve the same result, such as using arithmetic operations or bitwise operations. However, using a third variable is a simple and straightforward method that is easy to understand and implement.