## 10.WAP that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

- A WAP (Write a Program) is a task that requires writing a computer program in a specific programming language to achieve a desired output or functionality.
- In this task, the program should accept marks of five subjects as input from the user, calculate the percentage of marks obtained, and print the grade according to the following criteria:

| Percentage | Grade |
|------------|-------|
| >= 90      | A+    |
| >= 80      | A     |
| >= 70      | B+    |
| >= 60      | B     |
| >= 50      | C+    |
| >= 40      | C     |
| < 40       | F     |

- One possible way to write the program in Python is:

```python
# Input marks of five subjects
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

# Calculate percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

# Print percentage
print("Percentage: ", percentage)

# Print grade according to criteria
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B+")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C+")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: F")
```

- Some mnemonics and learning tricks for this task are:

  - Remember the formula for percentage: (total marks / maximum marks) * 100
  - Remember the order of the grade criteria: A+, A, B+, B, C+, C, F
  - Remember the comparison operators: >= (greater than or equal to), < (less than)
  - Remember the if-elif-else structure: if (condition): (statement), elif (condition): (statement), else: (statement)
  - Remember the indentation: use four spaces or a tab to indent the statements inside the if-elif-else blocks