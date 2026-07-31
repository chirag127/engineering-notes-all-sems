### Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

Normal forms are a set of rules or guidelines for designing relational databases in order to reduce data redundancy and improve data integrity. Normal forms are based on the concept of functional dependency, which means that the value of one attribute depends on the value of another attribute. There are different levels of normal forms, each with more stringent requirements than the previous one. The most common normal forms are:

- **First Normal Form (1NF):** A relation is in 1NF if it does not contain any composite or multi-valued attributes. This means that each attribute should have a single atomic value and each row should have a unique identifier (primary key).
- **Second Normal Form (2NF):** A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there should be no partial dependencies, where an attribute depends on only a part of the primary key.
- **Third Normal Form (3NF):** A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there should be no transitive dependencies, where an attribute depends on another non-key attribute that depends on the primary key.
- **Boyce-Codd Normal Form (BCNF):** A relation is in BCNF if it is in 3NF and every determinant is a candidate key. This means that there should be no functional dependencies where the left-hand side is not a candidate key.

The following table shows an example of a relation that is not in any normal form and how it can be normalized to different levels:

| Student ID | Name | Course | Instructor | Office |
|------------|------|--------|------------|--------|
| 101        | Alice | CS101 | Bob        | A101   |
| 102        | Bob   | CS102 | Carol      | A102   |
| 103        | Carol | CS101 | Bob        | A101   |
| 104        | Dave  | CS102 | Carol      | A102   |

- To convert this relation to 1NF, we need to remove the composite attribute Course, which contains both the course code and the instructor name. We can split it into two separate attributes: Course Code and Instructor Name. The resulting relation is:

| Student ID | Name | Course Code | Instructor Name | Office |
|------------|------|-------------|-----------------|--------|
| 101        | Alice | CS101       | Bob             | A101   |
| 102        | Bob   | CS102       | Carol           | A102   |
| 103        | Carol | CS101       | Bob             | A101   |
| 104        | Dave  | CS102       | Carol           | A102   |

- To convert this relation to 2NF, we need to remove the partial dependencies, where the Office attribute depends on the Instructor Name attribute, which is only a part of the primary key (Student ID, Course Code). We can do this by creating a new relation for the instructors and referencing it from the original relation. The resulting relations are:

| Student ID | Name | Course Code |
|------------|------|-------------|
| 101        | Alice | CS101       |
| 102        | Bob   | CS102       |
| 103        | Carol | CS101       |
| 104        | Dave  | CS102       |

| Instructor Name | Office |
|-----------------|--------|
| Bob             | A101   |
| Carol           | A102   |

- To convert this relation to 3NF, we need to remove the transitive dependencies, where the Name attribute depends on the Student ID attribute, which depends on the primary key (Student ID, Course Code). We can do this by creating a new relation for the students and referencing it from the original relation. The resulting relations are:

| Student ID | Course Code |
|------------|-------------|
| 101        | CS101       |
| 102        | CS102       |
| 103        | CS101       |
| 104        | CS102       |

| Student ID | Name |
|------------|------|
| 101        | Alice |
| 102        | Bob   |
| 103        | Carol |
| 104        | Dave  |

| Instructor Name | Office |
|-----------------|--------|
| Bob             | A101   |