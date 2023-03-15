### Break and Continue

- Break and continue are two keywords that can be used to alter the flow of a loop in Python.
- Break is used to exit the loop prematurely, while continue is used to skip the current iteration and move on to the next one.
- Break and continue can be used with both for and while loops, but they have different effects depending on the type of loop.

#### Break with for loop

- A break statement inside a for loop will terminate the loop and execute the code after the loop.
- For example, the following code will print the numbers from 1 to 10, but stop when it reaches 5:

```python
for i in range(1, 11):
  print(i)
  if i == 5:
    break
print("Loop ended")
```

- The output will be:

```text
1
2
3
4
5
Loop ended
```

#### Break with while loop

- A break statement inside a while loop will also terminate the loop and execute the code after the loop.
- For example, the following code will print the numbers from 1 to 10, but stop when it reaches 5:

```python
i = 1
while i < 11:
  print(i)
  if i == 5:
    break
  i += 1
print("Loop ended")
```

- The output will be the same as the previous example.

#### Continue with for loop

- A continue statement inside a for loop will skip the current iteration and continue with the next one.
- For example, the following code will print the odd numbers from 1 to 10:

```python
for i in range(1, 11):
  if i % 2 == 0:
    continue
  print(i)
```

- The output will be:

```text
1
3
5
7
9
```

#### Continue with while loop

- A continue statement inside a while loop will also skip the current iteration and continue with the next one.
- For example, the following code will print the odd numbers from 1 to 10:

```python
i = 1
while i < 11:
  if i % 2 == 0:
    i += 1
    continue
  print(i)
  i += 1
```

- The output will be the same as the previous example.