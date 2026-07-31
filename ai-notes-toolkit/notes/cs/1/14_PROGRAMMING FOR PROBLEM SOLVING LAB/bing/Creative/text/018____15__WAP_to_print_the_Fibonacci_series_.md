## 15. WAP to print the Fibonacci series.

- The Fibonacci series is a sequence of numbers where each term is the sum of the previous two terms.
- The first two terms of the Fibonacci series are 1 and 1.
- The general formula for the nth term of the Fibonacci series is:

  - F(n) = F(n-1) + F(n-2), for n > 2

- To write a program to print the Fibonacci series, we need to:

  - Declare a variable n to store the number of terms to be printed.
  - Declare three variables a, b and c to store the current, previous and next term of the series respectively.
  - Initialize a and b to 1, and c to 0.
  - Use a loop to iterate from 1 to n, and perform the following steps in each iteration:
    - Print the value of a.
    - Assign the value of b to c.
    - Assign the value of a to b.
    - Assign the value of c + b to a.
  - End the loop.

- Here is an example of a program to print the Fibonacci series in Python:

```python
# Program to print the Fibonacci series

# Input the number of terms
n = int(input("Enter the number of terms: "))

# Initialize the variables
a = 1 # Current term
b = 1 # Previous term
c = 0 # Next term

# Loop from 1 to n
for i in range(1, n+1):
  # Print the current term
  print(a, end=" ")
  # Update the variables
  c = b
  b = a
  a = c + b

# Print a new line
print()
```

- Here is an example of the output of the program for n = 10:

```text
Enter the number of terms: 10
1 1 2 3 5 8 13 21 34 55
```