### Identification of Independent Paths

- Independent paths are paths in a program that execute a new set of statements or conditions that have not been executed before by any other paths  .
- Independent paths can be identified by using a control flow graph, which is a graphical representation of the program that shows the nodes (statements or blocks) and the edges (transitions or branches) between them .
- Independent paths can be calculated by using the cyclomatic complexity, which is a metric that measures the number of linearly independent paths in a control flow graph   .
- Cyclomatic complexity can be computed by using any of the following formulas  :
  - Cyclomatic complexity = Edges - Nodes + 2
  - Cyclomatic complexity = Regions + 1
  - Cyclomatic complexity = Decisions + 1
- Independent paths can be used to design test cases that cover all the possible paths in a program, which can improve the code coverage and reduce the risk of errors .