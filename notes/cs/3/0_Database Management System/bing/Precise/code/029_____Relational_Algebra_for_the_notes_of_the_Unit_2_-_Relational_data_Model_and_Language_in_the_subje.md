### Relational Algebra

Relational algebra is a procedural query language for relational databases. It consists of a set of operations that take one or two relations as input and produce a new relation as output. The fundamental operations of relational algebra are:

1. **Selection**: The selection operation selects rows from a relation that satisfy a given predicate. It is denoted by the sigma (σ) symbol.

2. **Projection**: The projection operation selects columns from a relation and discards the other columns. It is denoted by the pi (π) symbol.

3. **Union**: The union operation combines two relations by taking the union of their tuples. The two relations must have the same set of attributes.

4. **Set difference**: The set difference operation takes the difference of two relations by removing the tuples of the second relation from the first relation.

5. **Cartesian product**: The Cartesian product operation combines two relations by forming all possible combinations of their tuples.

6. **Rename**: The rename operation renames the attributes of a relation.

7. **Intersection**: The intersection operation takes the intersection of two relations by keeping only the tuples that are present in both relations.

8. **Join**: The join operation combines two relations by forming all possible combinations of their tuples and keeping only the combinations that satisfy a given predicate.

Relational algebra provides a foundation for the SQL language, which is used to query and manipulate data in relational databases. It is important to understand the concepts of relational algebra in order to effectively use SQL and design efficient database systems.