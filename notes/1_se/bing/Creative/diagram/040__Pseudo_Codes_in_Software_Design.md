Pseudo codes are a way of writing programs in a human-readable form that does not follow the syntax of any specific programming language. They are used to describe the logic and steps of an algorithm without worrying about the technical details. Pseudo codes can be translated into any programming language later.

Pseudo codes use some common keywords and constructs to represent the control flow of the algorithm, such as SEQUENCE, CASE, WHILE, REPEAT-UNTIL, FOR, and IF-THEN-ELSE. They can also use other keywords or commands depending on the application or domain.

There is no standard way of drawing a diagram for pseudo codes, but one possible way is to use a flowchart. A flowchart is a graphical representation of the steps and decisions in an algorithm using symbols and arrows. Each symbol has a specific meaning and function. For example, a rectangle represents a process or an action, a diamond represents a condition or a decision, an oval represents the start or end of the algorithm, and so on.

The following diagram illustrates the basic architecture of a pseudo code using a flowchart:

```
+-----------------+
| Start           |
+-----------------+
        |
        v
+-----------------+
| Declare x, y, z |
+-----------------+
        |
        v
+-----------------+
| Read x and y    |
+-----------------+
        |
        v
+-----------------+
| z = x + y       |
+-----------------+
        |
        v
+-----------------+
| Print z         |
+-----------------+
        |
        v
+-----------------+
| End             |
+-----------------+
```

This pseudo code is a simple example of adding two numbers and printing the result. It can be written in any programming language using the appropriate syntax and data types. For example, in Python, it can be written as:

```python
# Declare x, y, z
x = 0
y = 0
z = 0

# Read x and y
x = int(input("Enter x: "))
y = int(input("Enter y: "))

# z = x + y
z = x + y

# Print z
print("z =", z)
```