### Idea of Algorithm: Representation of Algorithm, Flowchart, Pseudo Code with Examples, From Algorithms to Programs, Source Code

- An algorithm is a set of instructions or rules that can be followed to solve a problem or perform a computation     .
- An algorithm can be represented in different ways, such as:
  - Flowchart: A graphical representation of an algorithm using symbols and arrows to show the flow of control and data . For example, a flowchart for finding the maximum of three numbers is:

  ```
  Start
  |
  V
  Input a, b, c
  |
  V
  max = a
  |
  V
  Is b > max?
  |       |
  No      Yes
  |       |
  V       V
  Is c > max?  max = b
  |       |    |
  No      Yes  V
  |       |    Is c > max?
  V       V    |       |
  Output max   No      Yes
  |       |    |       |
  V       V    V       V
  Stop    max = c      max = c
          |             |
          V             V
          Output max    Output max
          |             |
          V             V
          Stop          Stop
  ```

  - Pseudo code: A textual representation of an algorithm using natural language and some programming conventions to describe the logic and steps of an algorithm . For example, a pseudo code for finding the maximum of three numbers is:

  ```
  START
  INPUT a, b, c
  SET max TO a
  IF b > max THEN
    SET max TO b
  END IF
  IF c > max THEN
    SET max TO c
  END IF
  OUTPUT max
  STOP
  ```

  - From algorithms to programs: A program is an implementation of an algorithm in a specific programming language that can be executed by a computer . For example, a program for finding the maximum of three numbers in Python is:

  ```python
  # Start
  # Input a, b, c
  a = int(input("Enter a: "))
  b = int(input("Enter b: "))
  c = int(input("Enter c: "))
  # Set max to a
  max = a
  # If b > max then
  if b > max:
    # Set max to b
    max = b
  # End if
  # If c > max then
  if c > max:
    # Set max to c
    max = c
  # End if
  # Output max
  print("The maximum is", max)
  # Stop
  ```

  - Source code: The source code is the text of a program written in a programming language that can be read and edited by humans . For example, the source code of the program above is:

  ```python
  # Start
  # Input a, b, c
  a = int(input("Enter a: "))
  b = int(input("Enter b: "))
  c = int(input("Enter c: "))
  # Set max to a
  max = a
  # If b > max then
  if b > max:
    # Set max to b
    max = b
  # End if
  # If c > max then
  if c > max:
    # Set max to c
    max = c
  # End if
  # Output max
  print("The maximum is", max)
  # Stop
  ```