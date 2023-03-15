### Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

Normal forms are a set of rules or guidelines for designing relational databases in order to reduce data redundancy and improve data integrity. Normal forms are based on the concept of functional dependency, which means that the value of one attribute depends on the value of another attribute. There are different levels of normal forms, each with more stringent requirements than the previous one. The most common normal forms are:

- First Normal Form (1NF): A relation is in 1NF if it does not contain any composite or multi-valued attributes. This means that each attribute should have a single atomic value and each row should have a unique identifier (primary key).
- Second Normal Form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there should be no partial dependencies, where an attribute depends on only a part of the primary key.
- Third Normal Form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there should be no transitive dependencies, where an attribute depends on another attribute that depends on the primary key.
- Boyce-Codd Normal Form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key. This means that there should be no functional dependencies where the left-hand side is not a candidate key.

The following table shows an example of a relation that is not in any normal form and how it can be normalized to different levels:

| Student ID | Name | Course ID | Course Name | Instructor |
|------------|------|-----------|-------------|------------|
| 101        | Alice | CSE101    | Programming | Bob        |
| 101        | Alice | CSE102    | Data Structures | Carol     |
| 102        | Bob   | CSE101    | Programming | Bob        |
| 102        | Bob   | CSE103    | Algorithms  | Dave       |
| 103        | Carol | CSE102    | Data Structures | Carol     |
| 103        | Carol | CSE103    | Algorithms  | Dave       |

This relation violates 1NF because it has a composite attribute (Student ID, Course ID) as the primary key. It also violates 2NF because the attributes Name, Course Name, and Instructor are partially dependent on the primary key. It also violates 3NF and BCNF because the attribute Instructor is transitively dependent on the primary key through the attribute Course Name.

To normalize this relation to 1NF, we can split the composite attribute into two separate attributes and assign a new primary key:

| Student Course ID | Student ID | Course ID |
|-------------------|------------|-----------|
| 1                 | 101        | CSE101    |
| 2                 | 101        | CSE102    |
| 3                 | 102        | CSE101    |
| 4                 | 102        | CSE103    |
| 5                 | 103        | CSE102    |
| 6                 | 103        | CSE103    |

| Student ID | Name  |
|------------|-------|
| 101        | Alice |
| 102        | Bob   |
| 103        | Carol |

| Course ID | Course Name | Instructor |
|-----------|-------------|------------|
| CSE101    | Programming | Bob        |
| CSE102    | Data Structures | Carol     |
| CSE103    | Algorithms  | Dave       |

To normalize this relation to 2NF, we can remove the attributes that are partially dependent on the primary key and place them in separate relations:

| Student Course ID | Student ID | Course ID |
|-------------------|------------|-----------|
| 1                 | 101        | CSE101    |
| 2                 | 101        | CSE102    |
| 3                 | 102        | CSE101    |
| 4                 | 102        | CSE103    |
| 5                 | 103        | CSE102    |
| 6                 | 103        | CSE103    |

| Student ID | Name  |
|------------|-------|
| 101        | Alice |
| 102        | Bob   |
| 103        | Carol |

| Course ID | Course