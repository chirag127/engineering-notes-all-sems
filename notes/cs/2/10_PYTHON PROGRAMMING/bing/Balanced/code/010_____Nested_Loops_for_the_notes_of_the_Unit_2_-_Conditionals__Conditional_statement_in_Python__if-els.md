### Nested Loops

- A nested loop is a loop that is placed inside another loop.
- Nested loops can be used to perform repeated tasks on each element of a collection, such as a list, a tuple, a string, or a dictionary.
- Nested loops can also be used to create patterns, such as grids, tables, or shapes, by using print statements inside the loops.
- The syntax of a nested loop is similar to a regular loop, except that the inner loop is indented under the outer loop.
- The inner loop executes all its iterations for each iteration of the outer loop.
- The inner loop can use the same or a different loop variable as the outer loop.
- The inner loop can also use the loop variable of the outer loop in its condition or body.
- The flow of control in a nested loop is as follows:
  - The outer loop starts from its initial value and checks its condition.
  - If the condition is true, the outer loop enters its body and executes the first statement, which is the inner loop.
  - The inner loop starts from its initial value and checks its condition.
  - If the condition is true, the inner loop enters its body and executes its statements.
  - The inner loop then increments or decrements its loop variable and checks its condition again.
  - The inner loop repeats this process until its condition becomes false.
  - The outer loop then increments or decrements its loop variable and checks its condition again.
  - The outer loop repeats this process until its condition becomes false.
- An example of a nested loop is:

```python
# This nested loop prints a 5x5 grid of asterisks
for i in range(5): # outer loop
  for j in range(5): # inner loop
    print("*", end=" ") # print an asterisk and a space
  print() # print a newline after each row
```

- The output of this nested loop is:

```
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
```