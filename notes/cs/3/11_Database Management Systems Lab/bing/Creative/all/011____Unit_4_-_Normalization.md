## Unit 4 - Normalization

- Normalization is a process of organizing the data in a database to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design so that it achieves the optimal structure composed of atomic elements (i.e. elements that cannot be broken down into smaller parts).
- There are two goals of the normalization process: 
  - Eliminating redundant data (for example, storing the same data in more than one table) and 
  - Ensuring data dependencies make sense (only storing related data in a table). Both of these are worthy goals as they reduce the amount of space a database consumes and ensure that data is logically stored.
- The most common forms of normalization applied to databases are called the normal forms. They are numbered from one (the lowest form of normalization, referred to as first normal form or 1NF) through five (the highest, fifth normal form or 5NF). In practical applications, you'll often see 1NF, 2NF, and 3NF along with the occasional 4NF. Fifth normal form is very rarely seen and won't be discussed in this course.
- The normal forms are cumulative. In other words, to qualify for second normal form, a table must first satisfy the requirements for first normal form. To qualify for third normal form, a table must first satisfy the requirements for second normal form, and so on.
- The following are the definitions and examples of each normal form:

### First Normal Form (1NF)
- A table is in 1NF if it contains no repeating groups of data.
- A repeating group is a set of two or more fields that can occur any number of times in a single record.
- For example, consider the following table that stores the courses taken by students:

| Student ID | Name | Course 1 | Course 2 | Course 3 |
|------------|------|----------|----------|----------|
| 1001       | John | Math     | English  | History  |
| 1002       | Mary | Science  | Art      | NULL     |
| 1003       | Bob  | Music    | NULL     | NULL     |

- This table is not in 1NF because it contains a repeating group of fields: Course 1, Course 2, and Course 3. These fields can store multiple values for each student, but they are not atomic.
- To convert this table into 1NF, we need to remove the repeating group and create a separate table for courses, with a foreign key that references the student table. For example:

| Student ID | Name |
|------------|------|
| 1001       | John |
| 1002       | Mary |
| 1003       | Bob  |

| Student ID | Course |
|------------|--------|
| 1001       | Math   |
| 1001       | English|
| 1001       | History|
| 1002       | Science|
| 1002       | Art    |
| 1003       | Music  |

- Now, each table is in 1NF as it contains only atomic values and no repeating groups.

### Second Normal Form (2NF)
- A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
- A non-key attribute is an attribute that is not part of the primary key.
- A functional dependency is a relationship between two attributes, such that the value of one attribute (the determinant) uniquely determines the value of another attribute (the dependent).
- A full functional dependency is a functional dependency where the entire primary key is the determinant. In other words, removing any attribute from the primary key would make the dependency invalid.
- For example, consider the following table that stores the grades of students in different courses:

| Student ID | Course | Grade | Instructor |
|------------|--------|-------|------------|
| 1001       | Math   | A     | Smith      |
| 1001       | English| B     | Jones      |
| 1002       | Science| C     | Lee        |
| 1002       | Art    | A     | Chen       |
| 1003       | Music  | B     | Davis      |

- The primary key of this table is a composite key of Student ID and Course, as they uniquely identify each record.
- This table is in 1NF, but not in 2NF, because there are some non-key attributes that are not fully functionally dependent on the primary key. For instance, the attribute Instructor is functionally dependent on the attribute Course, but not on the attribute Student ID. This means that the instructor of a course does not