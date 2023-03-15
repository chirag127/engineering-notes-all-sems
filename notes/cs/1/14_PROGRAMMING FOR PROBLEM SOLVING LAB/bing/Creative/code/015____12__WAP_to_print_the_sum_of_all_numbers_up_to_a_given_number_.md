Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics.

Here is the content you requested:

## 12. WAP to print the sum of all numbers up to a given number.

- The problem statement is to write a program that takes a positive integer n as input and prints the sum of all natural numbers from 1 to n.
- One possible solution is to use a loop that iterates from 1 to n and adds each number to a variable that stores the sum.
- Another possible solution is to use a mathematical formula that calculates the sum of the first n natural numbers as n*(n+1)/2.
- Here is an example of the first solution in Python:

```python
# Input a positive integer n
n = int(input("Enter a positive integer: "))

# Initialize a variable to store the sum
sum = 0

# Loop from 1 to n and add each number to the sum
for i in range(1, n+1):
  sum = sum + i

# Print the sum
print("The sum of all numbers up to", n, "is", sum)
```

- Here is an example of the second solution in Python:

```python
# Input a positive integer n
n = int(input("Enter a positive integer: "))

# Calculate the sum using the formula
sum = n*(n+1)//2

# Print the sum
print("The sum of all numbers up to", n, "is", sum)
```

- Both solutions have the same output for any valid input. For example, if n is 10, the output is:

```
The sum of all numbers up to 10 is 55
```