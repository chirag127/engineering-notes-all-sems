### Normalization using FD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

Normalization is the process of organizing data in a database to reduce redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way. Normalization is achieved by dividing larger tables into smaller, more manageable tables and establishing relationships between them.

Functional dependencies (FDs) play a crucial role in the normalization process. A functional dependency is a relationship between two attributes in which the value of one attribute determines the value of the other attribute. For example, in a table containing employee data, the employee's ID number determines their name, address, and other personal information. This is written as EmployeeID -> EmployeeName, EmployeeAddress, etc.

There are several normal forms, each with its own set of rules and requirements. The most commonly used normal forms are:

1. First Normal Form (1NF): This normal form requires that all data in a table be atomic, meaning that each attribute contains only one value and there are no repeating groups or arrays.

2. Second Normal Form (2NF): This normal form requires that a table be in 1NF and that all non-key attributes be dependent on the entire primary key.

3. Third Normal Form (3NF): This normal form requires that a table be in 2NF and that there be no transitive dependencies, meaning that non-key attributes are not dependent on other non-key attributes.

Normalization using FDs involves identifying the functional dependencies in a table and using them to decompose the table into smaller, more manageable tables that meet the requirements of the desired normal form. This process can be iterative, with each normal form building on the previous one.

In summary, normalization is an important process in database design that helps to reduce redundancy and dependency. Functional dependencies play a crucial role in this process, allowing for the decomposition of larger tables into smaller, more manageable ones that meet the requirements of the desired normal form. By following the rules of normalization and using FDs, a well-designed and efficient database can be created.