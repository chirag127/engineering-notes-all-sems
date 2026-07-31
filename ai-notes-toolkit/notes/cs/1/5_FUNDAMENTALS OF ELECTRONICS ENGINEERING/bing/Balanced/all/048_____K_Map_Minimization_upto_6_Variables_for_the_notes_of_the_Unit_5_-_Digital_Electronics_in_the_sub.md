# K Map Minimization upto 6 Variables

- Karnaugh map or K-map is a map of a function used in a technique used for minimization or simplification of a Boolean expression. It results in less number of logic gates and inputs to be used during the fabrication.
- K-map is a graphical representation of a truth table. Each cell in the map corresponds to a minterm or a maxterm of the function. The cells are arranged in such a way that adjacent cells differ by only one bit in their binary address.
- The main idea of K-map minimization is to group the adjacent cells that have the same output value (either 1 or 0) and eliminate the redundant variables from the expression. The groups can be of size 1, 2, 4, 8, 16, or 32, and they must be a power of 2. The groups can also wrap around the edges of the map.
- The simplified expression can be obtained by writing the common variables of each group in either sum of products (SOP) or product of sums (POS) form. The groups with output value 1 are called prime implicants, and the groups that are essential to cover all the 1s are called essential prime implicants. The groups with output value 0 are called prime implicates, and the groups that are essential to cover all the 0s are called essential prime implicates.
- K-map of 2 to 4 variables is very easy. However, 5 and 6 variable K-map is a little bit complex. We will discuss one by one in details.

## 5 Variable K-Map

- 5 variables have 2^5 = 32 minterms. Therefore there are 32 cells in 5 variable K-map for each minterm.
- A 5 variable K-map can be formed by using two 4 variable K-maps. One K-map is for the minterms with the fifth variable equal to 0, and the other K-map is for the minterms with the fifth variable equal to 1. The two K-maps are placed side by side, and the common edges are overlapped to form a single map.
- The grouping of the cells is done in the same way as in 4 variable K-map, but the groups can span across the two K-maps. The simplified expression is obtained by writing the common variables of each group, and including the fifth variable if the group is in only one K-map.
- For example, consider the following 5 variable function:

  F(A, B, C, D, E) = ∑(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 24, 25, 26, 27, 28, 29, 30, 31)

- The 5 variable K-map for this function is shown below:

  ![5 variable K-map](https://i.imgur.com/8Qjw0wD.png)

- The groups are marked with different colors and letters. The simplified expression is:

  F(A, B, C, D, E) = A' + B' + C' + D' + E' + ABE + ACE + ADE + BCD + BDE + CDE

## 6 Variable K-Map

- 6 variables have 2^6 = 64 minterms. Therefore there are 64 cells in 6 variable K-map for each minterm.
- A 6 variable K-map can be formed by using four 4 variable K-maps. Two K-maps are for the minterms with the sixth variable equal to 0, and the other two K-maps are for the minterms with the sixth variable equal to 1. The four K-maps are arranged in a square, and the common edges are overlapped to form a single map.
- The grouping of the cells is done in the same way as in 4 variable K-map, but the groups can span across the four K-maps. The simplified expression is obtained by writing the common variables of each group, and including the fifth and sixth variables if the group is in only one or two K-maps.
- For example, consider the following 6 variable function:

  F(A, B, C, D, E, F) = ∑