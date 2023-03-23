### Third Normal Forms for the Notes of the Unit 4 - Database Design & Normalization in the Subject of Basics of Database Management System

In the process of database normalization, the third normal form (3NF) is an essential step that ensures the elimination of data redundancy and inconsistencies. Here are some important points to remember about 3NF:

- The objective of 3NF is to minimize data redundancy by ensuring that a table does not contain any non-key attribute that is dependent on only a portion of the primary key.
- A table is said to be in 3NF if it is already in second normal form (2NF) and all non-key attributes are dependent only on the primary key or other non-key attributes.
- To achieve 3NF, it is necessary to break down tables with multiple independent relationships into separate tables.
- In 3NF, each non-key attribute is directly dependent on the primary key, and there are no transitive dependencies between non-key attributes.
- Transitive dependencies occur when a non-key attribute is dependent on another non-key attribute, which in turn is dependent on the primary key.
- To avoid transitive dependencies, it is necessary to split the table into multiple tables, each with a separate primary key and a set of non-key attributes that are dependent only on the primary key.
- The 3NF helps to eliminate data inconsistencies and anomalies, making the database more robust and efficient.
- While 3NF is an essential step in the normalization process, it is not always necessary to achieve it in every case. In some situations, it may be more practical to settle for a lower normal form if the benefits of higher normalization do not outweigh the costs.

In conclusion, 3NF is a crucial step in the normalization process that ensures the elimination of data redundancy and inconsistencies. It helps to ensure that a database is robust, efficient, and easy to maintain.