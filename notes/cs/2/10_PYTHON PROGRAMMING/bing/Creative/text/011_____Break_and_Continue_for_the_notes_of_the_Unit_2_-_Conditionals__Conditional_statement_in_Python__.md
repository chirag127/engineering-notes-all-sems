### Break and Continue

- Break and continue are two keywords that can be used to alter the flow of a loop in Python.
- Break is used to terminate the loop prematurely, when a certain condition is met.
- Continue is used to skip the current iteration of the loop, and move on to the next one, when a certain condition is met.
- Break and continue can be used with both for and while loops.

#### Examples of break and continue

- Suppose we want to loop through a list of numbers and print only the even ones, until we encounter a negative number. We can use break and continue as follows:

```python
numbers = [2, 4, 6, 8, -1, 10, 12]
for num in numbers:
  if num < 0:
    break # stop the loop
  if num % 2 != 0:
    continue # skip the odd number
  print(num)
```

- The output of this code is:

```output
2
4
6
8
```

- Suppose we want to loop through a string and print each character, except for vowels. We can use continue as follows:

```python
word = "python"
for char in word:
  if char in "aeiou":
    continue # skip the vowel
  print(char)
```

- The output of this code is:

```output
p
y
t
h
n
```