# Permutation and Symmetric Groups

## Permutation

- A permutation is a bijective function from a set to itself, that is, a function that maps each element of the set to a unique element of the set.
- A permutation can also be seen as a rearrangement of the elements of a set in a certain order.
- A permutation can be represented in different ways, such as a two-row notation, a cycle notation, or a matrix notation.
- For example, let S = {1, 2, 3, 4}. A permutation of S is a function f: S -> S such that f is bijective. One possible permutation is f(1) = 2, f(2) = 4, f(3) = 1, f(4) = 3. This can be written as:

  - Two-row notation: (1 2 3 4) (2 4 1 3)
  - Cycle notation: (1 2 4 3)
  - Matrix notation: | 1 2 3 4 | | 2 4 1 3 |

## Symmetric Group

- A symmetric group on a set X is the set of all permutations on X, denoted by Sym(X) or S_n, where n is the cardinality of X .
- A symmetric group is a group under the operation of function composition, that is, applying one permutation after another .
- For example, let S = {1, 2, 3, 4} and Sym(S) = S_4. Then S_4 has 4! = 24 elements, each of which is a permutation of S. The group operation is denoted by a dot, such as f.g, which means applying g first and then f. The identity element of S_4 is the permutation that maps each element to itself, denoted by e or (1)(2)(3)(4). The inverse of a permutation f is the permutation that undoes the effect of f, denoted by f^-1^.
- A symmetric group has some important properties, such as:

  - It is non-abelian, meaning that the order of applying permutations matters, that is, f.g is not necessarily equal to g.f.
  - It is finite, meaning that it has a finite number of elements, equal to n! for S_n.
  - It is the largest permutation group on n elements, meaning that any subgroup of S_n is also a permutation group.
  - It is isomorphic to the group of invertible n x n matrices under matrix multiplication, denoted by GL(n, R).

## Permutation Group

- A permutation group on a set X is a subgroup of the symmetric group on X, that is, a subset of Sym(X) that is also a group under function composition .
- A permutation group can also be defined as a group that acts on a set X, meaning that there is a homomorphism from the group to Sym(X) that preserves the group structure .
- For example, let S = {1, 2, 3, 4} and G = {(1), (1 2)(3 4), (1 3)(2 4), (1 4)(2 3)}. Then G is a permutation group on S, as it is a subgroup of S_4. It is also a group that acts on S, as there is a homomorphism from G to S_4 that maps each element of G to itself.
- A permutation group has some important properties, such as:

  - It is a subgroup of a symmetric group, meaning that it inherits some properties of the symmetric group, such as being finite and non-abelian.
  - It is isomorphic to a group of symmetries of some object, meaning that there is a one-to-one correspondence between the elements of the group and the ways of transforming the object without changing its shape or size .
  - It is determined by its generators, meaning that any element of the group can be obtained by applying a finite sequence of some fixed elements of the group, called generators .