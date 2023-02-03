### While loop including its working for the notes of the Unit 2 - Conditionals: Conditional statement in Python (if-else statement, its working and execution), Nested-if statement and Elif statement in Python, Expression Evaluation & Float Representation. in the subject of PYTHON PROGRAMMING

The while loop in Python is a control structure that allows you to repeat a block of code repeatedly until a certain condition is met. The basic syntax of the while loop is as follows:

```
while condition:
    # code to be executed
```

The `condition` in the while loop is evaluated before each iteration of the loop. If the condition is `True`, the code inside the loop is executed. If the condition is `False`, the loop terminates and control is transferred to the next statement after the loop.

Here's an example of how the while loop can be used to print the numbers 1 to 10:

```
counter = 1
while counter <= 10:
    print(counter)
    counter += 1
```

In this example, the variable `counter` is initialized to 1. The while loop continues to execute as long as the value of `counter` is less than or equal to 10. Inside the loop, the value of `counter` is printed and then incremented by 1.

It's important to be careful when using while loops, as they can run indefinitely if the condition is never met. To avoid this, it's a good practice to include a counter or some other mechanism to ensure that the loop will eventually terminate.
