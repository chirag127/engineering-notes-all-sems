### K Map Minimization upto 6 Variables

Karnaugh map or K-map is a graphical technique used for minimization or simplification of a Boolean expression. It results in less number of logic gates and inputs to be used during the fabrication.

A K-map consists of cells (squares) that represent the minterms of a Boolean function. Each cell is labeled with a binary code that corresponds to the values of the input variables. The number of cells in a K-map is equal to 2^n, where n is the number of input variables.

The main idea of K-map minimization is to group the adjacent cells that have the same output value (either 1 or 0) and eliminate the redundant variables from the expression. A group can have 1, 2, 4, 8, 16, or 32 cells, and must be a power of 2. The groups can wrap around the edges of the map, and can overlap with each other. The larger the group, the simpler the expression.

The steps for K-map minimization are:

- Draw a K-map with the number of cells corresponding to the number of input variables.
- Mark the cells with 1s and 0s according to the output values of the function. If the function has don't care conditions, mark them with Xs.
- Identify the prime implicants, which are the largest possible groups of adjacent cells with the same value. Circle them with different colors or shapes.
- Find the essential prime implicants, which are the prime implicants that cover at least one cell that is not covered by any other prime implicant. These are the mandatory terms in the simplified expression.
- Select the minimum number of remaining prime implicants that cover all the cells with 1s (or 0s, if the function is in canonical product of sums form). Use a table or a chart to find the optimal combination.
- Write the simplified expression by ORing the terms corresponding to the selected prime implicants. Each term is obtained by ANDing the variables that are common to all the cells in the group. If a variable changes its value within the group, it is eliminated.

The following are some examples of K-map minimization for different number of variables.

#### 2 Variable K-Map

2 variables have 2^n = 2^2 = 4 minterms. Therefore there are 4 cells in 2 variable K-map for each minterm.

The K-map for a 2 variable function F(A,B) is shown below.

| A\B | 0 | 1 |
| --- | --- | --- |
| 0 | F(0,0) | F(0,1) |
| 1 | F(1,0) | F(1,1) |

For example, if F(A,B) = A + B, the K-map is:

| A\B | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | 1 |
| 1 | 1 | 1 |

The simplified expression is F(A,B) = A + B, which is obtained by grouping the cells with 1s as shown below.

| A\B | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | <span style="color:red">1</span> |
| 1 | <span style="color:red">1</span> | <span style="color:red">1</span> |

The red group corresponds to the term A, and the blue group corresponds to the term B.

#### 3 Variable K-Map

3 variables have 2^n = 2^3 = 8 minterms. Therefore there are 8 cells in 3 variable K-map for each minterm.

The K-map for a 3 variable function F(A,B,C) is shown below.

| A\BC | 00 | 01 | 11 | 10 |
| --- | --- | --- | --- | --- |
| 0 | F(0,0,0) | F(0,0,1) | F(0,1,1) | F(0,1,0) |
| 1 | F(1,0,0) | F(1,0,1) | F(1,1,1) | F(1,1,0) |

For example, if F(A,B,C) = A'BC + AB'C + ABC, the K-map is:

|