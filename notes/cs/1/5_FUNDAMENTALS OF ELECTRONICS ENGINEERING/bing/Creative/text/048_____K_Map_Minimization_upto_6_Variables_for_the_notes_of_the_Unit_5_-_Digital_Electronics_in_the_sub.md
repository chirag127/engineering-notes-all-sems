### K Map Minimization upto 6 Variables

- Karnaugh map or K-map is a map of a function used in a technique used for minimization or simplification of a Boolean expression.
- It results in less number of logic gates and inputs to be used during the fabrication.
- K-map is a graphical representation of a truth table, where each cell corresponds to a minterm or a maxterm of the function.
- The cells are arranged in such a way that adjacent cells differ by only one bit in their binary address.
- The cells are grouped together to form implicants, which are the simplest product or sum terms of the function.
- The implicants are then combined to form the minimal expression of the function, which is the one with the least number of literals.
- The rules for grouping the cells are as follows:
  - The groups must be rectangular and contain 2^n cells, where n is an integer.
  - The groups must be as large as possible, covering all the 1's (for SOP) or 0's (for POS) of the function.
  - The groups can overlap, but no cell can be left out.
  - The groups can wrap around the edges of the map, as the map is considered to be a torus.
  - The groups can be marked with a symbol or a color to identify them.
- The number of cells in a K-map depends on the number of variables in the function. For n variables, there are 2^n cells in the K-map.
- K-maps of 2 to 4 variables are easy to handle, but 5 and 6 variable K-maps are more complex and require visualization .
- For 5 variable K-maps, there are 32 cells, which can be arranged as two 4-variable K-maps, one on top of the other .
- The top map represents the function when the fifth variable is 0, and the bottom map represents the function when the fifth variable is 1 .
- The cells in the top and bottom maps that have the same address are considered to be adjacent, and can be grouped together if they have the same value .
- For 6 variable K-maps, there are 64 cells, which can be arranged as four 4-variable K-maps, in a 2x2 grid.
- The four maps represent the function when the fifth and sixth variables are 00, 01, 10, and 11 respectively.
- The cells in the four maps that have the same address are considered to be adjacent, and can be grouped together if they have the same value.
- The cells in the four maps that are at the corners of the grid are also considered to be adjacent, and can be grouped together if they have the same value.
- An example of a 6 variable K-map is shown below:

![6 variable K-map](https://www.allaboutcircuits.com/uploads/articles/6-variable-k-map.jpg)

- The minimal expression of the function is obtained by writing the implicants for each group, and then combining them with OR (for SOP) or AND (for POS) operators.
- The implicants are written by using the variables that are common to all the cells in the group, and omitting the variables that change within the group.
- The omitted variables are called don't care variables, and are represented by X.
- For example, the group marked with A in the above map has the implicant ABCD'EF'.
- The group marked with B has the implicant ABCD'X'F, where X is a don't care variable.
- The group marked with C has the implicant A'BC'X'F, where X is a don't care variable.
- The group marked with D has the implicant A'BC'EF.
- The minimal expression of the function is A'BC'EF + A'BC'X'F + ABCD'X'F + ABCD'EF'.
- This expression can be further simplified by using the distributive law and eliminating the redundant terms.
- The final expression of the function is A'