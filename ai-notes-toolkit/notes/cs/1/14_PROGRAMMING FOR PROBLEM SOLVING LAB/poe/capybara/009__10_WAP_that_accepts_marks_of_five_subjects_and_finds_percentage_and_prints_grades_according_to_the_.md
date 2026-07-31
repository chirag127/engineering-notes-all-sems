## 10. WAP that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

To create a program that accepts marks of five subjects, finds the percentage and prints grades according to the following criteria, you can follow these steps:

1. Start by defining variables to store the marks of each subject. You can name these variables as `mark1`, `mark2`, `mark3`, `mark4`, and `mark5`.

2. Prompt the user to enter the marks of each subject using the `input()` function. Make sure to convert the input values to integers using the `int()` function. 

3. Calculate the total marks by adding the marks of all five subjects. You can use the formula `total_marks = mark1 + mark2 + mark3 + mark4 + mark5`.

4. Calculate the percentage by dividing the total marks by the maximum marks and multiplying the result by 100. You can assume that the maximum marks for each subject is 100. You can use the formula `percentage = (total_marks / 500) * 100`.

5. Print the percentage using the `print()` function. You can format the output to display the percentage with two decimal places using the `format()` function. For example, `print("Percentage: {:.2f}%".format(percentage))`.

6. Determine the grade based on the percentage using the following criteria:
   - If the percentage is between 90 and 100, the grade is A+.
   - If the percentage is between 80 and 89, the grade is A.
   - If the percentage is between 70 and 79, the grade is B.
   - If the percentage is between 60 and 69, the grade is C.
   - If the percentage is between 50 and 59, the grade is D.
   - If the percentage is below 50, the grade is F.

7. Print the grade using the `print()` function. You can use a conditional statement to determine the grade based on the percentage. For example,
```
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")
```

By following these steps, you can create a program that accepts marks of five subjects, finds the percentage and prints grades according to the given criteria.