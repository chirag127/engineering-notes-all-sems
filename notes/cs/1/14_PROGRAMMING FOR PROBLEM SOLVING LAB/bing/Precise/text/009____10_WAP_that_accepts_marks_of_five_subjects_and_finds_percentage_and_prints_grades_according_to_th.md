## 10. WAP that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

1. First, the program should prompt the user to enter the marks of five subjects.
2. The marks entered by the user should be stored in variables or an array.
3. The program should then calculate the total marks obtained by adding the marks of all five subjects.
4. The percentage can be calculated by dividing the total marks by the maximum possible marks and multiplying the result by 100.
5. Once the percentage is calculated, the program should use conditional statements to determine the grade according to the given criteria.
6. The grade should then be printed to the screen.

Here is an example of how the code for this program might look like in Python:

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

# Determine grade according to the given criteria
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

# Print the grade
print("Grade:", grade)
```