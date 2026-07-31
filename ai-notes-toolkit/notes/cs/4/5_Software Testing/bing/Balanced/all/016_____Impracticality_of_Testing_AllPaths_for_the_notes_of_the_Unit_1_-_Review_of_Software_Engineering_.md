### Impracticality of Testing All Paths

- Testing all paths of a software system is impractical because the number of paths grows exponentially with the size and complexity of the system.
- A path is a sequence of statements or decisions executed by the system from a starting point to an ending point.
- The number of paths in a system can be estimated by the cyclomatic complexity, which is a measure of the number of independent paths in the system.
- The cyclomatic complexity can be calculated by the formula: `V(G) = E - N + 2P`, where `E` is the number of edges, `N` is the number of nodes, and `P` is the number of connected components in the control flow graph of the system.
- For example, consider the following pseudocode of a simple program that calculates the factorial of a number:

```
function factorial(n):
  if n < 0:
    return -1
  else if n == 0:
    return 1
  else:
    return n * factorial(n-1)
```

- The control flow graph of this program is:

```
  +---+     +---+     +---+
  | n | --> | < | --> | - |
  +---+     +---+     +---+
    |         |         |
    |         |         v
    |         |       +---+     +---+
    |         +-----> | = | --> | 1 |
    |                 +---+     +---+
    |                   |
    |                   v
    |                 +---+     +---+
    +---------------> | * | --> | - |
                      +---+     +---+
                        |         |
                        v         |
                      +---+       |
                      | f | ------+
                      +---+
```

- The cyclomatic complexity of this program is: `V(G) = 9 - 7 + 2 = 4`.
- This means that there are four independent paths in this program, which are:

  - Path 1: `n -> < -> - -> f`
  - Path 2: `n -> < -> = -> 1`
  - Path 3: `n -> < -> = -> * -> - -> f`
  - Path 4: `n -> < -> = -> * -> - -> f -> * -> - -> f -> ...`

- To test all paths, we would need to provide different inputs for each path, such as:

  - Path 1: `n = -1`
  - Path 2: `n = 0`
  - Path 3: `n = 1`
  - Path 4: `n = 2, 3, 4, ...`

- However, this is only a simple program with four paths. For a larger and more complex system, the number of paths can be much higher and impossible to test exhaustively.
- For example, if a system has 20 nodes and 25 edges, its cyclomatic complexity is: `V(G) = 25 - 20 + 2 = 7`.
- This means that there are at least 2^7 = 128 paths in the system, which would require 128 different inputs to test.
- Moreover, some paths may be infeasible or unreachable, meaning that they cannot be executed by any input or they are never executed in normal operation.
- For example, if a system has a path that depends on a condition that is always false, such as `if (1 == 2)`, then that path is infeasible and cannot be tested.
- Therefore, testing all paths of a software system is impractical and inefficient, and other testing techniques should be used to achieve adequate coverage and quality.