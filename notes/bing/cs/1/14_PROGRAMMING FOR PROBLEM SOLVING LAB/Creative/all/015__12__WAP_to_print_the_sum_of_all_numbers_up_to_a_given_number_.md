## 12. WAP to print the sum of all numbers up to a given number.

- The problem statement is to write a program that takes a positive integer n as input and prints the sum of all numbers from 1 to n, inclusive.
- The sum of all numbers from 1 to n can be calculated using a simple formula: `n * (n + 1) / 2`.
- This formula can be derived by observing that the sum of the first and the last number is n + 1, the sum of the second and the second last number is also n + 1, and so on. There are n / 2 such pairs, so the total sum is n / 2 * (n + 1).
- A possible mnemonic to remember this formula is: **N**ice **P**eople **D**ivide **N**umbers **A**nd **A**dd **T**hem.
- Here is an example of a program in Python that implements this logic:

```python
# Take a positive integer n as input
n = int(input("Enter a positive integer: "))

# Calculate the sum using the formula
sum = n * (n + 1) // 2

# Print the sum
print("The sum of all numbers from 1 to", n, "is", sum)
```

- Here is a sample output of the program:

```
Enter a positive integer: 10
The sum of all numbers from 1 to 10 is 55
```

- Alternatively, the sum can also be calculated using a loop that adds each number from 1 to n. This approach is less efficient than the formula, but it can be useful to understand the logic behind the problem.
- Here is an example of a program in Python that uses a loop to calculate the sum:

```python
# Take a positive integer n as input
n = int(input("Enter a positive integer: "))

# Initialize the sum to zero
sum = 0

# Loop from 1 to n and add each number to the sum
for i in range(1, n + 1):
  sum = sum + i

# Print the sum
print("The sum of all numbers from 1 to", n, "is", sum)
```

- Here is a sample output of the program:

```
Enter a positive integer: 10
The sum of all numbers from 1 to 10 is 55
```