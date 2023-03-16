### Cyclomatic Complexity

- Cyclomatic complexity is a software metric used to indicate the complexity of a program.
- It is a quantitative measure of the number of linearly independent paths through a program's source code.
- It was developed by Thomas J. McCabe, Sr. in 1976.
- It is based on the idea that the more decisions that have to be made in code, the more complex it is .
- It can be used to estimate the minimum number of test cases needed to achieve full branch coverage .
- It can also be used to identify the parts of the code that are more prone to errors and defects.
- It can be calculated using the following formula:

    - `M = E - N + 2P`
    - where `M` is the cyclomatic complexity, `E` is the number of edges in the control flow graph, `N` is the number of nodes in the control flow graph, and `P` is the number of connected components.

- For example, consider the following pseudocode:

    ```
    function foo(x, y) {
      if (x > 0) {
        print("positive")
      } else {
        print("non-positive")
      }
      if (y > 0) {
        print("positive")
      } else {
        print("non-positive")
      }
    }
    ```

- The control flow graph for this function is:

    ```
    +-----+     +-----+     +-----+
    | foo | --> | x>0 | --> | y>0 |
    +-----+     +-----+     +-----+
       |           |           |
       |           |           |
       |           |           |
       |           |           |
       |           |           |
       |           |           |
       |           |           |
       |           |           |
       |           |           |
       |           |           |
       |           |           |
       |           |           |
       |           |           |
    +-----+     +-----+     +-----+
    | end | <-- | end | <-- | end |
    +-----+     +-----+     +-----+
    ```

- The cyclomatic complexity of this function is:

    - `M = E - N + 2P`
    - `M = 8 - 6 + 2 * 1`
    - `M = 4`

- This means that there are four linearly independent paths through the function, and four test cases are needed to cover all branches. The test cases are:

    - `foo(1, 1)` -> prints "positive" twice
    - `foo(1, -1)` -> prints "positive" and "non-positive"
    - `foo(-1, 1)` -> prints "non-positive" and "positive"
    - `foo(-1, -1)` -> prints "non-positive" twice