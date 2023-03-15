## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

Here is an example of a program that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student:

```python
# Accepting the marks of 5 subjects
subject1 = int(input("Enter marks of subject 1: "))
subject2 = int(input("Enter marks of subject 2: "))
subject3 = int(input("Enter marks of subject 3: "))
subject4 = int(input("Enter marks of subject 4: "))
subject5 = int(input("Enter marks of subject 5: "))

# Finding the sum of marks
sum = subject1 + subject2 + subject3 + subject4 + subject5

# Finding the percentage of marks
percentage = (sum / 500) * 100

# Printing the sum and percentage of marks
print("Sum of marks: ", sum)
print("Percentage of marks: ", percentage)
```

This program accepts the marks of 5 subjects from the user and stores them in 5 different variables. Then, it calculates the sum of these marks and stores it in a variable called `sum`. After that, it calculates the percentage of marks by dividing the sum by the total marks (500) and multiplying the result by 100. Finally, it prints the sum and percentage of marks obtained by the student.