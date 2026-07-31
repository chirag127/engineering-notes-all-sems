# K Map Minimization upto 6 Variables

- Karnaugh map or K-map is a map of a function used in a technique used for minimization or simplification of a Boolean expression.
- It results in less number of logic gates and inputs to be used during the fabrication.
- K-map is a graphical representation of a truth table, where each cell corresponds to a minterm or a maxterm of the function.
- The cells are arranged in such a way that adjacent cells differ by only one bit position.
- The cells are also labeled with a binary address code that indicates the values of the variables for that cell.
- The main steps of K-map minimization are:
  - Identify all the essential prime implicants of the function, which are the largest groups of 1s (for SOP) or 0s (for POS) that cover at least one minterm or maxterm that is not covered by any other group.
  - Select the minimum number of essential prime implicants that cover all the minterms or maxterms of the function.
  - Write the simplified expression by taking the OR (for SOP) or AND (for POS) of the essential prime implicants.
- K-map of 2 to 4 variables is very easy. However, 5 and 6 variable K-map is a little bit complex.
- For 5 variable K-map, there are 2^5 = 32 cells, which can be arranged in a 4x8 or 8x4 matrix.
- The fifth variable is represented by two submaps, one for its value being 0 and the other for its value being 1.
- The cells in each submap are labeled with a 4-bit address code that follows the Gray code sequence.
- The cells in the same position in both submaps are considered adjacent and can be grouped together.
- For 6 variable K-map, there are 2^6 = 64 cells, which can be arranged in a 8x8 or 16x4 matrix.
- The sixth variable is represented by four submaps, one for each combination of its value and the value of the fifth variable.
- The cells in each submap are labeled with a 4-bit address code that follows the Gray code sequence.
- The cells in the same position in all four submaps are considered adjacent and can be grouped together.
- The cells in the same position in two adjacent submaps are also considered adjacent and can be grouped together.
- The cells in the corners of each submap are also considered adjacent and can be grouped together.
- The cells in the corners of the whole map are also considered adjacent and can be grouped together.
- The following diagrams show the 5 and 6 variable K-maps with the cell labels and the adjacency rules :

![5 variable K-map](https://www.electricaltechnology.org/wp-content/uploads/2018/05/5-variable-k-map.png)

![6 variable K-map](https://www.allaboutcircuits.com/uploads/articles/6-variable-k-map.jpg)

- The following example shows how to simplify a 6 variable function using K-map:

![6 variable K-map example](https://www.allaboutcircuits.com/uploads/articles/6-variable-k-map-example.jpg)

- The simplified expression is:

F = A'B'C'D' + A'BCD + AB'C'D + ABCD' + EF