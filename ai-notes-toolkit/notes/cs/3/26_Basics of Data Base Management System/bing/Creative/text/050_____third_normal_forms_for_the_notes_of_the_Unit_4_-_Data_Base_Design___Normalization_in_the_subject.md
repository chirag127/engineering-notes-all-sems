### Third Normal Form for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- A table is in 3NF if it is in second normal form (2NF) and every non-key attribute is non-transitively dependent on the primary key. That is, there is no functional dependency between two non-key attributes.
- A functional dependency is a relationship between two sets of attributes such that for a given value of one set, there is only one possible value of the other set.
- A transitive dependency is a functional dependency between two non-key attributes that are both functionally dependent on the primary key.
- For example, consider a table with the attributes Student ID, Student Name, Course ID, Course Name, and Instructor Name. The primary key is Student ID and Course ID. The table is not in 3NF because there is a transitive dependency between Course Name and Instructor Name. That is, Course Name determines Instructor Name and both are non-key attributes. To make the table in 3NF, we need to split it into two tables: one with Student ID, Student Name, and Course ID, and another with Course ID, Course Name, and Instructor Name.
- The benefits of 3NF are that it eliminates data redundancy, improves data consistency, avoids data anomalies, and preserves data integrity.
- The drawbacks of 3NF are that it may increase the number of tables and joins, reduce query performance, and complicate data manipulation.
- The Third Normal Form is also considered to be the ample requirement to build a database as the tables in the Third Normal Form are devoid of insert, update or delete anomalies.
- The Third Normal Form removes the redundancy effectively so the data becomes consistent as well as maintains the data integrity.
- The Third Normal Form always ensures functional dependency preserving and lossless.