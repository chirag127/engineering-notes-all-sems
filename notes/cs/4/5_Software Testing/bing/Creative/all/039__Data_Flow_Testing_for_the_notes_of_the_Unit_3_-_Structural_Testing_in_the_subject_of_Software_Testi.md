### Data Flow Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Data flow testing is a type of white-box testing technique that examines the data flow with respect to the variables used in the code .
- It checks the initialization, definition, and usage of variables and their values at each point in the program .
- It makes use of the control flow graph to identify the possible paths that involve the variables of interest  .
- It aims to cover the gap between path testing and branch testing by testing the data dependencies between statements.
- It can detect errors such as uninitialized variables, dead code, and incorrect variable values .

#### Steps of Data Flow Testing

- Create a data flow graph from the source code that shows the definition, usage, and kill points of variables  .
- Select a testing criterion such as all-defs, all-uses, all-du-paths, etc. that defines the coverage goal  .
- Identify the paths in the data flow graph that satisfy the testing criterion  .
- Derive test input data that can execute the selected paths and check the expected output  .

#### Example of Data Flow Testing

Consider the following pseudocode:

```
1. x = 1
2. if x > 0 then
3.   a = x + 1
4. else
5.   while x <= 0 do
6.     x = x + 1
7.   a = x + 1
8. print a
```

The data flow graph for this code is:

```
    1
    |
    2
   / \
  3   4
   \ /
    5
    |
    6
    |
    7
    |
    8
```

The nodes represent the statements and the edges represent the control flow. The definition and usage points of the variables x and a are marked with d and u respectively.

The testing criterion can be all-defs, which means that every definition of a variable must be covered by at least one path. The paths that satisfy this criterion are:

- 1(d x) - 2 - 3(d a) - 8(u a)
- 1(d x) - 2 - 4 - 5 - 6(d x) - 7(d a) - 8(u a)

The test input data that can execute these paths are:

- x = 1 for the first path
- x = -1 for the second path

The expected output for both paths is a = 2.