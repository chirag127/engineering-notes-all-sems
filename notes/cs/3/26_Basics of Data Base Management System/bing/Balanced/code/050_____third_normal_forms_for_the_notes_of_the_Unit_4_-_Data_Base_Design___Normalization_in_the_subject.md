### Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table.
- A transitive dependency is a functional dependency between two or more non-prime attributes that are indirectly determined by the primary key.
- For example, consider a table with the following attributes: Student ID, Student Name, Course ID, Course Name, Instructor ID, Instructor Name.
- The primary key is (Student ID, Course ID), and the candidate keys are (Student ID, Course ID) and (Student ID, Course Name).
- The non-prime attributes are Student Name, Course Name, Instructor ID, and Instructor Name.
- There is a transitive dependency between Instructor ID and Instructor Name, since Instructor ID -> Instructor Name, and Instructor ID is determined by Course ID, which is part of the primary key.
- To convert this table to 3NF, we need to remove the transitive dependency by creating a separate table for instructors, with Instructor ID as the primary key and Instructor Name as the non-prime attribute.
- The original table will then have a foreign key reference to the instructor table, and the transitive dependency will be eliminated.
- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the Third Normal Form.
  - The Third Normal Form ensures functional dependency preserving and lossless decomposition, which means that the original data can be reconstructed from the normalized tables without any loss of information or inconsistency.
  - The Third Normal Form reduces the storage space and improves the performance of the database queries.