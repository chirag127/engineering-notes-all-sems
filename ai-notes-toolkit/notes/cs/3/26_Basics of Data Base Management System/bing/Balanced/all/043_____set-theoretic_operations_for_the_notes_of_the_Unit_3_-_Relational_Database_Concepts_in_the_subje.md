# Set-theoretic operations in relational database

- Set-theoretic operations are based on the mathematical concept of sets, which are collections of distinct elements.
- Set-theoretic operations can be applied to relations in a relational database to combine or compare them in various ways.
- The main set-theoretic operations are union, intersection, difference, and Cartesian product.
- To apply set-theoretic operations to relations, the relations must be **union-compatible**, which means they have the same number and type of attributes, and the corresponding attributes have the same domain.
- The result of a set-theoretic operation is also a relation, which may or may not be stored in the database.

## Union

- The union operation, denoted by ∪, returns a relation that contains all the tuples that are either in the first relation or in the second relation, or in both.
- The union operation eliminates any duplicate tuples from the result.
- The union operation is **commutative**, which means that R ∪ S is equivalent to S ∪ R.
- The union operation is also **associative**, which means that (R ∪ S) ∪ T is equivalent to R ∪ (S ∪ T).
- The union operation can be implemented in SQL using the **UNION** keyword.

## Intersection

- The intersection operation, denoted by ∩, returns a relation that contains only the tuples that are common to both the first and the second relation.
- The intersection operation does not produce any duplicate tuples, since they are already eliminated by the union-compatibility condition.
- The intersection operation is **commutative**, which means that R ∩ S is equivalent to S ∩ R.
- The intersection operation is also **associative**, which means that (R ∩ S) ∩ T is equivalent to R ∩ (S ∩ T).
- The intersection operation can be implemented in SQL using the **INTERSECT** keyword.

## Difference

- The difference operation, denoted by -, returns a relation that contains only the tuples that are in the first relation but not in the second relation.
- The difference operation does not produce any duplicate tuples, since they are already eliminated by the union-compatibility condition.
- The difference operation is **not commutative**, which means that R - S is not equivalent to S - R.
- The difference operation is **not associative**, which means that (R - S) - T is not equivalent to R - (S - T).
- The difference operation can be implemented in SQL using the **EXCEPT** or **MINUS** keyword, depending on the database system.

## Cartesian product

- The Cartesian product operation, denoted by ×, returns a relation that contains all possible combinations of tuples from the first and the second relation.
- The Cartesian product operation does not require the relations to be union-compatible, since it combines the attributes of both relations.
- The Cartesian product operation may produce duplicate tuples, if the relations have common attributes with the same values.
- The Cartesian product operation is **commutative**, which means that R × S is equivalent to S × R.
- The Cartesian product operation is also **associative**, which means that (R × S) × T is equivalent to R × (S × T).
- The Cartesian product operation can be implemented in SQL using the **CROSS JOIN** keyword.