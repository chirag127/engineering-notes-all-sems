## 15. WAP to print the Fibonacci series.

- The Fibonacci series is a sequence of numbers where each term is the sum of the previous two terms. The first two terms are 0 and 1. For example, the first 10 terms of the Fibonacci series are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
- To write a program to print the Fibonacci series, we need to use a loop that iterates over a certain number of terms and calculates the next term by adding the previous two terms. We also need to store the previous two terms in variables and update them in each iteration.
- Here is a possible pseudocode for the program:

```
# Initialize the first two terms
a = 0
b = 1

# Ask the user for the number of terms to print
n = input("Enter the number of terms: ")

# Print the first term
print(a)

# Loop from 1 to n-1
for i = 1 to n-1
  # Calculate the next term by adding the previous two terms
  c = a + b
  # Print the next term
  print(c)
  # Update the previous two terms
  a = b
  b = c
# End of loop
```

- Here is a possible Python code for the program:

```python
# Initialize the first two terms
a = 0
b = 1

# Ask the user for the number of terms to print
n = int(input("Enter the number of terms: "))

# Print the first term
print(a)

# Loop from 1 to n-1
for i in range(1, n):
  # Calculate the next term by adding the previous two terms
  c = a + b
  # Print the next term
  print(c)
  # Update the previous two terms
  a = b
  b = c
# End of loop
```

- Here is a possible output for the program:

```
Enter the number of terms: 10
0
1
1
2
3
5
8
13
21
34
```