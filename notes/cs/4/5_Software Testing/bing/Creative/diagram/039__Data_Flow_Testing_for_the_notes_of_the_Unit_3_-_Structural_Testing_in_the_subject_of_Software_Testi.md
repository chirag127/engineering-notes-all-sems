Data Flow Testing is a type of structural testing that focuses on the data variables and their values in a program. It uses the control flow graph to find the test paths of a program according to the locations of definitions and uses of variables in the program. It also detects anomalies in the data flow, such as variables that are defined but not used, used but not defined, or defined twice before being used .

The following diagram illustrates the basic architecture of a data flow testing process:

```
+-----------------+     +-----------------+     +-----------------+
| Data Flow Graph | --> | Testing Criteria| --> | Path Selection  |
+-----------------+     +-----------------+     +-----------------+
                                                     |
                                                     V
+-----------------+     +-----------------+     +-----------------+
| Path Predicate  | <-- | Test Input      | <-- | Test Execution  |
+-----------------+     +-----------------+     +-----------------+
```

The data flow graph is a representation of the program's control flow with the information about the definitions and uses of variables at each node. The testing criteria are the rules or metrics that determine which paths to select for testing. The path selection is the process of identifying the paths that satisfy the testing criteria. The test input is the data that is fed to the program to execute the selected paths. The test execution is the process of running the program with the test input and observing the output. The path predicate is the logical expression that evaluates to true or false depending on the test input and the path conditions .

### Data Flow Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

To perform data flow testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing, one possible approach is as follows:

- Create a data flow graph for the program or module that is being tested. For example, consider the following program:

```
1. read x, y;
2. if (x>y)
3.   a = x+1
4. else
5.   a = y-1
6. print a;
```

The data flow graph for this program is:

```
    +---+  x, y
    | 1 |<------+
    +---+       |
      |         |
      V         |
    +---+       |
    | 2 |       |
    +---+       |
   /     \      |
  /       \     |
 /         \    |
V           V   |
+---+     +---+ |
| 3 |     | 4 | |
+---+     +---+ |
 \         /    |
  \       /     |
   \     /      |
    V   V       |
   +---+        |
   | 6 |        |
   +---+        |
    |           |
    V           |
    +--------->(a)
```

- Select a testing criterion that is suitable for the program or module. For example, one possible testing criterion is all-uses, which requires that every use of every variable is covered by at least one path from its definition. Another possible testing criterion is all-du-paths, which requires that every definition-use pair of every variable is covered by at least one path .
- Classify the paths that satisfy the testing criterion in the data flow graph. For example, for the all-uses criterion, one possible set of paths is:

```
1-2-3-6
1-2-4-6
```

For the all-du-paths criterion, one possible set of paths is:

```
1-2-3-6
1-2-4-6
1-2-3-2-4-6
1-2-4-2-3-6
```

- Develop path predicate expressions to derive test input. For example, for the path 1-2-3-6, the path predicate expression is:

```
x > y
```

This means that the test input should satisfy the condition that x is greater than y. For example, one possible test input is:

```
x = 5, y = 3
```

- Execute the test input and observe the output. For example, for the test input x = 5, y = 3, the output is:

```
a = 6
```

This means that the program executed the path 1-2-3-6 correctly