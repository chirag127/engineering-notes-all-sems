# Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

Normal forms are a set of rules or guidelines for designing relational database tables in a way that reduces data redundancy and improves data integrity. Normalization is the process of applying these rules to a database schema. There are different levels of normalization, called normal forms, that correspond to different conditions that a table must satisfy. The higher the normal form, the more normalized the table is. The most common normal forms are:

- **First Normal Form (1NF)**: A table is in 1NF if it does not contain any composite or multi-valued attributes. This means that each attribute has a single value and each row has a unique identifier (primary key).
- **Second Normal Form (2NF)**: A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there are no partial dependencies, where an attribute depends on only a part of the primary key.
- **Third Normal Form (3NF)**: A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there are no transitive dependencies, where an attribute depends on another attribute that depends on the primary key.
- **Boyce-Codd Normal Form (BCNF)**: A table is in BCNF if it is in 3NF and every determinant is a candidate key. This means that there are no non-trivial functional dependencies, where a non-key attribute determines another non-key attribute.

The following table shows an example of a table that is not normalized and how it can be transformed into different normal forms by decomposing it into smaller tables.

| Student ID | Name | Course ID | Course Name | Instructor |
|------------|------|-----------|-------------|------------|
| 101        | Alice | CS101     | Programming | Bob        |
| 101        | Alice | CS102     | Data Structures | Carol     |
| 102        | Bob   | CS101     | Programming | Bob        |
| 103        | Carol | CS103     | Database Systems | Dave      |
| 103        | Carol | CS104     | Operating Systems | Eve       |

- This table is not in 1NF because it has a composite attribute (Student ID, Course ID) as the primary key and a multi-valued attribute (Course Name, Instructor) for each course.
- To convert it to 1NF, we can split the table into two tables: one for students and one for courses. The primary key of the students table is Student ID and the primary key of the courses table is Course ID. We also add a foreign key (Student ID) to the courses table to link it to the students table.

| Student ID | Name  |
|------------|-------|
| 101        | Alice |
| 102        | Bob   |
| 103        | Carol |

| Course ID | Course Name | Instructor | Student ID |
|-----------|-------------|------------|------------|
| CS101     | Programming | Bob        | 101        |
| CS102     | Data Structures | Carol     | 101        |
| CS101     | Programming | Bob        | 102        |
| CS103     | Database Systems | Dave      | 103        |
| CS104     | Operating Systems | Eve       | 103        |

- These tables are in 1NF but not in 2NF because the courses table has a partial dependency: Course Name and Instructor depend on Course ID, not on the whole primary key (Course ID, Student ID).
- To convert it to 2NF, we can split the courses table into two tables: one for course details and one for course enrollments. The primary key of the course details table is Course ID and the primary key of the course enrollments table is (Course ID, Student ID). We also add a foreign key (Course ID) to the course enrollments table to link it to the course details table.

| Course ID | Course Name | Instructor |
|-----------|-------------|------------|
| CS101     | Programming | Bob        |
| CS102     | Data Structures | Carol     |
| CS103     | Database Systems | Dave      |
| CS104     | Operating Systems | Eve       |

| Course ID | Student ID |
|-----------|------------|
| CS101     | 101        |
| CS102     | 101        |
| CS101     |