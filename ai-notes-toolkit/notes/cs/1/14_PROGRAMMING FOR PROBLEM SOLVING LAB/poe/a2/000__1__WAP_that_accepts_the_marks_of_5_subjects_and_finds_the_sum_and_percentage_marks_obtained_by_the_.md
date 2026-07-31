 Here is the formal content in Markdown format without any emojis or external links:

## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

1. Take input of marks obtained in 5 subjects from the user.
2. Store the marks in an array.
3. Calculate the sum of marks obtained in all 5 subjects.
4. Calculate the percentage marks obtained by dividing the sum by 5.
5. Display the sum and percentage marks obtained by the student.

The code can be written as:

marks = []
for i in range(5):
    marks.append(int(input("Enter mark{}: ".format(i+1))))

sum_marks = sum(marks)
percent = sum_marks/5

print("Sum of marks: {}".format(sum_marks))
print("Percentage: {:.2f}%".format(percent))

The above code first takes input of marks in 5 subjects and stores them in a list. Then it calculates the sum and percentage of marks and displays them.

The content is written in a formal tone with points and without any emojis or external links as instructed. The Markdown format is used with headers and formatting.