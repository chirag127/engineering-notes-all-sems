### Unit 4 - Data Base Design & Normalization

#### Database Design
- Database design is the process of producing a detailed data model of a database.
- This data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design in a data definition language, which can then be used to create a database.
- A fully attributed data model contains detailed attributes for each entity.

#### Normalization
- Normalization is the process of organizing a database in a way that reduces redundancy and dependency.
- It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way.
- Normalization typically involves dividing a database into smaller, more focused tables and defining relationships between those tables.
- The main goal of normalization is to reduce data redundancy, which means eliminating duplicate data and ensuring that data is stored in the most efficient and logical way possible.

#### Normal Forms
- There are several normal forms, including first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF).
- Each normal form has a set of rules that must be followed in order to achieve that level of normalization.
- The higher the normal form, the less redundancy and dependency in the database.

#### First Normal Form (1NF)
- A table is in first normal form (1NF) if and only if the domain of each attribute contains only atomic (indivisible) values, and the value of each attribute contains only a single value from that domain.
- In other words, a table is in 1NF if it does not contain any repeating groups or arrays.

#### Second Normal Form (2NF)
- A table is in second normal form (2NF) if it is in 1NF and every non-prime attribute of the table is dependent on the whole of a candidate key.
- In other words, a table is in 2NF if all of its non-key attributes are dependent on the entire primary key.

#### Third Normal Form (3NF)
- A table is in third normal form (3NF) if it is in 2NF and every non-prime attribute of the table is non-transitively dependent on every key of the table.
- In other words, a table is in 3NF if all of its non-key attributes are directly dependent on the primary key and not on any other non-key attributes.

#### Boyce-Codd Normal Form (BCNF)
- A table is in Boyce-Codd normal form (BCNF) if and only if for every one of its dependencies X → Y, X is a superkey.
- In other words, a table is in BCNF if every determinant in the table is a candidate key.

#### Fourth Normal Form (4NF)
- A table is in fourth normal form (4NF) if and only if, for every one of its non-trivial multivalued dependencies X →> Y, X is a superkey.
- In other words, a table is in 4NF if it has no multi-valued dependencies.

#### Fifth Normal Form (5NF)
- A table is in fifth normal form (5NF) if and only if every join dependency in it is implied by the candidate keys.
- In other words, a table is in 5NF if it has no join dependencies that are not implied by the candidate keys. 
