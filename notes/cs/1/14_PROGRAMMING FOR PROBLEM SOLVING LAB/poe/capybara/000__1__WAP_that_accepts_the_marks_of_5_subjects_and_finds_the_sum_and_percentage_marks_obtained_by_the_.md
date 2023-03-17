## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

Here are some points to keep in mind when writing a program that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student:

- The program should prompt the user to enter the marks of each subject, one at a time.
- The program should validate the input to ensure that the marks entered are between 0 and 100, inclusive.
- The program should calculate the sum of the marks obtained by the student.
- The program should calculate the percentage marks obtained by the student by dividing the sum of the marks by the total possible marks (i.e., 500) and multiplying the result by 100.
- The program should then display the sum and percentage marks obtained by the student.

Here's an example code snippet in Python:

```
# Prompt user to enter marks for each subject
marks = []
for i in range(5):
    mark = int(input("Enter marks for subject {}: ".format(i+1)))
    while mark < 0 or mark > 100:
        mark = int(input("Invalid input. Enter marks for subject {}: ".format(i+1)))
    marks.append(mark)

# Calculate sum and percentage marks
sum_marks = sum(marks)
percentage_marks = (sum_marks / 500) * 100

# Display results
print("Sum of marks: {}".format(sum_marks))
print("Percentage marks: {:.2f}%".format(percentage_marks))
```

Remember to test your program with different inputs to ensure it works correctly.