### Recursive definition of relation

- A relation is a set of ordered pairs that satisfies some property or condition.
- A recursive definition of a relation is a way of specifying a relation by giving a rule that generates the next element of the relation from the previous ones.
- A recursive definition of a relation consists of two parts:
  - A base case, which specifies one or more initial elements of the relation.
  - A recursive step, which specifies how to obtain new elements of the relation from the existing ones using a function or an operator.
- A recursive definition of a relation is also called an inductive definition, because it allows us to prove properties of the relation by induction.
- A recursive definition of a relation is useful when the relation has a regular or repetitive pattern or structure.

- For example, consider the relation R on the set of natural numbers N, defined as follows:

  - R = {(a, b) ∈ N x N | a < b}

  - This relation can be defined recursively as follows:

    - Base case: (0, 1) ∈ R
    - Recursive step: If (a, b) ∈ R, then (a, b + 1) ∈ R and (a + 1, b + 1) ∈ R

  - This recursive definition generates all the elements of R by starting from the base case and applying the recursive step repeatedly.

  - For example, we can obtain the following elements of R:

    - (0, 2) ∈ R, because (0, 1) ∈ R and (0, 1 + 1) ∈ R
    - (1, 3) ∈ R, because (0, 2) ∈ R and (0 + 1, 2 + 1) ∈ R
    - (2, 4) ∈ R, because (1, 3) ∈ R and (1 + 1, 3 + 1) ∈ R
    - And so on.

Some possible mnemonics and learning tricks for the topic are:

- To remember the base case and the recursive step, you can use the acronym BARS: Base case, Apply function, Repeat, Stop.
- To remember the difference between a relation and a function, you can use the phrase "A relation is a set, a function is a rule".
- To remember the types of relations, you can use the word "RARE": Reflexive, Antisymmetric, Reflexive, Equivalence.