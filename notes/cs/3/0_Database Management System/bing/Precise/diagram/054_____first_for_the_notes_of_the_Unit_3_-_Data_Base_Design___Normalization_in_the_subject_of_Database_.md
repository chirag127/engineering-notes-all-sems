### Unit 3 - Database Design & Normalization

Database design is the process of organizing data in a way that it meets the requirements of the users and the organization. Normalization is a technique used in database design to minimize data redundancy and dependency.

1. **Database Design:** The process of designing a database involves identifying the entities, attributes, and relationships that are relevant to the organization's operations. The design should also take into account the constraints and requirements of the users.

2. **Normalization:** Normalization is a technique used to minimize data redundancy and dependency in a database. It involves organizing the data into tables and establishing relationships between them. The goal of normalization is to ensure that each piece of data is stored in only one place, reducing the chances of inconsistencies and errors.

3. **First Normal Form (1NF):** A table is in first normal form if it contains no repeating groups or arrays. This means that each column in the table should contain only atomic values, and there should be no repeating groups of columns.

4. **Second Normal Form (2NF):** A table is in second normal form if it is in first normal form and all non-key attributes are dependent on the entire primary key. This means that there should be no partial dependencies, where an attribute depends on only part of the primary key.

5. **Third Normal Form (3NF):** A table is in third normal form if it is in second normal form and there are no transitive dependencies. This means that all non-key attributes should be directly dependent on the primary key, and not on other non-key attributes.

6. **Boyce-Codd Normal Form (BCNF):** A table is in Boyce-Codd normal form if it is in third normal form and every determinant is a candidate key. This means that there should be no dependencies between non-prime attributes.
