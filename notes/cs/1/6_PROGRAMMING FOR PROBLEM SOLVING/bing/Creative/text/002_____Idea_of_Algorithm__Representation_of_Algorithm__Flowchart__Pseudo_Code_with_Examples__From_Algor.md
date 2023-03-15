### Idea of Algorithm: Representation of Algorithm, Flowchart, Pseudo Code with Examples, From Algorithms to Programs, Source Code

- An algorithm is a set of instructions or rules that can be followed to solve a problem or perform a computation     .
- An algorithm can be represented in different ways, such as:
  - Flowchart: A graphical representation of an algorithm using symbols and arrows to show the sequence of steps and the logic of the algorithm . For example, the following flowchart shows an algorithm to find the maximum of three numbers:

  ```
  Start
  |
  V
  Input A, B, C
  |
  V
  If A > B and A > C then
  |                  |
  | Yes              | No
  V                  V
  Max = A            If B > C then
  |                  |              |
  |                  | Yes          | No
  V                  V              V
  Output Max         Max = B        Max = C
  |                  |              |
  |                  |              |
  V                  V              V
  Stop               Output Max     Output Max
                     |              |
                     |              |
                     V              V
                     Stop           Stop
  ```

  - Pseudo code: A textual representation of an algorithm using natural language and some programming conventions to describe the steps and the logic of the algorithm . For example, the following pseudo code shows an algorithm to find the maximum of three numbers:

  ```
  START
  INPUT A, B, C
  IF A > B AND A > C THEN
    SET Max TO A
  ELSE
    IF B > C THEN
      SET Max TO B
    ELSE
      SET Max TO C
    END IF
  END IF
  OUTPUT Max
  STOP
  ```

- An algorithm can be converted into a program, which is a set of instructions that can be executed by a computer .
- A program is written in a programming language, which is a formal language that defines the syntax and semantics of the program .
- A source code is the text representation of a program in a programming language .
- A source code can be compiled or interpreted, which are two ways of translating the source code into a machine code that can be executed by the computer .