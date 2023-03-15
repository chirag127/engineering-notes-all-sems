### Database Design and Normalization

Database design is the process of creating a logical and physical structure for storing and manipulating data in a database. Database design involves identifying the entities, attributes, relationships, and constraints that are relevant to the data requirements of an application or a system. Database design also involves choosing an appropriate data model, such as the relational model, and applying the principles of normalization to ensure data integrity and avoid redundancy.

Normalization is a database schema design technique that reduces data redundancy and eliminates undesirable characteristics like insertion, update and deletion anomalies. Normalization rules divides larger tables into smaller tables and links them using relationships. The purpose of normalization is to make the data in the database comply with the following properties:

- Atomicity: Each attribute should store a single value and not a composite or multivalued attribute.
- Consistency: The data in the database should be consistent and not contain any contradictions or conflicts.
- Isolation: The data in the database should be independent of the application or the user that accesses it.
- Durability: The data in the database should be persistent and not affected by system failures or errors.

There are several levels of normalization, each with a specific set of rules or criteria. The most common levels are:

- First Normal Form (1NF): A table is in 1NF if it contains only atomic values and there are no repeating groups or arrays.
- Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
- Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
- Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
- Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and there are no multivalued dependencies.
- Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and there are no join dependencies.

The process of normalization involves decomposing a table into smaller tables that satisfy a higher level of normalization, while preserving the information and the dependencies in the original table. The benefits of normalization are:

- It reduces data redundancy and storage space.
- It improves data integrity and consistency.
- It simplifies data manipulation and querying.
- It facilitates data security and access control.
- It enhances database performance and scalability.