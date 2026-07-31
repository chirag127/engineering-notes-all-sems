### Referential integrity

- Referential integrity is a database concept that ensures that relationships between tables remain consistent .
- It requires that if a value of one attribute (column) of a table references a value of another attribute (either in the same or a different table), then the referenced value must exist.
- It prevents the creation of orphan records, which are records that have no matching data in the related table .
- It also prevents the modification or deletion of referenced data, which would cause inconsistency or data loss .
- Referential integrity can be enforced by using primary keys and foreign keys, which are constraints that link the tables by matching values .
- Primary keys are unique identifiers for each record in a table, and foreign keys are attributes that reference the primary keys of another table .
- For example, in a database that stores information about students and courses, a student table may have a primary key called student_id, and a course table may have a primary key called course_id. A third table, called enrollment, may have a foreign key called student_id that references the student table, and another foreign key called course_id that references the course table. This way, the enrollment table can store the information about which students are enrolled in which courses, and maintain referential integrity between the tables.
- Referential integrity can also be enforced by using triggers, which are actions that are executed automatically when a certain event occurs in the database.
- Triggers can be used to check the validity of the referenced data, and perform appropriate actions such as rejecting the operation, cascading the changes, or setting default values.
- For example, a trigger can be defined on the student table to prevent the deletion of a student record if the student is enrolled in any course, or to cascade the deletion to the enrollment table if the student is not enrolled in any course.