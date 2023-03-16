### Identification of Independent Paths

- Independent paths are paths in a program that execute a new set of statements or conditions that have not been executed before by any other path  .
- Independent paths can be identified by using a control flow graph, which is a graphical representation of the program that shows the nodes (statements or blocks) and the edges (transitions or branches) between them .
- Independent paths can be used to measure the cyclomatic complexity of a program, which is the number of independent paths in the program  .
- Cyclomatic complexity can be calculated by using one of the following formulas  :
  - Cyclomatic complexity = Edges - Nodes + 2
  - Cyclomatic complexity = Regions + 1
  - Cyclomatic complexity = Decisions + 1
- Independent paths can be used to design test cases that cover all the possible paths in the program, ensuring that every statement and condition is tested at least once  .
- Independent paths can help to improve the code coverage, reduce the risk, and detect the errors in the program .