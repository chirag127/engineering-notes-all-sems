### Idea of Algorithm: Representation of Algorithm, Flowchart, Pseudo Code with Examples, From Algorithms to Programs, Source Code

- An algorithm is a set of instructions or rules that can be followed to solve a problem or perform a computation     .
- An algorithm can be represented in different ways, such as flowcharts, pseudo code, natural language, or formal languages.
- A flowchart is a graphical representation of an algorithm that uses symbols and arrows to show the steps and the order of execution .
- A pseudo code is a textual representation of an algorithm that uses a simplified syntax and keywords to describe the logic and the actions of the algorithm .
- An example of a flowchart and a pseudo code for finding the maximum of three numbers is shown below:

![flowchart](https://i.imgur.com/4Zw0fZa.png)

```
BEGIN
  INPUT a, b, c
  IF a > b THEN
    max = a
  ELSE
    max = b
  ENDIF
  IF c > max THEN
    max = c
  ENDIF
  OUTPUT max
END
```

- An algorithm can be translated into a program, which is a set of instructions that can be executed by a computer .
- A program is written in a programming language, which is a formal language that has a specific syntax and semantics .
- A source code is the text of a program written in a programming language .
- An example of a source code for finding the maximum of three numbers in Python is shown below:

```python
# This is a comment
# Input three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Find the maximum of the three numbers
if a > b:
  max = a
else:
  max = b
if c > max:
  max = c

# Output the maximum
print("The maximum is", max)
```