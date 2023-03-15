### Recursive definition of relation

- A relation is a set of ordered pairs that satisfies some property or condition.
- A recursive definition of a relation consists of two parts: a base case and a recursive step.
- A base case specifies one or more ordered pairs that belong to the relation.
- A recursive step specifies a rule that generates new ordered pairs from the existing ones.
- A recursive definition of a relation is complete if every ordered pair in the relation can be obtained by applying the base case and the recursive step finitely many times.

#### Example 1: The relation "is a multiple of" on the set of natural numbers

- Base case: (0, n) belongs to the relation for any natural number n.
- Recursive step: If (a, b) belongs to the relation, then (a + b, b) also belongs to the relation.
- This means that a is a multiple of b if and only if a can be obtained by adding b to itself zero or more times.

#### Example 2: The relation "is an ancestor of" on the set of people

- Base case: (p, q) belongs to the relation if p is a parent of q.
- Recursive step: If (p, q) and (q, r) belong to the relation, then (p, r) also belongs to the relation.
- This means that p is an ancestor of r if and only if p is a parent of q and q is an ancestor of r.