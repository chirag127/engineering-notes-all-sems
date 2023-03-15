# Functional Dependencies

Functional dependencies are a fundamental concept in the normalization of relational databases. They are used to define the relationships between attributes in a relation and to identify the keys of a relation.

A functional dependency is a constraint between two sets of attributes in a relation. It is denoted by X -> Y, where X and Y are sets of attributes in a relation R. This means that for any two tuples t1 and t2 in R, if t1[X] = t2[X], then t1[Y] = t2[Y].

In other words, the values of the attributes in Y are determined by the values of the attributes in X. X is called the determinant and Y is called the dependent.

Functional dependencies are used to identify the keys of a relation. A key is a set of attributes that uniquely identifies a tuple in a relation. A key is minimal if no proper subset of the key is also a key.

A relation is in Boyce-Codd Normal Form (BCNF) if for every non-trivial functional dependency X -> Y, X is a superkey. A relation is in Third Normal Form (3NF) if for every non-trivial functional dependency X -> Y, either X is a superkey or Y is a prime attribute (an attribute that is part of some candidate key).

Normalization is the process of decomposing a relation into smaller relations to eliminate redundancy and anomalies. The goal is to have each relation in at least 3NF or BCNF.

Functional dependencies play a crucial role in the normalization process. They are used to identify the keys of a relation and to determine whether a relation is in a certain normal form. They are also used to decompose a relation into smaller relations that are in a higher normal form.