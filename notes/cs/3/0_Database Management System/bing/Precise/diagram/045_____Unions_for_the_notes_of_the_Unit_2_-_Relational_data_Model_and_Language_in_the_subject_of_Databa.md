### Unions

- A union is a set operation in relational algebra that combines the tuples of two relations into a single relation.
- The two relations must have the same number of attributes and the corresponding attributes must have compatible data types.
- The resulting relation contains all the tuples from both relations, but any duplicate tuples are removed.
- The union operation is denoted by the symbol ∪.
- The formal definition of union is: R ∪ S = {t | t ∈ R or t ∈ S}.
- Union is a commutative operation, meaning that the order of the relations does not matter (R ∪ S = S ∪ R).
- Union is also an associative operation, meaning that the grouping of the relations does not matter ((R ∪ S) ∪ T = R ∪ (S ∪ T)).
- In SQL, the union operation is performed using the UNION keyword.

Example:

Consider the following two relations R and S:

R = {(1, 'A'), (2, 'B'), (3, 'C')}

S = {(3, 'C'), (4, 'D'), (5, 'E')}

The union of R and S is:

R ∪ S = {(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')}

In SQL, the union of R and S can be obtained using the following query:

SELECT * FROM R
UNION
SELECT * FROM S;