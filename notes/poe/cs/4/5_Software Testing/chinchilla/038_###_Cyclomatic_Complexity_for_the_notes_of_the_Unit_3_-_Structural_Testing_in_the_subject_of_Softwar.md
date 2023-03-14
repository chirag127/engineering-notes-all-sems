### Cyclomatic Complexity for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

Cyclomatic Complexity is a software metric that measures the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code.

The concept of Cyclomatic Complexity was introduced by Thomas McCabe in 1976. It is an important metric in software testing because it helps in determining the number of test cases needed to test a program thoroughly.

#### Calculation of Cyclomatic Complexity:

The Cyclomatic Complexity of a program can be calculated using the following formula:

    M = E - N + 2

Where,
- M: Cyclomatic Complexity
- E: Number of edges in the control flow graph of the program
- N: Number of nodes in the control flow graph of the program

#### Control Flow Graph:

A control flow graph is a graphical representation of the program's control flow. It consists of nodes and edges. Nodes represent the basic blocks of the program, and edges represent the control flow between them.

#### Mnemonics and Learning Tricks:

- One learning trick for remembering the formula for Cyclomatic Complexity is "Eeny, meeny, miny, moe". Each word represents one of the variables in the formula: "E" for edges, "N" for nodes, "M" for Cyclomatic Complexity, and "2" for the constant value.

#### Advantages of Cyclomatic Complexity:

- It helps in identifying complex and risky parts of the program that require more attention and testing.
- It helps in measuring the maintainability and understandability of the program.
- It helps in determining the number of test cases needed to achieve full coverage of the program.

#### Disadvantages of Cyclomatic Complexity:

- It does not take into account the complexity of the data used in the program.
- It does not consider the quality of the code or the efficiency of the program.

#### Examples:

Consider the following code snippet:

```
int a, b, c;
if (a > 0 && b > 0) {
    c = a + b;
    if (c > 10) {
        printf("c is greater than 10");
    }
    else {
        printf("c is less than or equal to 10");
    }
}
```

The control flow graph for this code can be represented as:

```
      (1)
     /   \
   (2)   (3)
    |     |
   (4)   (5)
    \   /
     (6)
```

Here, there are 6 nodes and 7 edges. Using the formula, we can calculate the Cyclomatic Complexity as:

    M = E - N + 2
    M = 7 - 6 + 2
    M = 3

Therefore, the Cyclomatic Complexity of this program is 3.

#### Applications:

Cyclomatic Complexity is widely used in software testing and quality assurance. It helps in identifying potential problems in the software and improving its overall quality. It is also used in code review and maintenance to ensure that the code is maintainable and understandable.