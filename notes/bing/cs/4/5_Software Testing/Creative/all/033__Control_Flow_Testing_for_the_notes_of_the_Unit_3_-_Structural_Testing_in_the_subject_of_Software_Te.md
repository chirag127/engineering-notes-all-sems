### Control Flow Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Control flow testing is a type of software testing that uses the program's control flow as a model.
- Control flow testing is a white box testing technique, which means it requires the knowledge of the internal structure and logic of the program .
- The aim of control flow testing is to determine the execution order of statements or instructions of the program through a control structure, such as loops, branches, and conditions .
- The control structure of a program is used to develop a test case for the program, which covers all the possible paths that can be executed .
- Control flow testing can be performed manually or automatically, as the control flow graph that is used can be made by hand or by using tools.

#### Steps of control flow testing

- The steps of control flow testing are as follows :
  - Draw a control flow graph (CFG) of the program, which is a graphical representation of the program's structure and logic, showing the nodes and edges that correspond to the statements and transitions of the program.
  - Identify the independent paths in the CFG, which are the paths that traverse at least one edge that has not been traversed by any other path.
  - Derive test cases for each independent path, using the input and output values that correspond to the statements and conditions along the path.
  - Execute the test cases and compare the actual results with the expected results.

#### Advantages of control flow testing

- Some of the advantages of control flow testing are :
  - It detects almost half of the defects that are determined during the unit testing.
  - It also determines almost one-third of the defects of the whole program.
  - It can improve the quality and reliability of the program by ensuring that all the possible paths are tested.
  - It can help in debugging and maintenance of the program by identifying the source of errors and anomalies.

#### Disadvantages of control flow testing

- Some of the disadvantages of control flow testing are:
  - It can be time-consuming and complex to draw the CFG and identify the independent paths, especially for large and nested programs.
  - It can be difficult to generate test cases that cover all the paths, especially for paths that have rare or invalid inputs or outputs.
  - It can be redundant and inefficient to test all the paths, as some paths may have similar or trivial functionality or behavior.

#### Example of control flow testing

- Consider the following pseudocode of a program that calculates the factorial of a given number:

```
function factorial(n)
  if n < 0 then
    return -1
  else if n == 0 then
    return 1
  else
    f = 1
    for i = 1 to n do
      f = f * i
    end for
    return f
  end if
end function
```

- The CFG of the program is as follows:

```
  1
 / \
2   3
|   |
4   5
|   |
6   7
|   |
8   9
|  / \
10 11 12
 \ /
  13
```

- The nodes represent the statements and the edges represent the transitions of the program.
- The independent paths in the CFG are:
  - 1-2-13: when n < 0
  - 1-3-4-13: when n == 0
  - 1-3-5-6-7-8-10-13: when n > 0 and i == n
  - 1-3-5-6-7-9-11-6-7-8-10-13: when n > 0 and i < n
  - 1-3-5-6-7-9-12-6-7-8-10-13: when n > 0 and i > n
- The test cases for each independent path are:
  - Path 1-2-13: n = -1, expected output = -1
  - Path 1-3-4-13: n = 0, expected output = 1
  - Path 1-3-5-6-7-8-10-13: n =