# Karnaugh maps

- A Karnaugh map (K-map) is a method of simplifying Boolean algebra expressions .
- It is a visual method that uses a grid of cells to represent all the possible combinations of input variables and their corresponding output values.
- It helps to determine the minimum expressions of Product Of Sum (POS) and Sum Of Products (SOP) forms, which can be implemented using a minimum number of logic gates .
- It also helps to detect and eliminate race conditions, which are situations where the output of a logic circuit depends on the order or timing of the input changes.

## Working of K-map

- To use a K-map, the following steps are followed:
  - Select a K-map according to the number of input variables. For example, a 2-variable K-map has 4 cells, a 3-variable K-map has 8 cells, and a 4-variable K-map has 16 cells.
  - Fill the grid of the K-map with 0's and 1's according to the given Boolean expression or truth table. Each cell corresponds to a minterm (a product term with all the input variables) or a maxterm (a sum term with all the input variables).
  - Group the adjacent cells that have the same output value (either 0 or 1) into regions of size 1, 2, 4, 8, or 16. The regions can wrap around the edges of the K-map. The regions should be as large as possible and should not overlap.
  - Write the simplified Boolean expression for each region by eliminating the variables that change within the region. For example, if a region has cells with values AB, AB', A'B, and A'B', then the simplified expression for that region is 1, since the variables A and B change within the region. The final expression is the sum of the expressions for each region (for SOP form) or the product of the expressions for each region (for POS form).

## Rules of K-map

- The following rules are applied when using a K-map:
  - The cells of the K-map are labeled in such a way that only one variable changes between adjacent cells. This is done by using a Gray code sequence, which is a binary code where only one bit changes between successive values.
  - The regions of the K-map should be rectangular and should contain a power of 2 number of cells. The regions can be horizontal, vertical, or both, but they should not be diagonal.
  - The regions of the K-map should be as large as possible, since larger regions mean fewer variables in the simplified expression. The regions should cover all the cells with the same output value (either 0 or 1).
  - The regions of the K-map can overlap if it leads to a simpler expression. However, the same cell should not be counted more than once in the final expression.
  - The regions of the K-map can wrap around the edges of the K-map, since the K-map is considered to be a torus (a doughnut-shaped surface).

## Example Problems

- Here are some example problems of using K-maps to simplify Boolean expressions:

### Example 1

- Given the following Boolean expression, simplify it using a K-map:

  - F(A, B, C) = A'B'C + A'BC + AB'C + ABC

- Solution:

  - Step 1: Select a 3-variable K-map with 8 cells and label them with the Gray code sequence.

  | C\AB | 00 | 01 | 11 | 10 |
  | ---- | -- | -- | -- | -- |
  | 0    |    |    |    |    |
  | 1    |    |    |    |    |

  - Step 2: Fill the grid of the K-map with 0's and 1's according to the given expression. Each term in the expression corresponds to a cell with value 1.

  | C\AB | 00 | 01 | 11 | 10 |
  | ---- | -- | -- | -- | -- |
  | 0    | 1  | 1  | 1  | 0  |
  | 1    | 1  | 0  | 1  | 0  |

  - Step 3: Group the adjacent cells that have the same output value (1)