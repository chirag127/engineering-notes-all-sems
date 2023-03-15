### K Map Minimization upto 6 Variables

- Karnaugh map (K-map) is a graphical tool to simplify a Boolean expression or to convert a truth table to its corresponding logic circuit in a simple and orderly manner.
- K-map can handle up to four variables for SOP (sum of product) and POS (product of sum) expressions. For more than four variables, Quine-McCluskey method is preferred.
- However, it is possible to extend the K-map method to handle up to six variables by using three-dimensional or multidimensional K-maps.
- A three-dimensional K-map consists of two or more two-dimensional K-maps stacked on top of each other, with the corresponding cells connected by dotted lines.
- A multidimensional K-map consists of a rectangular array of two-dimensional K-maps, with the corresponding cells connected by solid or dashed lines.
- The rules for grouping and minimizing the K-map cells are the same as for the two-dimensional case, except that the groups can span across the layers or dimensions of the K-map.
- The following are some examples of K-map minimization for up to six variables:

#### Example 1: Minimize the following SOP expression using a three-dimensional K-map:

F(A,B,C,D,E) = ∑m(0,1,2,3,4,5,8,9,10,11,12,13,16,17,18,19,20,21,24,25,26,27,28,29)

- The expression has five variables, so we need a three-dimensional K-map with two layers of 4x4 two-dimensional K-maps.
- The first layer corresponds to E=0 and the second layer corresponds to E=1.
- The rows and columns of each layer are labeled by the values of A and B, and C and D, respectively.
- The cells are filled with 1s for the minterms of the expression and 0s for the remaining cells.
- The K-map is shown below:

|E=0|CD|00|01|11|10|
|:-:|:-:|:-:|:-:|:-:|:-:|
|AB|00|1|1|1|1|
|01|1|1|1|1|
|11|0|0|0|0|
|10|1|1|1|1|

|E=1|CD|00|01|11|10|
|:-:|:-:|:-:|:-:|:-:|:-:|
|AB|00|1|1|1|1|
|01|1|1|1|1|
|11|0|0|0|0|
|10|1|1|1|1|

- The groups of adjacent 1s are shown by different colors and shapes, and the corresponding prime implicants are:

|Group|Prime Implicant|
|:-:|:-:|
|Red Square|A'B'E'|
|Green Circle|A'B'E|
|Blue Triangle|AB'E'|
|Yellow Diamond|AB'E|
|Pink Hexagon|C'D'E'|
|Cyan Star|C'D'E|

- The minimum SOP expression is obtained by selecting the essential prime implicants and the minimum number of remaining prime implicants to cover all the 1s in the K-map.
- The essential prime implicants are those that cover at least one 1 that is not covered by any other prime implicant.
- In this case, the essential prime implicants are the red square, the green circle, the blue triangle, and the yellow diamond, as they cover the corners of the K-map that are not covered by any other group.
- The remaining prime implicants are the pink hexagon and the cyan star, which cover the middle cells of the K-map that are also covered by other groups.
- We can select either one of them to complete the cover, as they are equivalent in terms of cost and literals.
- Let us choose the pink hexagon for simplicity.
- The minimum SOP expression is:

F(A,B,C,D,E) = A'B'E' + A'B'E + AB'E' + AB'E + C'D'E'