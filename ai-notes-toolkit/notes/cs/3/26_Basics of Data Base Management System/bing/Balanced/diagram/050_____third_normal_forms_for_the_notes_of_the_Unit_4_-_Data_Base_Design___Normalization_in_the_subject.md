### Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table.
- A transitive dependency is a functional dependency between two or more non-prime attributes that are indirectly determined by the primary key.
- For example, consider a table with the following attributes: Student ID, Name, Course, Instructor, Instructor Office.
  - The primary key is Student ID and Course, since they uniquely identify each record.
  - The non-prime attributes are Name, Instructor, and Instructor Office.
  - There is a transitive dependency between Instructor and Instructor Office, since the office of an instructor is determined by the instructor, not by the primary key.
  - To eliminate the transitive dependency, we can split the table into two tables: one with Student ID, Name, Course, and Instructor, and another with Instructor and Instructor Office.
  - This way, we avoid duplication of data and potential inconsistencies in the instructor office information.
- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the 3NF.
  - The 3NF always ensures functional dependency preserving and lossless decomposition.
  - The 3NF reduces the complexity of the database design and makes it easier to maintain and query.