### K Map Minimization upto 6 Variables

- Karnaugh map or K-map is a graphical technique used for minimization or simplification of a Boolean expression.
- It results in less number of logic gates and inputs to be used during the fabrication.
- K-map can handle up to 6 variables, but the visualization becomes difficult for 5 and 6 variable K-maps .
- The basic steps for K-map minimization are:
  - Construct a K-map for the given Boolean expression, with one square (cell) for each minterm.
  - Group the adjacent cells containing 1s (called prime implicants) in the K-map, following these rules:
    - The groups must be rectangular and contain 2n cells, where n is an integer.
    - The groups must be as large as possible, covering all the 1s in the K-map.
    - The groups can overlap with each other if necessary.
    - The groups can wrap around the edges of the K-map if necessary.
    - The cells containing don't cares (X) can be included in the groups if they help to make larger groups or to reduce the number of groups.
  - Write the Boolean expression for each group, using the variable values that remain constant within the group.
  - Use the OR operation to combine the expressions for all the groups, obtaining the simplified Boolean expression.

- For 2 to 4 variable K-maps, the cells are arranged in a square or rectangular grid, with the variable values along the rows and columns forming a Gray code sequence .
- For example, a 4 variable K-map has 16 cells, arranged in a 4x4 grid, with the variables A and B along the rows and C and D along the columns, as shown below:

|   | 00 | 01 | 11 | 10 |
|---|----|----|----|----|
| 00| A'B'C'D' | A'B'C'D | A'B'CD | A'B'CD' |
| 01| A'BC'D' | A'BC'D | A'BCD | A'BCD' |
| 11| ABC'D' | ABC'D | ABCD | ABCD' |
| 10| AB'C'D' | AB'C'D | AB'CD | AB'CD' |

- For 5 and 6 variable K-maps, the cells are arranged in multiple 4 variable sub-maps, with the additional variables used to select the sub-map .
- For example, a 5 variable K-map has 32 cells, arranged in four 4x4 sub-maps, with the variables A, B, C and D forming the rows and columns of each sub-map, and the variable E used to select the sub-map, as shown below:

| E=0 | 00 | 01 | 11 | 10 |
|---|----|----|----|----|
| 00| A'B'C'D'E' | A'B'C'DE' | A'B'CDE' | A'B'CD'E' |
| 01| A'BC'D'E' | A'BC'DE' | A'BCDE' | A'BCD'E' |
| 11| ABC'D'E' | ABC'DE' | ABCDE' | ABCD'E' |
| 10| AB'C'D'E' | AB'C'DE' | AB'CDE' | AB'CD'E' |

| E=1 | 00 | 01 | 11 | 10 |
|---|----|----|----|----|
| 00| A'B'C'D'E | A'B'C'DE | A'B'CDE | A'B'CD'E |
| 01| A'BC'D'E | A'BC'DE | A'BCDE | A'BCD'E |
| 11| ABC'D'E | ABC'DE | ABCDE | ABCD'E |
| 10| AB'C'D'E | AB'C'DE | AB'CDE | AB'CD'E |

- A 6 variable K-map has 64 cells, arranged in 16 4x4 sub-maps, with the variables A, B, C and D forming the rows and columns of each sub-map, and the variables E and F used to select the sub-map, as shown below:

| E=0, F=0 | 00