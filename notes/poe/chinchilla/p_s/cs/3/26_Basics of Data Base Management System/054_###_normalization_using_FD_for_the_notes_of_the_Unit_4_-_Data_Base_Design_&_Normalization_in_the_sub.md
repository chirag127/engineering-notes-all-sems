### Normalization using FD

Normalization is a process of organizing data in a database to reduce redundancy and dependency. It involves breaking down a database into smaller, more manageable tables that are easier to maintain and update. One of the key techniques used in normalization is functional dependency (FD).

Functional dependency is a relationship between two attributes in a table where one attribute determines the value of another attribute. For example, in a table of customer orders, the order number determines the customer name. This is known as a functional dependency between the order number and customer name.

Normalization using FD involves identifying and eliminating redundant data in a database by applying a series of normal forms. There are several normal forms, each with its own set of rules and requirements. Here are some of the most common normal forms:

1. First Normal Form (1NF)
- Eliminates repeating groups and ensures that each table has a primary key.
- A table is in 1NF if each attribute contains only atomic values (i.e., indivisible values).
- Example: A table of customer orders might have repeating groups for multiple items ordered, which can be eliminated by creating a separate table for order items.

2. Second Normal Form (2NF)
- Eliminates partial dependencies.
- A table is in 2NF if it is in 1NF and every non-primary key attribute is fully dependent on the primary key.
- Example: In a table of customer orders, if the order number and item number together determine the quantity ordered, then the item number is partially dependent on the primary key (order number). This can be resolved by creating a separate table for order items.

3. Third Normal Form (3NF)
- Eliminates transitive dependencies.
- A table is in 3NF if it is in 2NF and every non-primary key attribute is non-transitively dependent on the primary key.
- Example: In a table of customer orders, if the order number determines the customer name and the customer name determines the customer address, then the customer address is transitively dependent on the primary key (order number). This can be resolved by creating a separate table for customers.

Advantages of normalization using FD:
- Reduces data redundancy and inconsistency.
- Improves data consistency and accuracy.
- Makes it easier to update and maintain the database.
- Enhances data integrity and security.

Disadvantages of normalization using FD:
- Can result in increased complexity and reduced performance.
- Requires careful planning and analysis to ensure that the normalization process is appropriate for the specific database.

Example:
Consider a table of student grades, with attributes for student ID, course ID, and grade. The student ID determines the student name, and the course ID determines the course name and instructor name. This table is not in 3NF, as the instructor name is transitively dependent on the primary key (student ID, course ID). To normalize the table, we can create separate tables for students, courses, and instructors, with appropriate foreign keys to link the tables together.

Applications:
Normalization using FD is widely used in relational database design, particularly in large and complex databases. It is an essential technique for ensuring data integrity and consistency, and for improving the efficiency and effectiveness of database operations.