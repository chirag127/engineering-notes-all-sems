## Between 90-100%-----Print ‘A’

- This is a common programming task that involves using conditional statements to print a letter grade based on a percentage score.
- A conditional statement is a block of code that executes only if a certain condition is true. For example, `if x > 10: print("x is greater than 10")`.
- To print a letter grade based on a percentage score, we need to compare the score with different ranges of values and print the corresponding letter. For example, `if score >= 90: print("A")`.
- The ranges of values for letter grades are usually as follows:

  - A: 90-100%
  - B: 80-89%
  - C: 70-79%
  - D: 60-69%
  - F: below 60%

- To cover all the possible cases, we need to use `elif` and `else` statements after the first `if` statement. `elif` stands for "else if" and `else` stands for "otherwise". For example, `elif score >= 80: print("B")` and `else: print("F")`.
- The complete code for printing a letter grade based on a percentage score in Python is:

```python
# Get the percentage score from the user
score = float(input("Enter your score: "))

# Check the score and print the letter grade
if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
elif score >= 60:
  print("D")
else:
  print("F")
```

- The code for printing a letter grade based on a percentage score in other programming languages may vary slightly in syntax, but the logic is the same.