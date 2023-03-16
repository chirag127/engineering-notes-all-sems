### Cyclomatic Complexity

- Cyclomatic complexity is a software metric used to indicate the complexity of a program or a function.
- It is a quantitative measure of the number of linearly independent paths through a program's source code .
- It is calculated by developing a control flow graph of the code that measures the number of edges, nodes and connected components .
- It can be used to estimate the number of test cases required to cover all the possible paths of the program.
- It can also be used to identify the potential risk of errors or defects in the code.

#### Formula

- The cyclomatic complexity can be computed using the following formula  :

  - Cyclomatic complexity = E – N + 2*P

  - where,

    - E = represents the number of edges in the control flow graph.
    - N = represents the number of nodes in the control flow graph.
    - P = represents the number of connected components in the control flow graph.

#### Example

- Consider the following pseudocode:

  ```
  function max(a, b)
    if a > b then
      return a
    else
      return b
    end if
  end function
  ```

- The control flow graph for this code is:

  ```
  +-----+     +-----+     +-----+
  |  a  | --> | a>b | --> |  a  |
  +-----+     +-----+     +-----+
                |  |
                |  v
                | +-----+
                +>|  b  |
                  +-----+
  ```

- The cyclomatic complexity for this code is:

  - E = 4
  - N = 4
  - P = 1
  - Cyclomatic complexity = 4 - 4 + 2*1 = 2

- This means that there are two linearly independent paths in this code:

  - Path 1: a > b -> return a
  - Path 2: a <= b -> return b

- Therefore, two test cases are required to cover all the possible paths of this code.