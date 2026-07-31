## 12. WAP to print the sum of all numbers up to a given number.

- A WAP (Write a Program) is a task that requires writing a computer program in a specific programming language to achieve a desired output or functionality.
- To print the sum of all numbers up to a given number, we need to follow these steps:
  - Declare a variable to store the given number and assign it a value.
  - Declare another variable to store the sum and initialize it to zero.
  - Use a loop to iterate from one to the given number, adding each number to the sum variable.
  - Print the sum variable after the loop ends.
- Here is an example of a WAP to print the sum of all numbers up to a given number in Python:

```python
# Declare a variable to store the given number and assign it a value
n = 10

# Declare another variable to store the sum and initialize it to zero
sum = 0

# Use a loop to iterate from one to the given number, adding each number to the sum variable
for i in range(1, n + 1):
  sum = sum + i

# Print the sum variable after the loop ends
print(sum)
```

- The output of this program is:

```python
55
```

- This is because the sum of all numbers from 1 to 10 is 55, which is calculated by the formula:

```python
sum = n * (n + 1) / 2
```

- where n is the given number.