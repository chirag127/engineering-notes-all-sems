Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student. Here is the content in markdown format:

## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

- To write a program that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student, we need to follow these steps:

  - Declare variables to store the marks of 5 subjects, the sum and the percentage.
  - Take input from the user for the marks of 5 subjects using the `input()` function and convert them to integers using the `int()` function.
  - Calculate the sum of the marks by adding them together and store it in the sum variable.
  - Calculate the percentage of the marks by dividing the sum by the total marks (which is 500) and multiplying by 100 and store it in the percentage variable.
  - Print the sum and the percentage using the `print()` function with appropriate messages.

- Here is an example of the program in Python:

```python
# Declare variables
marks1 = 0
marks2 = 0
marks3 = 0
marks4 = 0
marks5 = 0
sum = 0
percentage = 0

# Take input from the user
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
marks4 = int(input("Enter marks of subject 4: "))
marks5 = int(input("Enter marks of subject 5: "))

# Calculate the sum and the percentage
sum = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (sum / 500) * 100

# Print the sum and the percentage
print("The sum of marks is:", sum)
print("The percentage of marks is:", percentage)
```

- Here is an example of the output of the program:

```
Enter marks of subject 1: 85
Enter marks of subject 2: 90
Enter marks of subject 3: 95
Enter marks of subject 4: 80
Enter marks of subject 5: 75
The sum of marks is: 425
The percentage of marks is: 85.0
```