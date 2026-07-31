### Unit 4 - Data Base Design & Normalization

#### Database Design
- Database design is the process of producing a detailed data model of a database.
- This data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design in a data definition language, which can then be used to create a database.
- A fully attributed data model contains detailed attributes for each entity.

#### Normalization
- Normalization is the process of organizing a database in a way that reduces redundancy and dependency.
- It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way.
- Normalization typically involves dividing a database into smaller, more focused tables and defining relationships between those tables.
- The main goal of normalization is to reduce data redundancy, which means eliminating duplicate data and ensuring that data is stored in the most efficient way possible.

#### First Normal Form (1NF)
- A relation is in first normal form if and only if the domain of each attribute contains only atomic (indivisible) values, and the value of each attribute contains only a single value from that domain.
- In other words, the values in each column of a table must be of the same data type, and each row must have a unique combination of values.

#### Second Normal Form (2NF)
- A relation is in second normal form if it is in first normal form and every non-prime attribute is fully functionally dependent on the primary key.
- This means that there should be no partial dependencies, where an attribute depends on only part of the primary key.

#### Third Normal Form (3NF)
- A relation is in third normal form if it is in second normal form and every non-prime attribute is non-transitively dependent on the primary key.
- This means that there should be no transitive dependencies, where an attribute depends on another attribute that depends on the primary key.

#### Boyce-Codd Normal Form (BCNF)
- A relation is in Boyce-Codd normal form if and only if for every one of its non-trivial functional dependencies X → Y, X is a superkey.
- This means that the determinant of a non-trivial functional dependency must be a candidate key.

#### Fourth Normal Form (4NF)
- A relation is in fourth normal form if and only if, for every one of its non-trivial multivalued dependencies X →> Y, X is a superkey.
- This means that there should be no multi-valued dependencies, where an attribute depends on another attribute, but not on the key.

#### Fifth Normal Form (5NF)
- A relation is in fifth normal form if and only if, for every join dependency {R1, R2, ..., Rn} that holds over R, the intersection of each pair of Ri's is a superkey of R.
- This means that there should be no join dependencies, where the relation can be decomposed into multiple smaller relations, but cannot be reconstructed from those smaller relations without losing information.
