## 10.WAP that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

Here is the code for the 10th WAP in Python:

```
marks = []
for i in range(5):
    m = float(input("Enter marks of subject {}: ".format(i+1)))
    marks.append(m)

total = sum(marks)
percentage = total / 5

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

print("Percentage: {:.2f}%".format(percentage))
print("Grade:", grade)
```

The code first takes input of the marks of five subjects and stores them in a list. Then, it calculates the total marks and the percentage by dividing the total by 5.

Next, it uses if-elif statements to determine the grade based on the following criteria:
- If the percentage is 90 or above, the grade is 'A'
- If the percentage is between 80 and 90 (inclusive), the grade is 'B'
- If the percentage is between 70 and 80 (inclusive), the grade is 'C'
- If the percentage is between 60 and 70 (inclusive), the grade is 'D'
- If the percentage is below 60, the grade is 'F'

Finally, the code prints the percentage and the grade.
