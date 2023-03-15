### Composite Relations

- A composite relation is a relation that is obtained by combining two or more existing relations using a specific rule  .
- The rule for combining relations is called the composition of relations .
- The composition of relations is defined as follows: Let R be a relation from a set A to a set B, and let S be a relation from B to a set C. Then, the composition of R and S, denoted by R◦S, is a relation from A to C such that (a, c) ∈ R◦S if and only if there exists some b ∈ B such that (a, b) ∈ R and (b, c) ∈ S  .
- The composition of relations can be represented by a diagram as follows :

```
A --R--> B --S--> C
|                 |
|                 |
|-----R◦S-------->|
```

- The composition of relations is associative, meaning that (R◦S)◦T = R◦(S◦T) for any three relations R, S, and T that can be composed .
- The composition of relations is not commutative, meaning that R◦S is not necessarily equal to S◦R for any two relations R and S that can be composed .
- The composition of relations can be used to model various concepts and phenomena, such as functions, transformations, equivalence relations, order relations, and more  .