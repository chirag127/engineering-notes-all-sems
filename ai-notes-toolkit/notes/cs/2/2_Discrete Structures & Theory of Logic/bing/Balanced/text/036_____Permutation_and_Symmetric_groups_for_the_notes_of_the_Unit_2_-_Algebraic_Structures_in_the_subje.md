### Permutation and Symmetric Groups

- A **permutation** of a set is a bijection (one-to-one and onto function) from the set to itself. It is a way of rearranging the elements of the set in a different order.
- A **permutation group** on a set is a subset of the set of all permutations of the set that forms a group under the operation of function composition. It is a group of permutations that preserves some structure or property of the set.
- A **symmetric group** on a set is the set of all permutations of the set. It is the largest possible permutation group on the set. It is denoted by Sym(X) or S<sub>n</sub> if X = {1, 2, ..., n}.
- Every permutation group is a subgroup of a symmetric group, but not every subgroup of a symmetric group is a permutation group. For example, the group of rotations of a square is a permutation group on the set of vertices, but it is not a symmetric group because it does not contain all possible permutations of the vertices.
- The order of a permutation group is the number of permutations in the group. The order of a symmetric group is n!, where n is the size of the set. For example, the order of S<sub>4</sub> is 4! = 24.
- A permutation can be represented by a **cycle notation**, which lists the elements that are moved by the permutation in a circular order. For example, the permutation (1 2 3) means that 1 is mapped to 2, 2 is mapped to 3, and 3 is mapped to 1. The permutation (1 2)(3 4) means that 1 is mapped to 2, 2 is mapped to 1, 3 is mapped to 4, and 4 is mapped to 3. The permutation (1) means that 1 is mapped to itself, and it is called the **identity permutation**. It is denoted by e or id.
- A permutation can also be represented by a **two-row notation**, which lists the elements of the set in the first row and their images in the second row. For example, the permutation (1 2 3) can be written as

|1|2|3|
|-|-|-|
|2|3|1|

- The **inverse** of a permutation is the permutation that undoes its effect. It can be obtained by reversing the order of the cycles or swapping the rows of the two-row notation. For example, the inverse of (1 2 3) is (3 2 1) or

|1|2|3|
|-|-|-|
|3|1|2|

- The **composition** of two permutations is the permutation that results from applying the first permutation and then the second permutation. It can be obtained by multiplying the cycles from right to left or by applying the two-row notation from bottom to top. For example, the composition of (1 2 3) and (2 3 4) is (1 4 2 3) or

|1|2|3|4|
|-|-|-|-|
|2|3|4|1|
|4|1|2|3|

- The **order** of a permutation is the smallest positive integer k such that the permutation raised to the k-th power is the identity permutation. It can be obtained by finding the least common multiple of the lengths of the cycles. For example, the order of (1 2 3) is 3, and the order of (1 2)(3 4) is 2.
- A permutation is called **even** if it can be written as a product of an even number of transpositions (cycles of length 2), and **odd** if it can be written as a product of an odd number of transpositions. For example, (1 2 3) is even because it can be written as (1 2)(2 3), and (1 2)(3 4) is odd because it can be written as (1 2)(3 4). The **sign** of a permutation is +1 if it is even and -1 if it is odd. It is denoted by sgn(σ) or ε(σ).
- A **subgroup** of a group is a subset of the group that is also a group under the same operation. A subgroup is called **proper** if it is not equal to the whole group