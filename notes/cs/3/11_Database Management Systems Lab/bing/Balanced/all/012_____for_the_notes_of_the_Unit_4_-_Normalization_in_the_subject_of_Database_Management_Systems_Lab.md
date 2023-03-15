# Normalization in Database Management Systems

Normalization is a technique to reduce data redundancy and improve data integrity in a database. It involves dividing a large table into smaller tables based on certain rules, and linking them using foreign keys. The main benefits of normalization are:

- It avoids anomalies, such as insertion, deletion, and update anomalies, that can cause inconsistency and duplication of data.
- It reduces the storage space required for the database, as it eliminates repeated data.
- It simplifies the queries and operations on the database, as it reduces the number of joins and columns involved.
- It enhances the security and performance of the database, as it allows for better access control and indexing.

There are different levels of normalization, called normal forms, that define how well a table is normalized. The most common normal forms are:

- First Normal Form (1NF): A table is in 1NF if it has no repeating groups of attributes, and each attribute has a single value for each record. For example, a table that stores the name, address, and phone numbers of customers is not in 1NF, as it has a repeating group of phone numbers. To convert it to 1NF, we need to create a separate table for phone numbers, and link it to the customer table using a foreign key.
- Second Normal Form (2NF): A table is in 2NF if it is in 1NF and has no partial dependencies, meaning that each non-key attribute depends on the whole primary key, and not on a subset of it. For example, a table that stores the order details of customers, such as order number, customer ID, product ID, product name, and product price, is not in 2NF, as the product name and price depend only on the product ID, and not on the order number or customer ID. To convert it to 2NF, we need to create a separate table for products, and link it to the order table using a foreign key.
- Third Normal Form (3NF): A table is in 3NF if it is in 2NF and has no transitive dependencies, meaning that each non-key attribute depends only on the primary key, and not on any other non-key attribute. For example, a table that stores the customer details, such as customer ID, name, address, city, state, and zip code, is not in 3NF, as the city, state, and zip code depend on the address, and not on the customer ID. To convert it to 3NF, we need to create a separate table for addresses, and link it to the customer table using a foreign key.

There are other higher normal forms, such as Boyce-Codd Normal Form (BCNF), Fourth Normal Form (4NF), and Fifth Normal Form (5NF), that deal with more complex dependencies and constraints, but they are not commonly used in practice. The general rule of thumb is to normalize a table up to 3NF, unless there is a specific reason to go further or stop earlier.