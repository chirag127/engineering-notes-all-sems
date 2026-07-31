# Relations

- A relation is a way of describing a connection or association between two or more sets of elements .
- A relation can be represented by a set of ordered pairs, where the first element of each pair belongs to the first set and the second element belongs to the second set  .
- For example, if A = {1, 2, 3} and B = {a, b, c}, then a possible relation between A and B is R = {(1, a), (2, b), (3, c)}.
- The domain of a relation is the set of all first elements of the ordered pairs, and the range is the set of all second elements of the ordered pairs.
- For example, if R = {(1, a), (2, b), (3, c)}, then the domain of R is {1, 2, 3} and the range of R is {a, b, c}.
- A relation can also be represented by a mapping diagram, where arrows are drawn from the elements of the first set to the elements of the second set that are related to them .
- For example, the relation R = {(1, a), (2, b), (3, c)} can be shown by the following diagram:

```
  1  2  3
 /| /| /|
/ | / | /|
a b c
```

- A relation can also be represented by a matrix, where the rows correspond to the elements of the first set and the columns correspond to the elements of the second set, and a 1 is placed in the entry if the corresponding elements are related, and a 0 otherwise .
- For example, the relation R = {(1, a), (2, b), (3, c)} can be shown by the following matrix:

```
  a b c
1 1 0 0
2 0 1 0
3 0 0 1
```

- A relation can also be represented by a graph, where the vertices are the elements of the sets and the edges are the ordered pairs that are related .
- For example, the relation R = {(1, a), (2, b), (3, c)} can be shown by the following graph:

```
1---a
|
2---b
|
3---c
```

- A relation can have different properties, such as reflexivity, symmetry, transitivity, antisymmetry, and equivalence .
- A relation is reflexive if every element is related to itself, that is, (a, a) is in the relation for every a in the set .
- For example, the relation R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)} on the set A = {1, 2, 3} is reflexive.
- A relation is symmetric if whenever (a, b) is in the relation, so is (b, a), that is, the order of the elements does not matter .
- For example, the relation R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2)} on the set A = {1, 2, 3} is symmetric.
- A relation is transitive if whenever (a, b) and (b, c) are in the relation, so is (a, c), that is, the relation can be extended along a chain .
- For example, the relation R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)} on the set A = {1, 2, 3} is transitive.
- A relation is antisymmetric if whenever (a, b) and (b, a) are in the relation, then a = b, that is, the only way for two elements to be related in both directions is if they are the same [