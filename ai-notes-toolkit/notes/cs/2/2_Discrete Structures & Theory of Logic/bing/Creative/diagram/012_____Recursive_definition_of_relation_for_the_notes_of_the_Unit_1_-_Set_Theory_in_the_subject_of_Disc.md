### Recursive definition of relation

- A relation is a set of ordered pairs that satisfies some property or condition.
- A recursive definition of a relation is a way of specifying a relation by giving a rule that generates the next element of the relation from the previous ones.
- A recursive definition of a relation consists of two parts: a base case and a recursive step.
- The base case specifies one or more elements of the relation that are given explicitly.
- The recursive step specifies how to obtain new elements of the relation from the existing ones using a function or an operator.
- A recursive definition of a relation is complete if it generates all the elements of the relation and no more.
- A recursive definition of a relation is unique if there is only one way to generate each element of the relation.

#### Example 1: The relation "divides" on the set of natural numbers

- The relation "divides" on the set of natural numbers is defined as follows: (a,b) is in the relation if and only if there exists a natural number c such that a*c=b.
- A recursive definition of this relation is:

  - Base case: (1,n) is in the relation for any natural number n.
  - Recursive step: If (a,b) is in the relation, then (a*s(b),b*s(a)) is in the relation, where s is the successor function that adds one to a natural number.

- This recursive definition is complete and unique, as it generates all the pairs of natural numbers that satisfy the condition of divisibility and no others, and there is only one way to obtain each pair.

#### Example 2: The relation "ancestor" on the set of people

- The relation "ancestor" on the set of people is defined as follows: (a,b) is in the relation if and only if a is an ancestor of b, that is, a is a parent, grandparent, great-grandparent, etc. of b.
- A recursive definition of this relation is:

  - Base case: (a,b) is in the relation if and only if a is a parent of b.
  - Recursive step: If (a,b) is in the relation and (b,c) is in the relation, then (a,c) is in the relation.

- This recursive definition is complete and unique, as it generates all the pairs of people that satisfy the condition of ancestry and no others, and there is only one way to obtain each pair.