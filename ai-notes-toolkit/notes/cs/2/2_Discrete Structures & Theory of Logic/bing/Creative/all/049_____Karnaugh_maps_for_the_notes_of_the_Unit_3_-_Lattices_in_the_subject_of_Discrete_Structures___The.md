# Karnaugh maps

- A Karnaugh map (K-map) is a method of simplifying Boolean algebra expressions .
- It is a visual method that uses a grid of cells to represent all the possible combinations of input variables and their corresponding output values.
- It helps to determine the minimum expressions in the form of sum-of-products (SOP) or product-of-sums (POS) that are equivalent to the given Boolean function .
- It also helps to detect and eliminate race conditions in logic circuits.

## Working of K-maps

- To use a K-map, the following steps are followed:
  - Select a K-map according to the number of input variables. For example, for a two-variable function, a 2x2 K-map is used; for a three-variable function, a 2x4 K-map is used; and for a four-variable function, a 4x4 K-map is used.
  - Identify the minterms or maxterms as given in the problem. A minterm is a product term that contains all the input variables in either complemented or uncomplemented form. A maxterm is a sum term that contains all the input variables in either complemented or uncomplemented form.
  - Fill the grid of the K-map with 0s and 1s according to the minterms or maxterms. For a SOP expression, place 1s for the minterms and 0s for the rest. For a POS expression, place 0s for the maxterms and 1s for the rest.
  - Group the adjacent cells that contain the same value (either 1 or 0) in the largest possible power of two (such as 1, 2, 4, 8, etc.). The groups can wrap around the edges of the K-map. Each group represents a simplified term in the final expression.
  - Write the simplified expression by combining the common variables in each group. For a SOP expression, use OR operation to join the terms. For a POS expression, use AND operation to join the terms.

## Rules of K-maps

- The following rules should be followed while using K-maps:
  - The groups should be as large as possible, but they should not contain any cell with a different value.
  - The groups should be rectangular in shape and the number of cells in each group should be a power of two.
  - The groups can overlap with each other, but the overlapping cells should not be counted twice in the final expression.
  - The groups can be formed horizontally, vertically, or diagonally, but they should not break the continuity of the K-map.
  - The groups should cover all the cells with 1s for a SOP expression and all the cells with 0s for a POS expression.

## Example Problems

- Consider the following Boolean function:

  F(A, B, C) = ∑(0, 2, 4, 5, 6)

  This is a SOP expression with three input variables and five minterms.

- To simplify this function using a K-map, we follow these steps:

  - Select a 2x4 K-map for three input variables A, B, and C. Label the rows with A and the columns with BC.
  - Fill the K-map with 1s for the minterms and 0s for the rest. The minterms are 0, 2, 4, 5, and 6, which correspond to the binary values 000, 010, 100, 101, and 110 respectively.
  - Group the adjacent cells with 1s in the largest possible power of two. In this case, we can form two groups of four cells each, as shown below.

  | A\BC | 00 | 01 | 11 | 10 |
  | ---- | -- | -- | -- | -- |
  | 0    | 1  | 0  | 0  | 1  |
  | 1    | 1  | 1  | 0  | 1  |

  The groups are marked with different colors.

  - Write the simplified expression by combining the common variables in each group. For the red group, the common variable is A'. For the blue group, the common variable is B'. The final expression is:

  F(A, B, C) = A' + B'