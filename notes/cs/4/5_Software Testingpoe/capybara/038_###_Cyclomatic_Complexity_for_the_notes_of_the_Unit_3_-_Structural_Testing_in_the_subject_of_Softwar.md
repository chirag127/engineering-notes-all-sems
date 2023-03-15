### Cyclomatic Complexity for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

Cyclomatic complexity is a software metric that measures the complexity of a program by analyzing the number of linearly independent paths through a program's source code. In simpler terms, it measures the number of decision points or branches in a program.

#### Calculation of Cyclomatic Complexity

The Cyclomatic complexity of a program can be calculated using the following formula:

```
M = E - N + 2
```

Where,
- M = Cyclomatic complexity
- E = Number of edges in the graph
- N = Number of nodes in the graph

The graph used in the formula is called a control flow graph, which represents the flow of control within a program.

#### Mnemonics and Learning Tricks

There are several ways to remember the formula for Cyclomatic complexity. One popular mnemonic is:

"Every Ninja Punches Now"

Where the first letter of each word represents a term in the formula: E, N, P (which is equal to 2).

Another trick is to remember that the formula is derived from Euler's formula for 3D shapes, which is:

```
V - E + F = 2
```

Where,
- V = Number of vertices
- E = Number of edges
- F = Number of faces

By substituting F=1 (since a program has only one entry and exit point), the formula becomes:

```
V - E + 1 = 2
```

Which can be rearranged to get the formula for Cyclomatic complexity:

```
M = E - V + 2
```

#### Advantages of Cyclomatic Complexity

- Cyclomatic complexity is a good indicator of the difficulty of testing a program.
- It helps identify areas of a program that may be prone to errors or bugs.
- It can help in improving the maintainability of a program by identifying complex code that may need refactoring.

#### Disadvantages of Cyclomatic Complexity

- Cyclomatic complexity does not measure the quality of code or its efficiency.
- The formula may not be accurate for some programming languages or situations.
- It may not take into account the complexity of external libraries or APIs used in a program.

#### Examples of Cyclomatic Complexity

Let's take an example of a simple program with two decision points:

```
if x > 0:
    if y > 0:
        print("Both x and y are positive.")
    else:
        print("x is positive but y is not.")
else:
    if y > 0:
        print("y is positive but x is not.")
    else:
        print("Both x and y are non-positive.")
```

The control flow graph for this program would have 4 nodes and 5 edges, resulting in a Cyclomatic complexity of 3.

#### Applications of Cyclomatic Complexity

Cyclomatic complexity is a useful metric for software testing, as it helps in identifying complex and potentially error-prone areas of a program. It can also be used for code review and refactoring to improve the maintainability of a program.