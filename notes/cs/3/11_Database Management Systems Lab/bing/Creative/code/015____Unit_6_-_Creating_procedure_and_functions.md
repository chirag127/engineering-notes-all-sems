Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 6 - Creating procedure and functions.

## Unit 6 - Creating procedure and functions

- A procedure is a set of statements that performs a specific task or action. A function is a set of statements that returns a value or a result.
- Procedures and functions are useful for modularizing and reusing code, improving readability and maintainability, and avoiding repetition and errors.
- In most programming languages, procedures and functions are defined by using a keyword, a name, a list of parameters, and a body of statements. For example, in Python, a procedure can be defined as:

```python
def greet(name): # def is the keyword, greet is the name, name is the parameter
  print("Hello, " + name) # print is the statement in the body
```

- A function can be defined as:

```python
def square(x): # def is the keyword, square is the name, x is the parameter
  return x * x # return is the statement in the body that returns a value
```

- To call a procedure or a function, we use its name and pass the arguments that match the parameters. For example, to call the greet procedure, we can write:

```python
greet("Alice") # Alice is the argument that matches the name parameter
```

- To call the square function, we can write:

```python
y = square(5) # 5 is the argument that matches the x parameter, y is the variable that stores the returned value
```

- Some procedures and functions can have multiple parameters and arguments, or no parameters and arguments at all. For example, a procedure that prints a blank line can be defined as:

```python
def newline(): # no parameters
  print() # print a blank line
```

- A function that returns the current date can be defined as:

```python
def today(): # no parameters
  import datetime # import a module that handles dates and times
  return datetime.date.today() # return the current date
```

- Some procedures and functions can have optional parameters and arguments, or default values for some parameters. For example, a procedure that prints a message with a given number of times can be defined as:

```python
def repeat(message, times = 1): # times is an optional parameter with a default value of 1
  for i in range(times): # use a loop to repeat the message
    print(message)
```

- A function that calculates the area of a rectangle with a given length and width can be defined as:

```python
def area(length, width = length): # width is an optional parameter with a default value of length
  return length * width # return the area
```

- To call a procedure or a function with optional parameters, we can either specify the arguments for all the parameters, or omit some arguments and use the default values. For example, to call the repeat procedure, we can write:

```python
repeat("Hello") # use the default value of 1 for times
repeat("Bye", 3) # specify the value of 3 for times
```

- To call the area function, we can write:

```python
a = area(4) # use the default value of 4 for width
b = area(4, 5) # specify the value of 5 for width
```

- Some procedures and functions can have variable number of parameters and arguments, or keyword arguments that can be specified in any order. For example, a procedure that prints a formatted string with placeholders can be defined as:

```python
def format(string, *args): # *args is a variable parameter that can take any number of arguments
  print(string.format(*args)) # use the format method of the string object to replace the placeholders with the arguments
```

- A function that calculates the average of a given list of numbers can be defined as:

```python
def average(*numbers): # *numbers is a variable parameter that can take any number of arguments
  if len(numbers) == 0: # check if the list is empty
    return None # return None if there are no numbers
  else:
    return sum(numbers) / len(numbers) # return the sum of the numbers divided by the length of the list
```

- To call a procedure or a function with variable parameters, we can either pass a list of arguments, or use the * operator to unpack a list or a tuple. For example, to call the format procedure, we can write:

```python
format("Hello, {} and {}!", "Alice", "