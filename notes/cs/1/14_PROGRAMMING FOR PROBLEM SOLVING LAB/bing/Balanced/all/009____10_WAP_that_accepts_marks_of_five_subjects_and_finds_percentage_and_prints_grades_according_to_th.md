Hello, I am Sydney, your AI assistant. I can help you with your programming assignments. Here is the content for the topic you requested:

## 10.WAP that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

- The program should take the marks of five subjects as input from the user and store them in variables.
- The program should calculate the total marks by adding the marks of all the subjects and store it in a variable.
- The program should calculate the percentage by dividing the total marks by the maximum possible marks (which is 500) and multiplying by 100 and store it in a variable.
- The program should print the percentage and the grade according to the following criteria:

  - If the percentage is greater than or equal to 90, the grade is A+.
  - If the percentage is greater than or equal to 80 and less than 90, the grade is A.
  - If the percentage is greater than or equal to 70 and less than 80, the grade is B+.
  - If the percentage is greater than or equal to 60 and less than 70, the grade is B.
  - If the percentage is greater than or equal to 50 and less than 60, the grade is C+.
  - If the percentage is greater than or equal to 40 and less than 50, the grade is C.
  - If the percentage is less than 40, the grade is F.

- The program should use conditional statements (such as if-else) to check the percentage and print the corresponding grade.
- The program should use print statements to display the output to the user.

- Here is an example of the program in Python:

```python
# WAP that accepts marks of five subjects and finds percentage and prints grades

# Input marks of five subjects
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

# Calculate total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage
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