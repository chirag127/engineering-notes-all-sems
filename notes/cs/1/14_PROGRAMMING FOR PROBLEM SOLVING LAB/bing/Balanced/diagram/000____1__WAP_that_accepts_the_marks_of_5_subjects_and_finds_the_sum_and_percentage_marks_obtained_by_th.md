## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

- WAP stands for Write a Program, which is a common abbreviation used in programming assignments.
- To write a program that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student, we need to follow these steps:

  - Declare variables to store the marks of 5 subjects, the sum and the percentage.
  - Prompt the user to enter the marks of 5 subjects and store them in the variables.
  - Calculate the sum by adding the marks of 5 subjects.
  - Calculate the percentage by dividing the sum by the total marks (which is 500) and multiplying by 100.
  - Display the sum and the percentage to the user.

- Here is an example of a program written in Python that implements these steps:

```python
# Declare variables
mark1 = 0
mark2 = 0
mark3 = 0
mark4 = 0
mark5 = 0
sum = 0
percentage = 0

# Prompt the user to enter the marks of 5 subjects
mark1 = int(input("Enter the mark of subject 1: "))
mark2 = int(input("Enter the mark of subject 2: "))
mark3 = int(input("Enter the mark of subject 3: "))
mark4 = int(input("Enter the mark of subject 4: "))
mark5 = int(input("Enter the mark of subject 5: "))

# Calculate the sum
sum = mark1 + mark2 + mark3 + mark4 + mark5

# Calculate the percentage
percentage = (sum / 500) * 100

# Display the sum and the percentage
print("The sum of marks is: ", sum)
print("The percentage of marks is: ", percentage)
```