## 15. WAP to print the Fibonacci series.

- The Fibonacci series is a sequence of numbers where each term is the sum of the previous two terms.
- The first two terms of the Fibonacci series are 1 and 1.
- The general formula for the nth term of the Fibonacci series is:

```
F(n) = F(n-1) + F(n-2)
```

- To write a program to print the Fibonacci series, we need to:

  - Declare a variable to store the number of terms to be printed.
  - Declare three variables to store the current term, the previous term, and the next term of the series.
  - Initialize the first two terms as 1 and 1.
  - Use a loop to iterate from 1 to the number of terms.
  - Print the current term in each iteration.
  - Update the next term as the sum of the current term and the previous term.
  - Update the previous term as the current term.
  - Update the current term as the next term.

- Here is an example of a program to print the Fibonacci series in Python:

```python
# Declare a variable to store the number of terms
n = int(input("Enter the number of terms: "))

# Declare three variables to store the current, previous, and next term
current = 1
previous = 1
next = 0

# Use a loop to iterate from 1 to n
for i in range(1, n+1):
  # Print the current term
  print(current, end=" ")
  # Update the next term as the sum of the current and previous term
  next = current + previous
  # Update the previous term as the current term
  previous = current
  # Update the current term as the next term
  current = next
```

- The output of the program for n = 10 is:

```
1 1 2 3 5 8 13 21 34 55
```