### Relational Algebra - Relational Calculus

Relational Algebra and Relational Calculus are two formal query languages used to retrieve data from Relational Databases. Both these languages are used to manipulate data in a relational database. In this section, we will discuss the basics of Relational Algebra and Relational Calculus.

#### Relational Algebra

Relational Algebra is a procedural query language used to select, filter, and manipulate data in a relational database. It consists of a set of operations that can be used to manipulate relations. These operations can be divided into two categories - unary and binary.

##### Unary Operations

1. Selection (σ): This operation is used to select a subset of tuples from a relation that satisfy a given condition.
2. Projection (π): This operation is used to select a subset of attributes from a relation.
3. Renaming (ρ): This operation is used to rename the attributes of a relation.

##### Binary Operations

1. Union (⋃): This operation is used to combine two relations into a single relation.
2. Intersection (⋂): This operation is used to find the common tuples between two relations.
3. Difference (-): This operation is used to find the tuples that are present in one relation but not in the other.
4. Cartesian Product (×): This operation is used to combine each tuple of one relation with every tuple of another relation.

#### Relational Calculus

Relational Calculus is a non-procedural query language used to retrieve data from a relational database. It consists of two types of calculus - Tuple Relational Calculus (TRC) and Domain Relational Calculus (DRC).

##### Tuple Relational Calculus (TRC)

TRC is a formal language used to select tuples from a relation based on a given condition. It uses variables to represent tuples and a formula to define the condition.

##### Domain Relational Calculus (DRC)

DRC is a formal language used to select tuples from a relation based on a given condition. It uses variables to represent attributes and a formula to define the condition.

#### Conclusion

Relational Algebra and Relational Calculus are two important query languages used in the field of Relational Databases. While Relational Algebra is a procedural language, Relational Calculus is a non-procedural language. Both these languages are used to retrieve data from a relational database based on a given condition.