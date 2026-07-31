# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database system.
- Database design involves identifying the entities, attributes, and relationships that are relevant to the problem domain and organizing them into tables and columns.
- Database design also involves defining the constraints, indexes, views, triggers, and other database objects that are needed to ensure data integrity, security, and performance.
- Database design follows a set of principles and guidelines to ensure that the database is well-structured, normalized, and easy to maintain and query.

## Normalization
- Normalization is a database design technique that reduces data redundancy and improves data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- Normalization also simplifies the database design by eliminating unnecessary or redundant data and ensuring that each table contains only related data.
- Normalization is a progressive process that involves applying different levels of normal forms to the database design. Each level of normalization has a specific goal and a set of criteria that must be met before moving to the next level.
- The most common levels of normalization are:

  - First normal form (1NF): Each column in a table must contain atomic values, meaning that they cannot be further divided into smaller parts. There should be no repeating groups or arrays of values in a single column. Each row in a table must have a unique identifier or primary key.
  - Second normal form (2NF): Each column in a table that is not part of the primary key must depend on the whole primary key, meaning that there should be no partial dependencies. A partial dependency occurs when a column depends on only a subset of the primary key. For example, if a table has a composite primary key of (student_id, course_id), then the column grade should depend on both student_id and course_id, not just one of them.
  - Third normal form (3NF): Each column in a table that is not part of the primary key must depend only on the primary key, meaning that there should be no transitive dependencies. A transitive dependency occurs when a column depends on another column that is not part of the primary key. For example, if a table has a primary key of student_id and a column of student_name, then the column student_address should depend on student_id, not on student_name.
  - Boyce-Codd normal form (BCNF): Each column in a table that is not part of a candidate key (a minimal set of columns that can uniquely identify a row) must depend on the whole candidate key, meaning that there should be no partial dependencies. This is a stronger version of 2NF that applies to tables that have more than one candidate key. For example, if a table has two candidate keys of (student_id, course_id) and (student_name, course_name), then the column grade should depend on both student_id and course_id, and on both student_name and course_name, not just one of them.
  - Fourth normal form (4NF): Each column in a table that is not part of a candidate key must depend on the whole candidate key, and there should be no multi-valued dependencies. A multi-valued dependency occurs when a column can have more than one value for a given combination of values in the candidate key. For example, if a table has a candidate key of (student_id, course_id) and a column of hobbies, then the column hobbies should not have multiple values for the same student_id and course_id combination.
  - Fifth normal form (5NF): Each column in a table that is not part of a candidate key must depend on the whole candidate key, and there should be no join dependencies. A join dependency occurs when a table can be decomposed into two or more tables and then reconstructed by joining them on their candidate keys without losing any information. For example, if a table has a candidate key of (student_id, course_id, instructor_id) and columns of student_name, course_name, instructor_name, and grade, then the table can be decomposed into three tables of (student_id, student_name), (course_id, course_name), and (instructor_id, instructor_name), and then reconstructed by joining them on their candidate keys without losing any information.

- Normalization has many benefits, such as:

  - Reducing data duplication and storage space
  - Improving data consistency and accuracy
  - Enhancing data security and integrity
  - Facilitating data manipulation and querying
  - Increasing database performance and scalability
  - Simplifying database maintenance