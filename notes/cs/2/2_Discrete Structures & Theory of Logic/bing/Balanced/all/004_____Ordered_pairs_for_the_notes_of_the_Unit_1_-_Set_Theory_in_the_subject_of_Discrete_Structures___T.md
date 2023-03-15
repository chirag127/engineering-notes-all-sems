# Ordered pairs for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- An ordered pair is a pair of elements where the order matters. For example, (1, 2) is different from (2, 1).
- An ordered pair can be written as (a, b) where a is the first element and b is the second element.
- An ordered pair can also be represented by a point on a Cartesian plane, where the first element is the x-coordinate and the second element is the y-coordinate. For example, (3, 4) is the point (3, 4) on the plane.
- The set of all ordered pairs of a given type is called a Cartesian product. For example, the Cartesian product of two sets A and B is the set of all ordered pairs (a, b) where a belongs to A and b belongs to B. It is denoted by A x B.
- The Cartesian product of two sets can be visualized by a table or a grid, where each row corresponds to an element of the first set and each column corresponds to an element of the second set. The ordered pairs are the cells of the table or the grid. For example, if A = {1, 2, 3} and B = {a, b}, then A x B = {(1, a), (1, b), (2, a), (2, b), (3, a), (3, b)} and the table is:

|   | a | b |
|---|---|---|
| 1 |(1, a)|(1, b)|
| 2 |(2, a)|(2, b)|
| 3 |(3, a)|(3, b)|

- The Cartesian product of two sets is not commutative, meaning that A x B is not the same as B x A. For example, if A = {1, 2} and B = {a, b, c}, then A x B = {(1, a), (1, b), (1, c), (2, a), (2, b), (2, c)} and B x A = {(a, 1), (a, 2), (b, 1), (b, 2), (c, 1), (c, 2)}. The tables are:

|   | a | b | c |
|---|---|---|---|
| 1 |(1, a)|(1, b)|(1, c)|
| 2 |(2, a)|(2, b)|(2, c)|

|   | 1 | 2 |
|---|---|---|
| a |(a, 1)|(a, 2)|
| b |(b, 1)|(b, 2)|
| c |(c, 1)|(c, 2)|

- The Cartesian product of more than two sets can be defined recursively by using the Cartesian product of two sets. For example, the Cartesian product of three sets A, B, and C is the set of all ordered pairs (a, b, c) where a belongs to A, b belongs to B, and c belongs to C. It is denoted by A x B x C. It can also be written as (A x B) x C or A x (B x C), since the order of the sets does not matter. For example, if A = {1, 2}, B = {a, b}, and C = {x, y}, then A x B x C = {(1, a, x), (1, a, y), (1, b, x), (1, b, y), (2, a, x), (2, a, y), (2, b, x), (2, b, y)}. The table is:

|   | a | b |
|---|---|---|
| 1 |(1, a)|(1, b)|
| 2 |(2, a)|(2, b)|

|   | x | y |
|---|---|---|
|(1, a)|(1, a, x)|(1, a, y)|
|(1, b)|(1, b, x)|(1, b, y)|
|(2, a)|(2, a, x)|(2, a, y)|
|(2, b)|(2, b, x)|(2, b, y)|

- The Cartesian product of n sets can be generalized by using the notation A1 x A2 x ... x An, where Ai is the