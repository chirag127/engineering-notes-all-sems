### Unit 4 - Normalization in Database Management Systems Lab

Normalization is the process of organizing data in a database to minimize redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way. Normalization typically involves dividing a database into smaller, more focused tables and defining relationships between those tables.

There are several levels of normalization, known as normal forms. Each normal form has a set of rules that must be followed in order to achieve that level of normalization. The most commonly used normal forms are:

1. **First Normal Form (1NF):** This normal form requires that all data in a table be atomic, meaning that each attribute contains only one value and there are no repeating groups or arrays.
2. **Second Normal Form (2NF):** This normal form requires that a table be in 1NF and that all non-key attributes be dependent on the entire primary key.
3. **Third Normal Form (3NF):** This normal form requires that a table be in 2NF and that there be no transitive dependencies between non-key attributes.
4. **Boyce-Codd Normal Form (BCNF):** This normal form is a stronger version of 3NF that requires that for every non-trivial functional dependency, the determinant is a superkey.

Normalization can help to improve the efficiency and flexibility of a database, but it is not always necessary or desirable. In some cases, denormalization, or the intentional introduction of redundancy, can improve performance or simplify the design of a database.