### Karnaugh maps

- A Karnaugh map (K-map) is a method of simplifying Boolean algebra expressions .
- It is a visual method that uses a grid of cells to represent all the possible combinations of input variables and their corresponding output values.
- It helps to determine the minimum expressions for a Boolean function in the form of sum-of-products (SOP) or product-of-sums (POS) .
- It also helps to detect and eliminate race conditions in logic circuits.

#### Working of K-maps

- To use a K-map, the following steps are followed:
  - Select a K-map according to the number of input variables. For example, a 2-variable K-map has 4 cells, a 3-variable K-map has 8 cells, and a 4-variable K-map has 16 cells.
  - Label the rows and columns of the K-map with the input variables and their complements in Gray code order. Gray code is a binary code where only one bit changes between adjacent values.
  - Fill the cells of the K-map with the output values of the Boolean function for each combination of input variables. The output values can be either 0 or 1, or don't care (X) if the output is irrelevant for that input combination.
  - Group the adjacent cells that have the same output value (1 for SOP, 0 for POS) into the largest possible power-of-two regions. The regions can wrap around the edges of the K-map and overlap with each other. Each region represents a product term (for SOP) or a sum term (for POS) in the simplified expression.
  - Write the simplified expression by combining the common variables in each region. For example, a region that covers the cells AB, AB', A'B, and A'B' can be simplified as B.

#### Example of K-maps

- Consider the following Boolean function of three variables A, B, and C:

  F(A, B, C) = Σ(0, 2, 4, 5, 6)

  where Σ denotes the SOP form and the numbers in the parentheses are the minterms of the function.

- To simplify this function using a K-map, we follow these steps:

  - We select a 3-variable K-map with 8 cells and label the rows and columns with A, A', B, B', C, and C' in Gray code order.

  - We fill the cells of the K-map with 1 for the minterms of the function and 0 for the rest.

  - We group the adjacent cells that have 1 into the largest possible regions. In this case, we have two regions: one that covers the cells 4 and 5, and another that covers the cells 2 and 6.

  - We write the simplified expression by combining the common variables in each region. The first region has A and C as the common variables, so it can be written as AC. The second region has B' and C as the common variables, so it can be written as B'C. The final expression is the sum of these two terms, which is AC + B'C.

- The K-map and the simplified expression for this example are shown below:

|   | C' | C  |
|---|----|----|
| A | 0  | 1  |
| A'| 1  | 0  |

F(A, B, C) = AC + B'C