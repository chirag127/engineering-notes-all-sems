## 12. WAP to print the sum of all numbers up to a given number.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- To print the sum of all numbers up to a given number, we need to use a loop that iterates from 1 to the given number and adds each number to a variable that stores the sum.
- We also need to use an input function that takes the given number from the user and converts it to an integer.
- We can use any programming language to write the program, but for this example, we will use Python.
- The program can be written as follows:

```python
# Take the given number from the user and convert it to an integer
n = int(input("Enter a positive integer: "))

# Initialize a variable to store the sum
sum = 0

# Use a loop to iterate from 1 to n and add each number to the sum
for i in range(1, n + 1):
  sum = sum + i

# Print the sum
print("The sum of all numbers up to", n, "is", sum)
```

- The output of the program will depend on the input given by the user. For example, if the user enters 10, the output will be:

```
Enter a positive integer: 10
The sum of all numbers up to 10 is 55
```

- This program can be modified to use different input and output functions, or different looping constructs, depending on the programming language and the requirements of the task.