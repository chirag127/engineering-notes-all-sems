## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

- A WAP (Write a Program) is a task that requires writing a computer program in a specific programming language to perform a certain operation or function.
- To write a WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student, we need to follow these steps:
  - Declare and initialize variables to store the marks of 5 subjects, the sum and the percentage.
  - Prompt the user to enter the marks of 5 subjects and store them in the variables using input statements.
  - Calculate the sum of the marks by adding the values of the variables using arithmetic operators.
  - Calculate the percentage of the marks by dividing the sum by the total marks (which is 500) and multiplying by 100 using arithmetic operators.
  - Display the sum and the percentage of the marks using output statements.
- Here is an example of a WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student in Python:

```python
# Declare and initialize variables
marks1 = 0
marks2 = 0
marks3 = 0
marks4 = 0
marks5 = 0
sum = 0
percentage = 0

# Prompt the user to enter the marks of 5 subjects and store them in the variables
marks1 = int(input("Enter the marks of subject 1: "))
marks2 = int(input("Enter the marks of subject 2: "))
marks3 = int(input("Enter the marks of subject 3: "))
marks4 = int(input("Enter the marks of subject 4: "))
marks5 = int(input("Enter the marks of subject 5: "))

# Calculate the sum of the marks by adding the values of the variables
sum = marks1 + marks2 + marks3 + marks4 + marks5

# Calculate the percentage of the marks by dividing the sum by the total marks and multiplying by 100
percentage = (sum / 500) * 100

# Display the sum and the percentage of the marks
print("The sum of the marks is:", sum)
print("The percentage of the marks is:", percentage)
```