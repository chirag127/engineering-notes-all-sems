## Between 90-100%-----Print ‘A’

- This is a common programming task that involves using conditional statements to assign grades based on numerical scores.
- The syntax and logic may vary depending on the programming language, but the general idea is to compare the score with a range of values and print the corresponding grade.
- For example, in Python, one possible way to implement this task is:

```python
# Assume score is a variable that holds the numerical score
if score >= 90 and score <= 100: # Check if the score is between 90 and 100
    print('A') # Print A as the grade
elif score >= 80 and score < 90: # Check if the score is between 80 and 90
    print('B') # Print B as the grade
elif score >= 70 and score < 80: # Check if the score is between 70 and 80
    print('C') # Print C as the grade
elif score >= 60 and score < 70: # Check if the score is between 60 and 70
    print('D') # Print D as the grade
else: # For any other score
    print('F') # Print F as the grade
```

- In this example, the `if` statement evaluates the first condition, which is `score >= 90 and score <= 100`. This means that the score must be greater than or equal to 90 and less than or equal to 100. If this condition is true, the program executes the indented block of code, which is `print('A')`, and then exits the `if` statement. If this condition is false, the program moves on to the next condition, which is `score >= 80 and score < 90`, and so on, until it finds a condition that is true or reaches the `else` clause, which is the default case when none of the conditions are true.
- The `and` operator is used to combine two conditions that must both be true for the whole expression to be true. The `>=` and `<=` operators are used to check if a value is greater than or equal to, or less than or equal to, another value. The `<` and `>` operators are used to check if a value is strictly less than or greater than another value. The `print()` function is used to display a message on the screen.
- Other programming languages may have different ways of writing conditional statements, such as using `switch` or `case` statements, or using different symbols or keywords for operators or functions. However, the basic logic of comparing the score with a range of values and printing the corresponding grade remains the same.