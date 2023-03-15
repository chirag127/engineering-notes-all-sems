# Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

Normal forms are a set of rules or guidelines for designing relational database tables in a way that reduces data redundancy and improves data integrity. Normalization is the process of applying these rules to a database schema. There are different levels of normal forms, each with more stringent requirements than the previous one. The most common normal forms are:

- **First Normal Form (1NF)**: A table is in 1NF if it does not contain any composite or multi-valued attributes. That is, each attribute should have a single atomic value and each row should have a unique identifier (primary key).
- **Second Normal Form (2NF)**: A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there should be no partial dependencies, where an attribute depends on only a part of the primary key.
- **Third Normal Form (3NF)**: A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there should be no transitive dependencies, where an attribute depends on another attribute that depends on the primary key.
- **Boyce-Codd Normal Form (BCNF)**: A table is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there should be no non-trivial functional dependencies, where a non-key attribute determines another non-key attribute.

The following table shows an example of a table that is not in any normal form and how it can be normalized to different levels:

| Student ID | Name | Course ID | Course Name | Instructor |
|------------|------|-----------|-------------|------------|
| 101        | Alice | CS101     | Programming | Bob        |
| 101        | Alice | CS102     | Data Structures | Carol     |
| 102        | Bob   | CS101     | Programming | Bob        |
| 102        | Bob   | CS103     | Algorithms  | Dave       |
| 103        | Carol | CS102     | Data Structures | Carol     |
| 103        | Carol | CS103     | Algorithms  | Dave       |

This table is not in 1NF because it has a composite attribute (Course ID, Course Name, Instructor) and a multi-valued attribute (Course ID). To convert it to 1NF, we need to split the composite attribute into separate attributes and create a new table for the multi-valued attribute. The result is:

| Student ID | Name  |
|------------|-------|
| 101        | Alice |
| 102        | Bob   |
| 103        | Carol |

| Student ID | Course ID |
|------------|-----------|
| 101        | CS101     |
| 101        | CS102     |
| 102        | CS101     |
| 102        | CS103     |
| 103        | CS102     |
| 103        | CS103     |

| Course ID | Course Name | Instructor |
|-----------|-------------|------------|
| CS101     | Programming | Bob        |
| CS102     | Data Structures | Carol     |
| CS103     | Algorithms  | Dave       |

This table is in 1NF but not in 2NF because the attributes Course Name and Instructor are partially dependent on the primary key Course ID. To convert it to 2NF, we need to remove the partial dependencies and create a new table for the non-key attributes. The result is:

| Student ID | Name  |
|------------|-------|
| 101        | Alice |
| 102        | Bob   |
| 103        | Carol |

| Student ID | Course ID |
|------------|-----------|
| 101        | CS101     |
| 101        | CS102     |
| 102        | CS101     |
| 102        | CS103     |
| 103        | CS102     |
| 103        | CS103     |

| Course ID | Course Name |
|-----------|-------------|
| CS101     | Programming |
| CS102     | Data Structures |
| CS103     | Algorithms  |

| Course Name | Instructor |
|-------------|------------|
| Programming | Bob        |
| Data Structures | Carol     |
| Algorithms  | Dave       |

This table is in 2NF but not in 3NF because the attribute Instructor is transitively dependent on the primary