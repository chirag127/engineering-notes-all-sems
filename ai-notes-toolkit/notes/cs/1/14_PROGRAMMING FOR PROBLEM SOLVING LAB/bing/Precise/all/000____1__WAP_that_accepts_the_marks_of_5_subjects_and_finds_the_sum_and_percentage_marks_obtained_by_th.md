## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

A WAP (Write a Program) is a common term used in computer science and programming to refer to the task of writing a computer program to solve a specific problem or perform a specific task.

In this case, the WAP is to write a program that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student. Here are the steps to solve this problem:

1. Define a variable to store the marks of each subject.
2. Accept the marks of 5 subjects from the user and store them in the respective variables.
3. Calculate the sum of the marks by adding the marks of all 5 subjects.
4. Calculate the percentage marks by dividing the sum of the marks by the total marks and multiplying by 100.
5. Display the sum and percentage marks obtained by the student.

Here is an example of a program written in Python that solves this problem:

```python
# Define variables to store the marks of each subject
subject1 = 0
subject2 = 0
subject3 = 0
subject4 = 0
subject5 = 0

# Accept the marks of 5 subjects from the user
subject1 = int(input("Enter the marks of subject 1: "))
subject2 = int(input("Enter the marks of subject 2: "))
subject3 = int(input("Enter the marks of subject 3: "))
subject4 = int(input("Enter the marks of subject 4: "))
subject5 = int(input("Enter the marks of subject 5: "))

# Calculate the sum of the marks
sum_of_marks = subject1 + subject2 + subject3 + subject4 + subject5

# Calculate the percentage marks
percentage_marks = (sum_of_marks / 500) * 100

# Display the sum and percentage marks obtained by the student
print("Sum of marks: ", sum_of_marks)
print("Percentage marks: ", percentage_marks)
```

This program accepts the marks of 5 subjects from the user, calculates the sum and percentage marks, and displays the result. The user can run this program and enter the marks of the 5 subjects to find the sum and percentage marks obtained by the student.