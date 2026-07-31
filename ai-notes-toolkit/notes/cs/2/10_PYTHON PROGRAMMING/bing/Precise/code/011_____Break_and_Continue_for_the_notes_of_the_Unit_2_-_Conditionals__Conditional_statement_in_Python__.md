### Break and Continue

`break` and `continue` are two important statements in Python that are used to control the flow of execution in a loop.

- `break` is used to exit a loop prematurely. When a `break` statement is encountered inside a loop, the loop is immediately terminated and the program control resumes at the next statement following the loop.

- `continue` is used to skip the rest of the code inside a loop for the current iteration only. When a `continue` statement is encountered inside a loop, the control is transferred to the beginning of the loop for the next iteration, bypassing the remaining statements in the loop.

Here is an example that demonstrates the use of `break` and `continue` in a `for` loop:

```python
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
```

In this example, the `continue` statement is encountered when `i` is equal to 5. This causes the loop to skip the `print` statement for this iteration and move on to the next iteration. The `break` statement is encountered when `i` is equal to 8. This causes the loop to terminate and the program control to move to the next statement following the loop.

It is important to use `break` and `continue` statements judiciously as they can make the code difficult to read and understand if not used properly. It is also important to note that `break` and `continue` statements only affect the innermost loop in which they are used. If used inside a nested loop, they will only affect the innermost loop and not the outer loops.