### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table  .
- A super key may have additional attributes that are not needed for unique identification .
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table .
- A super key can also be NULL, meaning that it does not have any value.
- A table can have more than one super key, but only one primary key, which is a candidate key chosen by the database designer .
- A super key can be used to enforce referential integrity, which means that the values of a foreign key in one table must match the values of a primary key in another table.

Some examples of super keys are:

- In a table of students, the attributes {student_id, name, email} form a super key, because they can uniquely identify each student. However, this super key is not minimal, because {student_id} alone can also uniquely identify each student. Therefore, {student_id} is a candidate key, and {student_id, name, email} is a super key that contains the candidate key.
- In a table of employees, the attributes {employee_id, name, department, salary} form a super key, because they can uniquely identify each employee. However, this super key is not minimal, because {employee_id} alone can also uniquely identify each employee. Therefore, {employee_id} is a candidate key, and {employee_id, name, department, salary} is a super key that contains the candidate key.
- In a table of books, the attributes {ISBN, title, author, publisher, year} form a super key, because they can uniquely identify each book. However, this super key is not minimal, because {ISBN} alone can also uniquely identify each book. Therefore, {ISBN} is a candidate key, and {ISBN, title, author, publisher, year} is a super key that contains the candidate key.