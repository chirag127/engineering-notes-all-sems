### normal forms for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

Normal forms are a set of guidelines for organizing data in a database to minimize data redundancy and improve data integrity. They are used to ensure that data is stored in a consistent and efficient manner. 

1. First Normal Form (1NF): In 1NF, each column in a table contains only atomic values, and each row is unique.

2. Second Normal Form (2NF): In 2NF, a table is in 1NF and all non-key columns are dependent on the entire primary key.

3. Third Normal Form (3NF): In 3NF, a table is in 2NF and all non-key columns are not dependent on other non-key columns.

4. Boyce-Codd Normal Form (BCNF): In BCNF, a table is in 3NF and every non-trivial functional dependency is on a superkey.

5. Fourth Normal Form (4NF): In 4NF, a table is in BCNF and there are no multi-valued dependencies.

6. Fifth Normal Form (5NF): In 5NF, a table is in 4NF and there are no join dependencies.

Normalization is a key aspect of database design and helps to ensure that data is stored in a consistent and efficient manner. By following the normal forms, database designers can minimize data redundancy, improve data integrity, and ensure that data is stored in a manner that is easy to maintain and update.
