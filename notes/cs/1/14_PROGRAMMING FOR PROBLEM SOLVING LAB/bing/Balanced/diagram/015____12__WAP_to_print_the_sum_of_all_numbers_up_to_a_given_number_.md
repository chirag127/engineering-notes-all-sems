## 12. WAP to print the sum of all numbers up to a given number.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- To print the sum of all numbers up to a given number, we need to use a loop that iterates from 1 to the given number and adds each number to a variable that stores the sum.
- We also need to use an input function that allows the user to enter the given number and a print function that displays the sum on the screen.
- Here is an example of a WAP to print the sum of all numbers up to a given number in Python:

```python
# WAP to print the sum of all numbers up to a given number

# Ask the user to enter a number
n = int(input("Enter a number: "))

# Initialize a variable to store the sum
sum = 0

# Use a loop to iterate from 1 to n
for i in range(1, n + 1):
  # Add each number to the sum
  sum = sum + i

# Print the sum
print("The sum of all numbers up to", n, "is", sum)
```

- Here is the output of the program for different inputs:

```text
Enter a number: 5
The sum of all numbers up to 5 is 15

Enter a number: 10
The sum of all numbers up to 10 is 55

Enter a number: 100
The sum of all numbers up to 100 is 5050
```

- Here are some points to remember when writing a WAP to print the sum of all numbers up to a given number:

  - Use a descriptive variable name for the sum, such as sum, total, or result.
  - Use a loop that starts from 1 and ends at the given number, not 0 and n - 1.
  - Use the range function to generate a sequence of numbers from 1 to n, and use n + 1 as the second argument to include n in the loop.
  - Use the input function to get the user input as a string and convert it to an integer using the int function.
  - Use the print function to display the sum and the given number, and use commas to separate them. You can also use string formatting or concatenation to format the output.