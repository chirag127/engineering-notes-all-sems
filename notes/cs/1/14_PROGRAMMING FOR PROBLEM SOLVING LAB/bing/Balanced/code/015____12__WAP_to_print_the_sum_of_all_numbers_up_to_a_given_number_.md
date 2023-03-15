## 12. WAP to print the sum of all numbers up to a given number.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- To print the sum of all numbers up to a given number, we need to use a loop that iterates from 1 to the given number and adds each number to a variable that stores the sum.
- We also need to use a variable that stores the given number, which can be input by the user or assigned by the program.
- We can use any programming language to write the program, but for this example, we will use Python, which is a popular and easy-to-learn language.
- The program can be written as follows:

```python
# Python program to print the sum of all numbers up to a given number

# Input the given number
n = int(input("Enter a positive integer: "))

# Initialize the sum variable to zero
sum = 0

# Loop from 1 to n
for i in range(1, n + 1):
  # Add i to the sum
  sum = sum + i

# Print the sum
print("The sum of all numbers up to", n, "is", sum)
```

- The output of the program will depend on the input given by the user. For example, if the user enters 10, the output will be:

```
Enter a positive integer: 10
The sum of all numbers up to 10 is 55
```

- The program can be modified to use different loops, such as while or do-while, or different languages, such as C, Java, or Ruby, but the logic will remain the same.