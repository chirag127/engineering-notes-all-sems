# Third Normal Form

- Third normal form (3NF) is a database design principle that aims to reduce data redundancy and improve data integrity.
- 3NF states that a table is in 3NF if it is in second normal form (2NF) and every non-key attribute is non-transitively dependent on the primary key.
- Non-transitive dependency means that there is no indirect or hidden relationship between a non-key attribute and the primary key through another non-key attribute.
- For example, consider a table that stores the information of students, courses, and instructors:

| Student ID | Student Name | Course ID | Course Name | Instructor ID | Instructor Name |
|------------|--------------|-----------|-------------|---------------|-----------------|
| S001       | Alice        | C001      | DBMS        | I001          | Bob             |
| S002       | Bob          | C002      | OOP         | I002          | Carol           |
| S003       | Carol        | C001      | DBMS        | I001          | Bob             |
| S004       | Dave         | C003      | DS          | I003          | Dave            |

- This table is not in 3NF because there are non-transitive dependencies between the non-key attributes. For instance, Course Name depends on Course ID, and Instructor Name depends on Instructor ID, which are both non-key attributes.
- To convert this table into 3NF, we need to decompose it into smaller tables that eliminate the non-transitive dependencies. One possible way to do this is:

| Student ID | Student Name | Course ID |
|------------|--------------|-----------|
| S001       | Alice        | C001      |
| S002       | Bob          | C002      |
| S003       | Carol        | C001      |
| S004       | Dave         | C003      |

| Course ID | Course Name | Instructor ID |
|-----------|-------------|---------------|
| C001      | DBMS        | I001          |
| C002      | OOP         | I002          |
| C003      | DS          | I003          |

| Instructor ID | Instructor Name |
|---------------|-----------------|
| I001          | Bob             |
| I002          | Carol           |
| I003          | Dave            |

- The benefits of 3NF are:

  - It reduces data duplication and storage space.
  - It improves data consistency and accuracy.
  - It facilitates data manipulation and querying.
  - It prevents update, insertion, and deletion anomalies.