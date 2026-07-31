### Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- 3NF was originally defined by E. F. Codd in 1971. Codd's definition states that a table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table. A transitive dependency is a functional dependency between two non-prime attributes, such that one non-prime attribute determines another non-prime attribute through the primary key.
- For example, consider a table with the following attributes: Student ID, Student Name, Course ID, Course Name, Instructor ID, Instructor Name. The primary key is (Student ID, Course ID). The non-prime attributes are Student Name, Course Name, Instructor ID, and Instructor Name. There is a transitive dependency between Course ID and Instructor ID, because Course ID determines Instructor ID through the primary key. This violates 3NF and can cause data anomalies, such as inconsistency, redundancy, and deletion anomalies.
- To convert the table into 3NF, we need to remove the transitive dependency by splitting the table into two tables: one with the attributes Student ID, Student Name, Course ID, Course Name, and another with the attributes Course ID, Instructor ID, Instructor Name. The primary key of the first table is (Student ID, Course ID), and the primary key of the second table is Course ID. The two tables are linked by a foreign key constraint on Course ID.
- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the Third Normal Form.
  - The Third Normal Form ensures functional dependency preserving and lossless decomposition, which means that the original data can be reconstructed from the normalized tables without any loss of information or inconsistency.
  - The Third Normal Form reduces the storage space and improves the performance of the database operations, such as insertion, deletion, and update.