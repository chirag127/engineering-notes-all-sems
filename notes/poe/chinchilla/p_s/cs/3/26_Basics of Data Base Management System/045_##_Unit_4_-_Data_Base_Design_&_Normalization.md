## Unit 4 - Data Base Design & Normalization

In this unit, we will learn about database design and normalization. Database design is the process of creating a database schema, which includes defining tables, columns, and relationships between tables. Normalization is a technique used to reduce data redundancy and improve data integrity.

### Database Design

- A database schema is a blueprint of a database that specifies the tables, columns, and relationships between the tables.
- The tables in a database should be designed in a way that minimizes data redundancy and maximizes data integrity.
- The columns in a table should be carefully chosen and named to accurately represent the data they hold.
- Relationships between tables can be one-to-one, one-to-many, or many-to-many. These relationships are defined through foreign keys.
- The process of database design includes identifying the entities and relationships in a system, creating an ER diagram, and converting the ER diagram into a database schema.

### Normalization

- Normalization is a technique used to reduce data redundancy and improve data integrity in a database.
- Normalization involves breaking down a table into smaller, more specialized tables that are related to each other by primary and foreign keys.
- There are several levels of normalization, including first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on.
- Each level of normalization has specific rules that must be followed in order to achieve the desired level of normalization.
- Normalization can improve data integrity by reducing the likelihood of data anomalies, such as update, insertion, and deletion anomalies.

### Advantages of Normalization

- Normalization can improve data integrity by reducing data redundancy and ensuring that each piece of data is stored in only one place.
- Normalization can simplify database design by breaking down complex tables into smaller, more specialized tables.
- Normalization can make it easier to modify and update a database schema.

### Disadvantages of Normalization

- Normalization can be time-consuming and complex, especially when dealing with large and complex databases.
- Over-normalization can lead to complex queries and decreased performance.
- Normalization can sometimes result in the need for multiple joins to retrieve data from related tables.

### Examples of Normalization

- Consider a database of customers and their orders. A denormalized table might include all of the customer information and all of their orders in a single table. A normalized table might include a customers table and an orders table, with a foreign key linking the two tables.
- Consider a database of employees and their departments. A denormalized table might include all of the employee information and all of the department information in a single table. A normalized table might include an employees table and a departments table, with a foreign key linking the employees table to the departments table.

### Applications of Normalization

- Normalization is commonly used in relational databases to improve data integrity and reduce data redundancy.
- Normalization can be used in any application that involves storing and retrieving data from a database.
- Normalization is especially useful in applications where data integrity is critical, such as financial applications or healthcare applications.