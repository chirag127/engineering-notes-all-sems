### Idea of Algorithm: Representation of Algorithm, Flowchart, Pseudo Code with Examples, From Algorithms to Programs, Source Code

An algorithm is a step-by-step procedure to solve a problem. It is a finite sequence of well-defined, computer-implementable instructions, typically to solve a class of problems or to perform a computation.

#### Representation of Algorithm
There are several ways to represent an algorithm, including:
1. **Natural language:** Describing the algorithm in a human language, such as English.
2. **Flowchart:** A graphical representation of the algorithm using symbols and arrows to show the flow of control.
3. **Pseudo code:** A high-level description of the algorithm using a combination of natural language and programming language constructs.

#### Flowchart
A flowchart is a type of diagram that represents an algorithm, workflow, or process. It shows the steps as boxes of various kinds, and their order by connecting them with arrows. Flowcharts are used in analyzing, designing, documenting, or managing a process or program in various fields.

#### Pseudo Code
Pseudo code is an informal high-level description of the operating principle of a computer program or other algorithm. It uses the structural conventions of a normal programming language, but is intended for human reading rather than machine reading. Pseudo code typically omits details that are essential for machine understanding of the algorithm, such as variable declarations.

#### Examples
Here is an example of an algorithm to find the largest number in a list, represented in natural language, flowchart, and pseudo code:

**Natural language:**
1. Set the first number in the list as the largest number.
2. Compare the next number in the list with the current largest number.
3. If the next number is larger, set it as the new largest number.
4. Repeat step 2 and 3 until all numbers in the list have been compared.
5. The largest number is the result.

**Flowchart:**
```
  +----------------+
  | Set first      |
  | number as max  |
  +-------+--------+
          |
          v
  +-------+--------+
  | Compare next   |
  | number with max|
  +-------+--------+
          |
          v
  +-------+--------+
  | If next > max  |
  | set next as max|
  +-------+--------+
          |
          v
  +-------+--------+
  | Repeat until   |
  | end of list    |
  +-------+--------+
          |
          v
  +-------+--------+
  | Max is result  |
  +----------------+
```

**Pseudo code:**
```
SET max = list[0]
FOR i = 1 to length(list) - 1
    IF list[i] > max THEN
        SET max = list[i]
    ENDIF
ENDFOR
RETURN max
```

#### From Algorithms to Programs
An algorithm is a conceptual idea, while a program is a concrete implementation of the algorithm in a specific programming language. To convert an algorithm into a program, the algorithm must be translated into a programming language, which can then be compiled or interpreted to produce an executable program.

#### Source Code
The source code is the text representation of a program written in a programming language. It contains the instructions that are executed by the computer to perform the desired task. The source code is typically stored in a text file and can be edited using a text editor or an integrated development environment (IDE). The source code must be compiled or interpreted to produce an executable program.