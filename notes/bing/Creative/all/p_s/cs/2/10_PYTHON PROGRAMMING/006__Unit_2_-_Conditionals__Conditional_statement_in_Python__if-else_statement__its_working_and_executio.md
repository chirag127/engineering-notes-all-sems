## Unit 2 - Conditionals: Conditional statement in Python (if-else statement, its working and execution), Nested-if statement and Elif statement in Python, Expression Evaluation & Float Representation.

- A conditional statement in python, also called a condition construct, is a statement that accommodates a condition inside itself. This condition is constructed using the bitwise, boolean, and comparison operators in Python.
- A conditional statement allows us to execute different blocks of code depending on whether certain conditions are true or false.
- Python supports the following types of conditional statements:
  - if statement: The simplest and most used conditional statement in Python. It evaluates an expression and executes a block of code if the expression is true .
  - if-else statement: A conditional statement that executes a block of code if the expression is true, and another block of code if the expression is false .
  - if-elif-else statement: A conditional statement that can have multiple branches of execution based on different conditions. The elif keyword stands for else if, and it allows us to check for more than one condition .
  - switch case statement: A conditional statement that is not directly supported by Python, but can be implemented using a dictionary or a function. It allows us to execute different blocks of code based on the value of a variable or an expression.

- The syntax of the if statement in Python is as follows:

```python
if expression:
    # block of code to execute if expression is true
```

- The syntax of the if-else statement in Python is as follows:

```python
if expression:
    # block of code to execute if expression is true
else:
    # block of code to execute if expression is false
```

- The syntax of the if-elif-else statement in Python is as follows:

```python
if expression1:
    # block of code to execute if expression1 is true
elif expression2:
    # block of code to execute if expression2 is true
elif expression3:
    # block of code to execute if expression3 is true
...
else:
    # block of code to execute if none of the expressions are true
```

- The syntax of the switch case statement in Python using a dictionary is as follows:

```python
switcher = {
    case1: value1,
    case2: value2,
    case3: value3,
    ...
}

# get the value associated with the case
value = switcher.get(case, default_value)

# execute the block of code based on the value
if value == value1:
    # block of code for case1
elif value == value2:
    # block of code for case2
elif value == value3:
    # block of code for case3
...
else:
    # block of code for default case
```

- The syntax of the switch case statement in Python using a function is as follows:

```python
def switch(case):
    # define a function for each case
    def case1():
        # block of code for case1
        return value1
    def case2():
        # block of code for case2
        return value2
    def case3():
        # block of code for case3
        return value3
    ...
    def default():
        # block of code for default case
        return default_value

    # create a dictionary that maps each case to its corresponding function
    switcher = {
        case1: case1,
        case2: case2,
        case3: case3,
        ...
    }

    # get the function associated with the case
    func = switcher.get(case, default)

    # execute the function and return its value
    return func()

# call the switch function with the case
value = switch(case)
```

- A nested-if statement is a conditional statement that contains another conditional statement inside its block of code. It allows us to check for more complex conditions and execute different blocks of code accordingly .
- The syntax of a nested-if statement in Python is as follows:

```python
if expression1:
    # block of code to execute if expression1 is true
    if expression2:
        # block of code to execute if expression2 is true
    else:
        # block of code to execute if expression2 is false
else:
    # block of code to execute if expression1 is false
```

- Expression evaluation

I'm not sure what topic you are referring to, but I can try to help you find some good mnemonics and learning tricks if you tell me more. Mnemonics and learning tricks can be very helpful for memorizing facts, concepts, or processes, as long as they are easy to remember and make sense to you. Some examples of mnemonics and learning tricks are:

- Acronyms: using the first letter of each word in a list or phrase to form a new word, such as ROYGBIV for the colors of the rainbow, or PEMDAS for the order of operations in math.
- Acrostics: using the first letter of each word in a list or phrase to form a new sentence, such as Every Good Boy Deserves Fudge for the notes on the treble clef, or My Very Eager Mother Just Served Us Nine Pizzas for the order of the planets.
- Rhymes: using words that sound alike to help you remember something, such as Thirty days hath September, April, June, and November, or In fourteen hundred ninety-two, Columbus sailed the ocean blue.
- Chunking: breaking down a large amount of information into smaller, more manageable units, such as grouping digits in a phone number or a social security number, or dividing a long word into syllables.
- Visualization: creating a mental image or a story that connects the information you want to remember, such as imagining a giant spider web to remember the parts of a web page, or picturing a fish in a tree to remember that the word "gill" means both a breathing organ and a unit of measurement.

Do you have a specific topic or subject that you want to learn more about? I can help you find some mnemonics and learning tricks that are relevant and easy to remember.