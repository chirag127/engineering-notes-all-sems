## Between 90-100%-----Print ‘A’

- This is a common way of assigning grades based on percentage scores in some educational systems.
- It means that if a student scores between 90% and 100% on a test or assignment, they will receive an ‘A’ grade, which is the highest possible grade.
- To implement this logic in a programming language, one can use a conditional statement that checks if the percentage score is within the specified range, and then prints ‘A’ as the output.
- For example, in Python, one can write:

```python
# Assume score is a variable that stores the percentage score
if 90 <= score <= 100: # Check if score is between 90 and 100
    print('A') # Print 'A' as the output
```

- Alternatively, one can use a nested conditional statement that checks if the percentage score is greater than or equal to 90, and then checks if it is less than or equal to 100, and then prints ‘A’ as the output.
- For example, in Python, one can write:

```python
# Assume score is a variable that stores the percentage score
if score >= 90: # Check if score is greater than or equal to 90
    if score <= 100: # Check if score is less than or equal to 100
        print('A') # Print 'A' as the output
```

- Both methods are equivalent and will produce the same result. However, the first method is more concise and readable, and is therefore preferred.