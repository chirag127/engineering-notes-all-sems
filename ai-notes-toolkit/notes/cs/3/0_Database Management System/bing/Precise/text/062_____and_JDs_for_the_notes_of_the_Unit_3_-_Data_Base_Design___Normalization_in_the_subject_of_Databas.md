### Unit 3 - Data Base Design & Normalization

#### Database Design
- Database design is the process of creating a detailed data model of a database.
- This data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design in a data definition language, which can then be used to create a database.
- A fully attributed data model contains detailed attributes for each entity.

#### Normalization
- Normalization is the process of organizing a database in a way that reduces redundancy and dependency.
- It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way.
- Normalization typically involves dividing a database into smaller, more focused tables and defining relationships between those tables.

#### Normal Forms
- There are several normal forms, including first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF).
- Each normal form has a set of rules that must be followed in order to achieve that level of normalization.
- The higher the level of normalization, the less redundancy and dependency in the database.

#### First Normal Form (1NF)
- A table is in first normal form (1NF) if and only if the domain of each attribute contains only atomic (indivisible) values, and the value of each attribute contains only a single value from that domain.
- In other words, each column in the table must contain only one value per row, and there can be no repeating groups or arrays.

#### Second Normal Form (2NF)
- A table is in second normal form (2NF) if it is in 1NF and every non-prime attribute of the table is dependent on the whole of a candidate key.
- In other words, there should be no partial dependencies, where an attribute depends on only part of a candidate key.

#### Third Normal Form (3NF)
- A table is in third normal form (3NF) if it is in 2NF and every non-prime attribute of the table is non-transitively dependent on every key of the table.
- In other words, there should be no transitive dependencies, where an attribute depends on another attribute, which in turn depends on the key.

#### Boyce-Codd Normal Form (BCNF)
- A table is in Boyce-Codd normal form (BCNF) if and only if for every one of its dependencies X → Y, X is a superkey.
- In other words, the determinant of each functional dependency must be a candidate key.

#### Fourth Normal Form (4NF)
- A table is in fourth normal form (4NF) if and only if, for every one of its non-trivial multivalued dependencies X →→ Y, X is a superkey.
- In other words, there should be no multi-valued dependencies, where an attribute depends on another attribute, but not on the key.

#### Fifth Normal Form (5NF)
- A table is in fifth normal form (5NF) if and only if every join dependency in it is implied by the candidate keys.
- In other words, the table should not have any join dependencies that are not implied by the candidate keys.