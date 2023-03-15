Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to print the sum of all numbers up to a given number. Here is the content in markdown format:

## 12. WAP to print the sum of all numbers up to a given number.

- The problem statement is to write a program that takes a positive integer n as input and prints the sum of all natural numbers from 1 to n.
- The program can be written in any programming language, but for this example, we will use Python.
- The algorithm for the program is as follows:

  - Initialize a variable sum to 0.
  - Initialize a variable i to 1.
  - Repeat the following steps until i is greater than n:
    - Add i to sum.
    - Increment i by 1.
  - Print the value of sum.

- The code for the program is as follows:

```python
# Python program to print the sum of all numbers up to a given number

# Take input from the user
n = int(input("Enter a positive integer: "))

# Initialize sum to 0
sum = 0

# Initialize i to 1
i = 1

# Repeat until i is greater than n
while i <= n:
  # Add i to sum
  sum = sum + i
  # Increment i by 1
  i = i + 1

# Print the sum
print("The sum of all numbers from 1 to", n, "is", sum)
```

- The output of the program for different values of n is as follows:

```
Enter a positive integer: 5
The sum of all numbers from 1 to 5 is 15
```

```
Enter a positive integer: 10
The sum of all numbers from 1 to 10 is 55
```

```
Enter a positive integer: 100
The sum of all numbers from 1 to 100 is 5050
```

- The program can be tested and run online using any online Python compiler or IDE, such as [Repl.it](https://repl.it/languages/python3).
- The program can be modified to use a different programming language, such as C, Java, or C++, by changing the syntax and input/output methods accordingly.