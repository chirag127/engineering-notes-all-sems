## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

Here is a sample program in Python that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student:

```python
# Accepting the marks of 5 subjects
subject1 = int(input("Enter marks of subject 1: "))
subject2 = int(input("Enter marks of subject 2: "))
subject3 = int(input("Enter marks of subject 3: "))
subject4 = int(input("Enter marks of subject 4: "))
subject5 = int(input("Enter marks of subject 5: "))

# Calculating the sum of marks
sum = subject1 + subject2 + subject3 + subject4 + subject5

# Calculating the percentage
percentage = (sum / 500) * 100

# Displaying the sum and percentage
print("Sum of marks:", sum)
print("Percentage:", percentage)
```

This program prompts the user to enter the marks of 5 subjects. The marks are then stored in variables `subject1`, `subject2`, `subject3`, `subject4`, and `subject5`. The sum of the marks is calculated by adding the values of these variables and stored in the variable `sum`. The percentage is then calculated by dividing the sum by the total marks (500) and multiplying by 100. The sum and percentage are then displayed using the `print` function.