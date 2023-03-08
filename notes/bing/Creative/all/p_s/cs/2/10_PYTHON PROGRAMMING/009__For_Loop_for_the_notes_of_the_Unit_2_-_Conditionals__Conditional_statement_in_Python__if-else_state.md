### For Loop

- A for loop is a control structure that allows you to repeat a block of code a fixed number of times.
- In Python, a for loop is used for iterating over a sequence, such as a list, a tuple, a dictionary, a set, or a string.
- Unlike other programming languages, Python does not have a C-style for loop that uses a counter variable and a condition. Instead, Python uses an iterator method that automatically produces the next item in the sequence.
- The syntax of a for loop in Python is:

```python
for item in sequence:
    # do something with item
```

- The `item` variable is a temporary name that refers to the current element in the sequence. You can use any valid identifier as the name of the item variable.
- The `sequence` can be any iterable object that supports the `__iter__()` and `__next__()` methods, such as a list, a tuple, a range, etc.
- The `:` symbol marks the end of the for loop header and the beginning of the loop body, which is indented by four spaces or a tab.
- The loop body contains the statements that are executed for each item in the sequence. The loop body can have one or more statements, or it can be empty (in which case you need to use the `pass` statement to avoid a syntax error).
- The for loop terminates when the sequence is exhausted or when a `break` statement is encountered inside the loop body. A `break` statement allows you to exit the loop prematurely, skipping the remaining items in the sequence.
- You can also use a `continue` statement inside the loop body to skip the current iteration and move on to the next item in the sequence. A `continue` statement is useful when you want to skip some items based on a condition.
- You can also use an `else` clause after the for loop to execute a block of code when the loop ends normally, i.e., without encountering a `break` statement. The `else` clause is optional and rarely used.

#### Examples of for loop in Python

- Here is an example of a for loop that prints the elements of a list:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Output:

```
apple
banana
cherry
```

- Here is an example of a for loop that iterates over a range of numbers from 1 to 10 and prints the square of each number:

```python
for num in range(1, 11):
    print(num ** 2)
```

Output:

```
1
4
9
16
25
36
49
64
81
100
```

- Here is an example of a for loop that iterates over the keys of a dictionary and prints the key-value pairs:

```python
student = {"name": "John", "age": 18, "grade": "A"}
for key in student:
    print(key, "=", student[key])
```

Output:

```
name = John
age = 18
grade = A
```

- Here is an example of a for loop that uses a break statement to stop the loop when it finds the letter "e" in a string:

```python
word = "Hello"
for letter in word:
    if letter == "e":
        print("Found e, stopping the loop.")
        break
    print(letter)
```

Output:

```
H
Found e, stopping the loop.
```

- Here is an example of a for loop that uses a continue statement to skip the letter "o" in a string:

```python
word = "Hello"
for letter in word:
    if letter == "o":
        print("Skipping o.")
        continue
    print(letter)
```

Output:

```
H
e
l
l
Skipping o.
```

- Here is an example of a for loop that uses an else clause to print a message when the loop ends normally:

```python
for num in range(1, 6):
    print(num)
else:
    print("The loop is over.")
```

Output:

```
1
2
3
4
5
The loop is over.
```

Some possible mnemonics and learning tricks for the topic are:

- To remember the syntax of a for loop, you can use the acronym FISE: For, In, Sequence, Else.
- To remember the difference between break and continue, you can use the rhyme: Break is to stop, continue is to hop.
- To remember the order of execution of a for loop, you can use the phrase: Header, Body, Else, Next.