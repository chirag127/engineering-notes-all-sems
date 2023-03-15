### Unit 4 - Data Base Design & Normalization

#### Database Design
- Database design is the process of creating a detailed data model of a database.
- This data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design in a data definition language, which can then be used to create a database.
- A fully attributed data model contains detailed attributes for each entity.

#### Normalization
- Normalization is the process of organizing a database in a way that reduces redundancy and dependency.
- It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way.
- Normalization typically involves dividing a database into smaller, more focused tables and defining relationships between those tables.
- The main goal of normalization is to reduce data redundancy, which means eliminating duplicate data and ensuring that data is stored in the most efficient and logical way possible.

#### First Normal Form (1NF)
- A relation is in first normal form if and only if the domain of each attribute contains only atomic (indivisible) values, and the value of each attribute contains only a single value from that domain.
- In other words, a table is in 1NF if and only if it contains no repeating groups or arrays.

#### Second Normal Form (2NF)
- A relation is in second normal form if it is in first normal form and every non-prime attribute is fully functionally dependent on the primary key.
- In other words, a table is in 2NF if and only if it is in 1NF and no non-prime attribute is dependent on any proper subset of any candidate key of the table.

#### Third Normal Form (3NF)
- A relation is in third normal form if it is in second normal form and every non-prime attribute is non-transitively dependent on the primary key.
- In other words, a table is in 3NF if and only if it is in 2NF and there are no transitive dependencies between non-prime attributes.
