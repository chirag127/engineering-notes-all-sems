## Between 90-100%-----Print ‘A’

- This is a common programming task that involves using conditional statements to check the value of a variable or expression and print a corresponding letter grade.
- A conditional statement is a block of code that executes only if a certain condition is true. For example, `if x > 10: print("x is greater than 10")` will print the message only if the value of x is more than 10.
- To check if a value is between 90 and 100, we can use the logical operator `and`, which returns true only if both operands are true. For example, `x > 90 and x < 100` will return true only if x is more than 90 and less than 100.
- To print a letter grade, we can use the `print` function, which takes an argument and displays it on the screen. For example, `print("A")` will print the letter A.
- Putting it all together, we can write a conditional statement that checks if a value is between 90 and 100 and prints A as follows:

```python
# Assume we have a variable called score that holds a numerical value
if score >= 90 and score <= 100: # Check if score is between 90 and 100
    print("A") # Print A
```

- Note that we used `>=` and `<=` instead of `>` and `<` to include the boundary values of 90 and 100. This is a common convention in grading systems, but it may vary depending on the context.