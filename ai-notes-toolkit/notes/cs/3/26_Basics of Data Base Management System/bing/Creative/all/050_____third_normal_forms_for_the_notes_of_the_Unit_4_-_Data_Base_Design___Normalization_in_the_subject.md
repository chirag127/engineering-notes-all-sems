# Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- 3NF was originally defined by E. F. Codd in 1971.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table.
- A transitive dependency is a functional dependency between two non-prime attributes, such that one non-prime attribute determines another non-prime attribute through the primary key.
- For example, consider a table with the following attributes: Student ID, Student Name, Course ID, Course Name, Instructor ID, Instructor Name.
  - The primary key is (Student ID, Course ID).
  - The non-prime attributes are Student Name, Course Name, Instructor ID, Instructor Name.
  - There is a transitive dependency between Course ID and Instructor ID, because Course ID determines Instructor ID through the primary key.
  - There is also a transitive dependency between Instructor ID and Instructor Name, because Instructor ID determines Instructor Name.
  - To convert this table to 3NF, we need to remove the transitive dependencies by creating separate tables for Course and Instructor, as shown below:

| Student ID | Student Name | Course ID |
|------------|--------------|-----------|
| 101        | Alice        | C1        |
| 102        | Bob          | C2        |
| 103        | Charlie      | C3        |
| 104        | David        | C1        |

| Course ID | Course Name | Instructor ID |
|-----------|-------------|---------------|
| C1        | Math        | I1            |
| C2        | Physics     | I2            |
| C3        | Chemistry   | I3            |

| Instructor ID | Instructor Name |
|---------------|-----------------|
| I1            | Eve             |
| I2            | Frank           |
| I3            | Grace           |

- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the 3NF.
  - The 3NF always ensures functional dependency preserving and lossless decomposition.
  - The 3NF reduces the storage space and improves the performance of the database.