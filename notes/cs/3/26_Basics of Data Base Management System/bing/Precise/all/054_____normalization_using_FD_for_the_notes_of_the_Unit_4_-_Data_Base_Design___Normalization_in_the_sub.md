# Normalization using FD

Normalization is the process of organizing data in a database to minimize redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring data integrity. Normalization is achieved by dividing larger tables into smaller, more manageable tables and establishing relationships between them.

Functional dependencies (FDs) play a crucial role in the normalization process. A functional dependency is a relationship between two attributes in which the value of one attribute determines the value of the other attribute. For example, in a table with attributes `Student ID` and `Student Name`, the `Student ID` determines the `Student Name`, so there is a functional dependency between these two attributes.

There are several normal forms, each with its own set of rules and requirements. The most commonly used normal forms are:

1. **First Normal Form (1NF):** A table is in 1NF if it contains no repeating groups or arrays. In other words, each attribute must contain only atomic values, and each row must be unique.

2. **Second Normal Form (2NF):** A table is in 2NF if it is in 1NF and all non-key attributes are dependent on the entire primary key. This means that there should be no partial dependencies, where an attribute depends on only part of the primary key.

3. **Third Normal Form (3NF):** A table is in 3NF if it is in 2NF and there are no transitive dependencies, where a non-key attribute depends on another non-key attribute.

Normalization using FDs involves identifying the functional dependencies in a table and using them to decompose the table into smaller, more normalized tables. This process is repeated until the table is in the desired normal form.

In summary, normalization using FDs is a crucial step in database design that helps to minimize redundancy and dependency, and ensure data integrity. By identifying and using functional dependencies, tables can be decomposed into smaller, more manageable tables that meet the requirements of the desired normal form.