## 10. Write a program that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

1. First, the program should prompt the user to enter the marks of five subjects.
2. The program should then calculate the total marks and percentage by adding the marks of all five subjects and dividing the sum by the total number of subjects.
3. Based on the calculated percentage, the program should print the corresponding grade according to the following criteria:
    - If the percentage is greater than or equal to 90, the grade is 'A'.
    - If the percentage is greater than or equal to 80 and less than 90, the grade is 'B'.
    - If the percentage is greater than or equal to 70 and less than 80, the grade is 'C'.
    - If the percentage is greater than or equal to 60 and less than 70, the grade is 'D'.
    - If the percentage is less than 60, the grade is 'F'.
4. The program should then print the total marks, percentage, and grade.

Here is an example of how the program could be implemented in Python:

```python
# Accept marks of five subjects
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

# Calculate total marks and percentage
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100

# Determine grade based on percentage
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print total marks, percentage, and grade
print("Total Marks: ", total_marks)
print("Percentage: ", percentage)
print("Grade: ", grade)
```