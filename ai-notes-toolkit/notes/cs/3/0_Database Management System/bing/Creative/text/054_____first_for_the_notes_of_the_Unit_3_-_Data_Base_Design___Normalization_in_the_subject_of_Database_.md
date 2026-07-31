### Unit 3 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database normalization is a technique of database design that aims to reduce data redundancy and dependency by splitting a large table into smaller tables and defining relationships between them.
- The benefits of database normalization are:
  - It improves the clarity and consistency of the data and its relationships.
  - It avoids data anomalies such as insertion, deletion, and update anomalies that can cause data inconsistency and corruption.
  - It reduces the storage space and improves the performance of the database system.
  - It makes the database more flexible and adaptable to changing business requirements.
- The drawbacks of database normalization are:
  - It may increase the number of tables and joins, which can complicate the queries and affect the performance of the database system.
  - It may lose some information that is derived from the original table, such as the total amount of an order or the average salary of an employee.
  - It may not be suitable for some applications that require denormalized data for analytical or reporting purposes.
- The process of database normalization involves applying a series of rules or normal forms to a table until it satisfies a certain level of normalization. The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute is atomic or indivisible.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key or the whole key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key or the whole key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key or a superkey.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and it has no multivalued dependencies or independent relationships between non-key attributes.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and it has no join dependencies or lossless decompositions that are not implied by the candidate keys.
- The steps to normalize a table are:
  - Identify the functional dependencies and candidate keys of the table.
  - Check if the table is in 1NF and eliminate any repeating groups or multivalued attributes by creating new tables and establishing foreign key relationships.
  - Check if the table is in 2NF and eliminate any partial dependencies by creating new tables and establishing foreign key relationships.
  - Check if the table is in 3NF and eliminate any transitive dependencies by creating new tables and establishing foreign key relationships.
  - Check if the table is in BCNF and eliminate any non-key determinants that are not candidate keys by creating new tables and establishing foreign key relationships.
  - Check if the table is in 4NF and eliminate any multivalued dependencies by creating new tables and establishing foreign key relationships.
  - Check if the table is in 5NF and eliminate any join dependencies that are not implied by the candidate keys by creating new tables and establishing foreign key relationships.
- An example of database normalization is:

  - Consider a table called Employee that stores the employee ID, name, department, salary, and projects of each employee in a company.

  | EmployeeID | Name | Department | Salary | Projects |
  | --- | --- | --- | --- | --- |
  | 101 | Alice | Sales | 5000 | A, B |
  | 102 | Bob | Marketing | 6000 | B, C |
  | 103 | Charlie | Sales | 7000 | A, C |
  | 104 | David | Marketing | 8000 | C, D |

  - The functional dependencies of the table are:

    - EmployeeID -> Name, Department, Salary
    - Department -> Salary
    - EmployeeID, Project -> Project

  - The candidate keys of the table are:

    - EmployeeID
    - EmployeeID, Project

  - The table is not in 1NF because it has a multivalued attribute (Projects) that can have more than one value for each employee.

  - To convert the table to 1NF, we create a new table called EmployeeProject that stores the employee ID