### Karnaugh maps

- A Karnaugh map (K-map) is a method of simplifying Boolean algebra expressions   .
- It is a graphical representation of a truth table, where each cell corresponds to a combination of input variables and the output variable  .
- It is based on the principle of adjacency, which states that two minterms or maxterms are adjacent if they differ by only one variable .
- It can be used to find the minimum sum-of-products (SOP) or product-of-sums (POS) expression for a given Boolean function  .
- It can also be used to detect and eliminate race conditions in logic circuits.

#### Rules for K-map simplification

- Select a K-map according to the number of input variables. For n variables, use a 2^n-cell K-map.
- Fill the cells with 0s and 1s according to the given minterms or maxterms. Use a gray code order to label the rows and columns .
- Group the adjacent 1s (for SOP) or 0s (for POS) in the K-map. The groups can be of size 1, 2, 4, 8, or 16, and can wrap around the edges of the K-map  .
- Make the groups as large as possible, and avoid overlapping groups. Use only the necessary groups to cover all the 1s (for SOP) or 0s (for POS)  .
- Write the Boolean expression for each group by taking the common variables of the cells in the group. Use OR to combine the groups for SOP, and use AND to combine the groups for POS  .

#### Example of K-map simplification

- Given the Boolean function F(A, B, C, D) = Σ(0, 1, 2, 5, 8, 9, 10, 13, 15), find the minimum SOP expression using a K-map.
- The K-map for this function is:

|   | 00 | 01 | 11 | 10 |
|---|----|----|----|----|
| 00| 1  | 1  | 0  | 1  |
| 01| 0  | 1  | 1  | 0  |
| 11| 0  | 0  | 1  | 1  |
| 10| 1  | 1  | 0  | 1  |

- The groups for this K-map are:

|   | 00 | 01 | 11 | 10 |
|---|----|----|----|----|
| 00| 1  | 1  | 0  | 1  |
| 01| 0  | 1  | 1  | 0  |
| 11| 0  | 0  | 1  | 1  |
| 10| 1  | 1  | 0  | 1  |

| Group | Color | Expression |
|-------|-------|------------|
| G1    | Red   | A'B'       |
| G2    | Blue  | B'C'       |
| G3    | Green | CD         |
| G4    | Yellow| A'D        |

- The minimum SOP expression for this function is:

F(A, B, C, D) = A'B' + B'C' + CD + A'D