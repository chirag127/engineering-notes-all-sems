Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on permutation and symmetric groups for the unit 2 of algebraic structures in the subject of discrete structures and theory of logic.

### Permutation and Symmetric Groups

- A **permutation** of a set is a bijective function from the set to itself, that is, a function that rearranges the elements of the set. For example, if X = {a, b, c}, then a permutation of X is a function f such that f(a) = b, f(b) = c, and f(c) = a. 
- A **permutation group** on a set X is a subgroup of the symmetric group on X, that is, a set of permutations of X that is closed under function composition and inverse, and contains the identity function. For example, if X = {1, 2, 3}, then a permutation group on X is the set {e, f, g}, where e is the identity function, f is the function that swaps 1 and 2, and g is the function that swaps 2 and 3.  
- A **symmetric group** on a set X is the set of all permutations of X, denoted by Sym(X) or S_n, where n is the cardinality of X. For example, if X = {1, 2, 3}, then the symmetric group on X is the set {e, f, g, h, i, j}, where e, f, and g are as above, and h is the function that swaps 1 and 3, i is the function that cycles 1, 2, and 3 clockwise, and j is the function that cycles 1, 2, and 3 counterclockwise.  
- The symmetric group on n elements has n! (n factorial) elements, and is the largest permutation group on n elements. Every group of order n is isomorphic to a subgroup of the symmetric group on n elements, by Cayley's theorem.  
- The symmetric group on n elements has a natural representation as a group of matrices, called the **permutation matrices**. A permutation matrix is a square matrix of size n that has exactly one 1 in each row and column, and 0 elsewhere. The matrix corresponds to the permutation that maps the i-th element to the j-th element if and only if the (i, j)-th entry of the matrix is 1. For example, the permutation matrix for the function f that swaps 1 and 2 is

```
|0 1 0|
|1 0 0|
|0 0 1|
```

The group operation of the symmetric group is then the matrix multiplication of the permutation matrices.