Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

- If percentage is greater than or equal to 90, grade is A+
- If percentage is greater than or equal to 80 and less than 90, grade is A
- If percentage is greater than or equal to 70 and less than 80, grade is B+
- If percentage is greater than or equal to 60 and less than 70, grade is B
- If percentage is greater than or equal to 50 and less than 60, grade is C
- If percentage is less than 50, grade is F

Here is the program in Python:

```python
# WAP that accepts marks of five subjects and finds percentage and prints grades

# Input marks of five subjects
marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))
marks4 = float(input("Enter marks of subject 4: "))
marks5 = float(input("Enter marks of subject 5: "))

# Calculate total marks and percentage
total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total / 500) * 100

# Print percentage
print("Percentage: ", percentage)

# Print grade according to criteria
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B+"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "F"

print("Grade: ", grade)
```
