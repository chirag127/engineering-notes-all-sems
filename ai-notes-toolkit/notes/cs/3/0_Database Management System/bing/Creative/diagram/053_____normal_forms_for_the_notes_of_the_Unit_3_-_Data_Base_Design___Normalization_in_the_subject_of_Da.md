### Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

Normal forms are a set of rules or guidelines for designing relational database tables in a way that reduces data redundancy and improves data integrity. Normalization is the process of applying these rules to a database schema. There are different levels of normal forms, each with more stringent requirements than the previous one. The most common normal forms are:

- **First Normal Form (1NF):** A table is in 1NF if it does not contain any composite or multi-valued attributes. This means that each column should store only one value of a single data type, and each row should have a unique identifier (primary key).
- **Second Normal Form (2NF):** A table is in 2NF if it is in 1NF and it does not contain any partial dependencies. This means that each non-key column should depend on the whole primary key, and not on a subset of it. For example, if a table has a composite primary key of (student_id, course_id), then the grade column should depend on both student_id and course_id, and not on student_id alone.
- **Third Normal Form (3NF):** A table is in 3NF if it is in 2NF and it does not contain any transitive dependencies. This means that each non-key column should depend only on the primary key, and not on any other non-key column. For example, if a table has a primary key of student_id, and a non-key column of student_name, then the student_address column should depend on student_id, and not on student_name.
- **Boyce-Codd Normal Form (BCNF):** A table is in BCNF if it is in 3NF and it does not contain any non-trivial functional dependencies that are not implied by the candidate keys. This means that each determinant (a set of columns that determines another column) should be a candidate key (a minimal set of columns that uniquely identifies a row). For example, if a table has two candidate keys of (student_id, course_id) and (student_name, course_name), then the grade column should depend on either of them, and not on any other combination of columns.

The benefits of normalizing a database are:

- It reduces data duplication and storage space.
- It improves data consistency and integrity.
- It simplifies data manipulation and querying.
- It facilitates data security and maintenance.

The drawbacks of normalizing a database are:

- It may increase the number of tables and joins, which can affect performance and complexity.
- It may lose some information that is implicit in the original data structure.
- It may not suit some application requirements that need denormalized data.