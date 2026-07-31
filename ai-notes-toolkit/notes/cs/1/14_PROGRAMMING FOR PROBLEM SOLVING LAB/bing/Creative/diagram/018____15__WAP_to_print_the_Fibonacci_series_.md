## 15. WAP to print the Fibonacci series.

The Fibonacci series is a sequence of numbers where each term is the sum of the previous two terms. The first two terms are 0 and 1. For example, the first 10 terms of the Fibonacci series are:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34

To write a program to print the Fibonacci series, we can use the following algorithm:

- Declare and initialize three variables: `a = 0`, `b = 1`, and `c = 0`.
- Declare and initialize a variable `n` to store the number of terms to be printed.
- Use a loop to repeat the following steps until `n` terms are printed:
  - Print the value of `a`.
  - Assign the value of `b` to `c`.
  - Assign the sum of `a` and `b` to `b`.
  - Assign the value of `c` to `a`.
  - Decrement `n` by 1.

Here is an example of the program in Python:

```python
# WAP to print the Fibonacci series

# Declare and initialize three variables
a = 0
b = 1
c = 0

# Declare and initialize a variable to store the number of terms
n = int(input("Enter the number of terms: "))

# Use a loop to print the Fibonacci series
while n > 0:
  # Print the value of a
  print(a, end=" ")
  # Update the values of a, b, and c
  c = b
  b = a + b
  a = c
  # Decrement n by 1
  n = n - 1
```

Output:

```
Enter the number of terms: 10
0 1 1 2 3 5 8 13 21 34
```