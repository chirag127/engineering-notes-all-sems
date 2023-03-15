### Break and Continue

- Break and continue are two keywords that can be used to alter the flow of a loop in Python.
- Break is used to exit the loop prematurely, while continue is used to skip the current iteration and move on to the next one.
- Break and continue can be used with both for and while loops, but they have different effects depending on the type of loop.

#### Break with for loop

- A break statement inside a for loop will terminate the loop and execute the code after the loop.
- For example, the following code will print the numbers from 1 to 10, but stop at 5 because of the break statement.

```python
for i in range(1, 11):
  print(i)
  if i == 5:
    break
print("Loop ended")
```

- The output of this code is:

```
1
2
3
4
5
Loop ended
```

#### Break with while loop

- A break statement inside a while loop will also terminate the loop and execute the code after the loop.
- For example, the following code will print the numbers from 1 to 10, but stop at 5 because of the break statement.

```python
i = 1
while i <= 10:
  print(i)
  if i == 5:
    break
  i += 1
print("Loop ended")
```

- The output of this code is the same as the previous one:

```
1
2
3
4
5
Loop ended
```

#### Continue with for loop

- A continue statement inside a for loop will skip the current iteration and continue with the next one.
- For example, the following code will print the odd numbers from 1 to 10, by using continue to skip the even numbers.

```python
for i in range(1, 11):
  if i % 2 == 0:
    continue
  print(i)
print("Loop ended")
```

- The output of this code is:

```
1
3
5
7
9
Loop ended
```

#### Continue with while loop

- A continue statement inside a while loop will also skip the current iteration and continue with the next one.
- For example, the following code will print the odd numbers from 1 to 10, by using continue to skip the even numbers.

```python
i = 1
while i <= 10:
  if i % 2 == 0:
    i += 1
    continue
  print(i)
  i += 1
print("Loop ended")
```

- The output of this code is the same as the previous one:

```
1
3
5
7
9
Loop ended
```

- Note that in this case, the increment of i has to be done before the continue statement, otherwise the loop will never end.