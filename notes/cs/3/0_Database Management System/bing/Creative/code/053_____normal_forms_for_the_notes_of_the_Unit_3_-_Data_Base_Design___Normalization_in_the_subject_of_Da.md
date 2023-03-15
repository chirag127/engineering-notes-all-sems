### Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

Normal forms are a set of rules or guidelines for designing relational database tables in a way that reduces data redundancy and improves data integrity. Normal forms are based on the concept of functional dependency, which is a relationship between two or more attributes of a table. A functional dependency means that the value of one attribute determines the value of another attribute. For example, in a table of students, the student ID determines the name, email, and phone number of the student.

There are different levels of normal forms, each with a stricter set of requirements than the previous one. The most common normal forms are:

- First normal form (1NF): A table is in 1NF if it does not contain any composite or multi-valued attributes. A composite attribute is an attribute that can be further divided into sub-attributes, such as address or name. A multi-valued attribute is an attribute that can have more than one value for a given entity, such as hobbies or skills. To convert a table to 1NF, we need to split the composite and multi-valued attributes into separate attributes or tables.

- Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. A non-key attribute is an attribute that is not part of the primary key, which is a set of attributes that uniquely identifies each row in the table. A full functional dependency means that the value of a non-key attribute depends only on the whole primary key, not on a subset of it. To convert a table to 2NF, we need to remove the partial dependencies, which are the dependencies of non-key attributes on a subset of the primary key, by creating new tables with the dependent attributes and the subset of the primary key.

- Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. A non-transitive dependency means that the value of a non-key attribute depends only on the primary key, not on another non-key attribute. To convert a table to 3NF, we need to remove the transitive dependencies, which are the dependencies of non-key attributes on other non-key attributes, by creating new tables with the dependent attributes and the determinant attributes.

- Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key. A determinant is an attribute or a set of attributes that determines the value of another attribute. A candidate key is a set of attributes that can uniquely identify each row in the table and is a minimal subset of the superkey, which is a set of attributes that can uniquely identify each row in the table but may contain redundant attributes. To convert a table to BCNF, we need to remove the anomalies, which are the inconsistencies or redundancies that may occur when inserting, deleting, or updating data, by creating new tables with the dependent attributes and the determinant attributes.

The following table shows an example of a table that is not in any normal form and how to convert it to each normal form.

| Student ID | Name | Address | Phone | Course ID | Course Name | Instructor |
|------------|------|---------|-------|-----------|-------------|------------|
| 101        | Alice | 123 Main St, Seattle, WA | 555-1111 | CS101 | Introduction to Computer Science | Bob |
| 102        | Bob | 456 Elm St, Seattle, WA | 555-2222 | CS101 | Introduction to Computer Science | Bob |
| 103        | Charlie | 789 Pine St, Seattle, WA | 555-3333 | CS102 | Data Structures and Algorithms | Alice |
| 104        | David | 101 Maple St, Seattle, WA | 555-4444 | CS102 | Data Structures and Algorithms | Alice |
| 105        | Eve | 202 Oak St, Seattle, WA | 555-5555 | CS103 | Database Systems | Charlie |

To convert this table to 1NF, we need to split the composite attribute Address into Street, City, and State. We also need to assign a unique name to each attribute.

| Student_ID | Student_Name | Street | City | State | Phone | Course_ID | Course_Name | Instructor_Name |
|------------|--------------|--------|------|-------|-------|-----------|-------------|-----------------|
|