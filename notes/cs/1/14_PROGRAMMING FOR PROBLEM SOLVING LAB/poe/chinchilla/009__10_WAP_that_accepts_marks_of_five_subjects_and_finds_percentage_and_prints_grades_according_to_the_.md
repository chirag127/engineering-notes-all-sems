## 10. WAP that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

In this program, we will create a Python script that can accept marks of five subjects and calculate the percentage of the total marks obtained. Moreover, based on the percentage calculated, the program will print the corresponding grade according to the following criteria:

- 90% or above: A+
- 80% to 89.99%: A
- 70% to 79.99%: B+
- 60% to 69.99%: B
- 50% to 59.99%: C+
- 40% to 49.99%: C
- Below 40%: Fail

To achieve this, we will follow the following steps:

1. First, we will create a Python script, and we will import the necessary modules required to run the program, such as `os` module, which is used to clear the console screen.

2. Next, we will create a function named `calculate_percentage`, which will accept the marks of five subjects as input from the user and calculate the percentage of the total marks obtained.

3. After that, we will define a function named `calculate_grade`, which will accept the percentage calculated in the previous step and determine the grade based on the criteria mentioned above.

4. Finally, we will create the main function, which will call the `calculate_percentage` and `calculate_grade` functions and print the percentage and grade obtained by the student.

Here is the code for the program:

``` python
import os

def calculate_percentage():
    marks = []
    for i in range(5):
        subject = input("Enter the marks of subject {}: ".format(i+1))
        marks.append(int(subject))
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    return percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80 and percentage < 90:
        return "A"
    elif percentage >= 70 and percentage < 80:
        return "B+"
    elif percentage >= 60 and percentage < 70:
        return "B"
    elif percentage >= 50 and percentage < 60:
        return "C+"
    elif percentage >= 40 and percentage < 50:
        return "C"
    else:
        return "Fail"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    percentage = calculate_percentage()
    grade = calculate_grade(percentage)
    print("Percentage: {:.2f}%".format(percentage))
    print("Grade: {}".format(grade))

if __name__ == '__main__':
    main()
```

In conclusion, this program can be used to calculate the percentage of the total marks obtained by a student and determine their grade based on the criteria mentioned above. It can be helpful for students and teachers to evaluate the performance of the student in a particular subject or overall.