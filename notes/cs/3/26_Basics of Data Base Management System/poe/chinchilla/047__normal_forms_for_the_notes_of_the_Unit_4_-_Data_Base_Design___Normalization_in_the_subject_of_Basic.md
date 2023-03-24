### Normal Forms for the Notes of the Unit 4 - Database Design & Normalization in the Subject of Basics of Database Management System

In database management system, normalization is the process of organizing data in a database to reduce redundancy and dependency. Normalization helps in improving the performance of a database and ensures data integrity. Normalization is achieved by applying different normal forms to a database. The following are the different normal forms:

1. First Normal Form (1NF): 
   - A table is in 1NF if it has no repeating groups and all the attributes are atomic (indivisible).
   - Each attribute should have a unique name.
   - Each row should have a unique identifier called a primary key.

2. Second Normal Form (2NF): 
   - A table is in 2NF if it is in 1NF and all non-key attributes are fully functionally dependent on the primary key.
   - A fully functional dependency means that a non-key attribute is dependent on the entire primary key and not just a part of it.

3. Third Normal Form (3NF): 
   - A table is in 3NF if it is in 2NF and all non-key attributes are not transitively dependent on the primary key.
   - Transitive dependency means that a non-key attribute is dependent on another non-key attribute.

4. Boyce-Codd Normal Form (BCNF):
   - A table is in BCNF if for every functional dependency (X → Y), X is a superkey.
   - BCNF is a stronger form of 3NF.

5. Fourth Normal Form (4NF): 
   - A table is in 4NF if it is in BCNF and has no multi-valued dependencies.
   - Multi-valued dependencies occur when a non-key attribute is dependent on a combination of attributes that includes the primary key.

6. Fifth Normal Form (5NF):
   - A table is in 5NF if it is in 4NF and has no join dependencies.
   - Join dependencies occur when a table can be reconstructed by joining two or more tables together.

In conclusion, normalization is an important process in database design that helps in reducing data redundancy and ensuring data integrity. By applying the different normal forms, a database can be optimized for performance and maintainability.