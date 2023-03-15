# Third Normal Form

- Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.
- 3NF was originally defined by E. F. Codd in 1971.
- A table is in 3NF if and only if both of the following conditions hold:
  - The table is in second normal form (2NF).
  - No non-prime attribute is transitively dependent on the primary key.
- A non-prime attribute is an attribute that is not part of any candidate key of the table.
- A transitive dependency is a functional dependency between two non-prime attributes, such that one non-prime attribute determines another non-prime attribute through the primary key.
- For example, consider a table with the following attributes: Student_ID, Student_Name, Course_ID, Course_Name, Instructor_ID, Instructor_Name.
  - The primary key is (Student_ID, Course_ID).
  - The non-prime attributes are Student_Name, Course_Name, Instructor_ID, Instructor_Name.
  - There is a transitive dependency between Course_ID and Instructor_ID, because Course_ID determines Instructor_ID through the primary key.
  - There is also a transitive dependency between Instructor_ID and Instructor_Name, because Instructor_ID determines Instructor_Name.
  - To convert this table to 3NF, we need to remove the transitive dependencies by creating separate tables for Course and Instructor, as shown below:

| Student_ID | Student_Name | Course_ID |
|------------|--------------|-----------|
| S001       | Alice        | C001      |
| S002       | Bob          | C002      |
| S003       | Charlie      | C001      |
| S004       | David        | C003      |

| Course_ID | Course_Name | Instructor_ID |
|-----------|-------------|---------------|
| C001      | Database    | I001          |
| C002      | Programming | I002          |
| C003      | Math        | I003          |

| Instructor_ID | Instructor_Name |
|---------------|-----------------|
| I001          | John            |
| I002          | Mary            |
| I003          | Peter           |

- The advantages of 3NF are :
  - Normalization increases the data quality as the unwanted data is reduced from the database.
  - The transitive dependency creates the update anomalies and they can be removed by the usage of the 3NF.
  - The 3NF always ensures functional dependency preserving and lossless decomposition.
  - The 3NF reduces the storage space and improves the performance of the queries.
  - The 3NF makes the database more consistent and easier to maintain.