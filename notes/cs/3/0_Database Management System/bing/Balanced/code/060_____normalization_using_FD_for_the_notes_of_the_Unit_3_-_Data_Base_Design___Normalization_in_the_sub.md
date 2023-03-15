### Normalization using FD

Normalization is the process of designing a relational schema that minimizes redundancy and ensures data integrity. Normalization is based on the concept of functional dependency (FD), which describes the relationship between attributes (columns) in a table. A functional dependency FD: X -> Y means that the values of Y are determined by the values of X. Two tuples (rows) sharing the same values of X will necessarily have the same values of Y.

There are different levels of normalization, called normal forms, that are based on satisfying certain conditions on the functional dependencies of a table. The most common normal forms are:

- First normal form (1NF): A table is in 1NF if it does not contain any repeating groups of attributes, i.e., each attribute has a single value for each tuple.
- Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies.
- Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies.
- Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no dependencies on non-key attributes.

The process of normalization using FD involves the following steps:

- Identify all the functional dependencies in the table.
- Check if the table satisfies the desired normal form. If not, decompose the table into smaller tables that preserve the functional dependencies and the data.
- Repeat the process for each of the smaller tables until all of them are in the desired normal form.