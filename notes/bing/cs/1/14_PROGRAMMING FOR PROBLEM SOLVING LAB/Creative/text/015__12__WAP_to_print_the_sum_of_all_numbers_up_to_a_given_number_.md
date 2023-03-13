## 12. WAP to print the sum of all numbers up to a given number.

- The problem statement is to write a program that takes a positive integer n as input and prints the sum of all natural numbers from 1 to n.
- One possible solution is to use a loop that iterates from 1 to n and adds each number to a variable that stores the sum.
- Another possible solution is to use the formula for the sum of an arithmetic series, which is n(n+1)/2, and print the result.
- Here is an example of the first solution in Python:

```python
# Take input from the user
n = int(input("Enter a positive integer: "))

# Initialize sum to zero
sum = 0

# Loop from 1 to n
for i in range(1, n+1):
  # Add i to sum
  sum = sum + i

# Print the sum
print("The sum of all numbers up to", n, "is", sum)
```

- Here is an example of the second solution in Python:

```python
# Take input from the user
n = int(input("Enter a positive integer: "))

# Use the formula for the sum of an arithmetic series
sum = n * (n + 1) // 2

# Print the sum
print("The sum of all numbers up to", n, "is", sum)
```

- Both solutions have the same output, but the second one is more efficient as it does not use a loop. However, the first one is more intuitive and easier to understand.