### For Loop

- A for loop is a type of loop that iterates over a sequence of items, such as a list, a tuple, a string, or a range object.
- The syntax of a for loop is:

```python
for item in sequence:
    # do something with item
```

- The item variable can be any valid identifier, and it takes the value of each element in the sequence in each iteration.
- The sequence can be any iterable object that supports the `__iter__` and `__next__` methods, such as a list, a tuple, a string, or a range object.
- The body of the loop is indented under the for statement, and it can contain any valid Python statements, including other loops, conditionals, or function calls.
- The loop terminates when the sequence is exhausted, or when a `break` or `return` statement is encountered inside the loop body.
- A for loop can also have an optional `else` clause, which is executed when the loop ends normally, i.e., without a `break` or `return` statement. The syntax of a for loop with an else clause is:

```python
for item in sequence:
    # do something with item
else:
    # do something else
```

- Some examples of for loops are:

```python
# print the numbers from 1 to 10
for i in range(1, 11):
    print(i)

# print the elements of a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# print the characters of a string
name = "Sydney"
for char in name:
    print(char)

# print the sum of the elements of a list
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
else:
    print("The sum is", sum)
```