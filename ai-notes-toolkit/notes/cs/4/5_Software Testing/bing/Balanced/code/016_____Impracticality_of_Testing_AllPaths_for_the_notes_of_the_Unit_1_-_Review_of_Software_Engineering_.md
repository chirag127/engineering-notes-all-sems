### Impracticality of Testing All Paths

- Testing all paths of a software system is impractical because the number of paths grows exponentially with the size and complexity of the system.
- A path is a sequence of statements or decisions executed by the system from a starting point to an ending point.
- The number of paths in a system can be estimated by the cyclomatic complexity, which is a measure of the number of independent paths in the system.
- The cyclomatic complexity can be calculated by the formula `V(G) = E - N + 2P`, where `E` is the number of edges, `N` is the number of nodes, and `P` is the number of connected components in the control flow graph of the system.
- For example, consider the following pseudocode of a simple system:

```
if A then
  B
else
  C
endif
D
```

- The control flow graph of this system is:

```
    A
   / \
  B   C
   \ /
    D
```

- The cyclomatic complexity of this system is `V(G) = 4 - 4 + 2 = 2`, which means there are two independent paths: `A-B-D` and `A-C-D`.
- Testing all paths of this system is feasible, but if we add more statements or conditions, the number of paths will increase rapidly.
- For example, if we add another statement `E` after `D`, the cyclomatic complexity will become `V(G) = 5 - 5 + 2 = 2`, but the number of paths will double to four: `A-B-D-E`, `A-C-D-E`, `A-B-E`, and `A-C-E`.
- If we add another condition `if F then G else H endif` after `E`, the cyclomatic complexity will become `V(G) = 8 - 8 + 2 = 2`, but the number of paths will quadruple to 16: `A-B-D-E-F-G`, `A-B-D-E-F-H`, `A-B-D-F-G`, `A-B-D-F-H`, `A-B-E-F-G`, `A-B-E-F-H`, `A-B-F-G`, `A-B-F-H`, `A-C-D-E-F-G`, `A-C-D-E-F-H`, `A-C-D-F-G`, `A-C-D-F-H`, `A-C-E-F-G`, `A-C-E-F-H`, `A-C-F-G`, and `A-C-F-H`.
- As we can see, testing all paths of a system is impractical because it requires too much time and resources, and it may not be necessary or effective to test every possible path.
- Instead, testing techniques such as equivalence partitioning, boundary value analysis, decision table testing, and path testing can be used to select a subset of paths that cover the most important or critical aspects of the system.