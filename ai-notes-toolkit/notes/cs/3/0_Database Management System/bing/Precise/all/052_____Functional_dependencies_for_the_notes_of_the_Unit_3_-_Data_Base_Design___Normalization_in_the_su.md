### Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

Functional dependency is a constraint between two sets of attributes in a relation from a database. It is a relationship that exists when one attribute uniquely determines another attribute. In other words, if the value of one attribute is known, it is possible to determine the value of another attribute.

Here are some key points to remember about functional dependencies:

1. A functional dependency is denoted by X -> Y, where X and Y are sets of attributes and X determines Y.
2. The left side of a functional dependency is called the determinant and the right side is called the dependent.
3. A functional dependency is trivial if the dependent is a subset of the determinant.
4. A functional dependency is non-trivial if the dependent is not a subset of the determinant.
5. A functional dependency is fully functional if the determinant is a candidate key.
6. A functional dependency is transitive if there is an attribute Z such that X -> Z and Z -> Y.
7. A functional dependency is a multi-valued dependency if for any two tuples t1 and t2, if t1[X] = t2[X], then t1[Y] = t2[Y] and t1[Z] = t2[Z] for all other attributes Z.

Functional dependencies are used in the process of normalization to decompose relations into smaller relations that are in a higher normal form. This helps to eliminate redundancy and anomalies in the data.