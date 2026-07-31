 Here is the content in markdown format without any feeling or friendliness, being formal and without any emojis or external links:

### Break and Continue for the notes of the Unit 2 - Conditionals: Conditional statement in Python (if-else statement, its working and execution), Nested-if statement and Elif statement in Python, Expression Evaluation & Float Representation.

1. Break statement:
- Used to exit a loop immediately.
- Terminates the loop and the control returns to the next statement after the loop.
- Syntax: `break`

2. Continue statement:
- Used to skip the remaining part of the loop for the current iteration.
- The control jumps to the beginning of the loop for the next iteration.
- Syntax: `continue`

3. Usage of Break and Continue statements:
- Break is used to exit a loop completely.
- Continue is used to skip the current block, and return to the "top" of the loop.
- Both can be used in both While and For Loops.

4. Example of Break statement:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
Output: 0 1 2 3 4
The loop exits when i equals 5.

5. Example of Continue statement:
```python
for i in range(10):
    if i == 5:
        continue
    print(i)
```
Output: 0 1 2 3 4 6 7 8 9
The printing is skipped for i = 5, but the loop continues.

6. Use cases:
- Break is useful to exit a loop when some condition is met.
- Continue is useful to skip some iterations when some condition is met.