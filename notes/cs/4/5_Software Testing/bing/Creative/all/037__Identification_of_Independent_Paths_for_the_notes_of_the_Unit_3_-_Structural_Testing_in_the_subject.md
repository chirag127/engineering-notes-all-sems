### Identification of Independent Paths for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Structural testing, also known as white-box testing, is a technique that examines the internal structure and logic of the software code to verify its functionality and quality.
- Structural testing requires the tester to have access to the source code and design documents of the software under test.
- One of the objectives of structural testing is to identify and execute all the independent paths in the software code.
- An independent path is a path that introduces at least one new set of processing statements or a new condition.
- Identifying all the independent paths in the software code helps to measure the test coverage and ensure that all the possible scenarios are tested.
- There are different methods to identify the independent paths in the software code, such as:
  - Control flow graph
  - Cyclomatic complexity
  - Basis path testing
  - Data flow testing

#### Control flow graph

- A control flow graph (CFG) is a graphical representation of the software code that shows the flow of control among the statements and conditions.
- A CFG consists of nodes and edges, where nodes represent the statements or conditions, and edges represent the possible paths of execution.
- A CFG can be constructed by following these steps:
  - Identify the entry and exit points of the software code and label them as start and end nodes.
  - Identify the decision points (such as if, switch, while, for, etc.) and label them as predicate nodes.
  - Identify the statements that are executed sequentially and group them into a single node.
  - Draw the edges between the nodes to show the possible paths of execution.
  - Label the edges with the conditions or values that determine the flow of control.
- For example, consider the following pseudocode:

```
start
read x
if x > 0 then
  y = x + 1
else
  y = x - 1
end if
print y
end
```

- The CFG for this pseudocode is:

```
  start
   |
   v
  read x
   |
   v
 x > 0? ----> y = x - 1
   |               |
   | yes           v
   v               print y
  y = x + 1        |
   |               v
   v              end
  print y
   |
   v
  end
```

#### Cyclomatic complexity

- Cyclomatic complexity (CC) is a metric that measures the complexity of the software code by counting the number of independent paths in the CFG.
- CC can be calculated by using the following formula:

  ```
  CC = E - N + 2P
  ```

  where E is the number of edges, N is the number of nodes, and P is the number of connected components (subgraphs) in the CFG.
- CC can also be calculated by using the following formula:

  ```
  CC = R + 1
  ```

  where R is the number of regions (closed areas) in the CFG.
- CC can also be calculated by using the following formula:

  ```
  CC = D + 1
  ```

  where D is the number of decision points (predicate nodes) in the CFG.
- CC indicates the minimum number of test cases required to cover all the independent paths in the software code.
- CC also indicates the risk and maintainability of the software code. A higher CC means a higher complexity, which may lead to more errors and difficulties in testing and debugging.
- A general guideline for CC is:

  | CC  | Risk level |
  | --- | ---------- |
  | 1-10  | Low risk    |
  | 11-20 | Moderate risk |
  | 21-50 | High risk    |
  | >50   | Very high risk |

- For example, the CC for the CFG shown above is:

  ```
  CC = E - N + 2P
     = 9 - 7 + 2 * 1
     = 4
  ```

  or

  ```
  CC = R + 1
     = 3 + 1
     = 4
  ```

  or

  ```
  CC = D + 1
     = 1 + 1
     = 2
  ```

#### Basis path testing

- Basis path testing is a technique that uses the CC to derive a set of test cases that covers all the independent paths in the software code.
- Basis path testing can be performed by following these steps:
  - Construct the CFG for the software code and calculate the CC.
  - Identify the basis set of paths, which is a set of