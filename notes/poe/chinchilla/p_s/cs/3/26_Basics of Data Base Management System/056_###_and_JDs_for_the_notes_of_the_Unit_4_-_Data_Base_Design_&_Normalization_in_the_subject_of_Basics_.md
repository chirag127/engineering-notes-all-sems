### Unit 4 - Data Base Design & Normalization

#### Introduction
In this unit, we will learn about database design and normalization. Database design is the process of creating a database schema, while normalization is the process of organizing data in a database to reduce redundancy and dependency.

#### Entity-Relationship Model
The entity-relationship model is a graphical representation of entities and their relationships. It is used to design the database schema. The model consists of entities, attributes, and relationships.

- An entity is a thing or concept that exists independently and can be uniquely identified. For example, a customer, an employee, or a product.
- An attribute is a characteristic of an entity. For example, the name, age, or address of a customer.
- A relationship is a connection between two or more entities. For example, a customer buys a product.

#### Normalization
Normalization is the process of organizing data in a database to reduce redundancy and dependency. It involves breaking down a table into smaller tables to avoid data duplication and ensure data consistency.

There are different levels of normalization, each with its own set of rules. The most common levels are:

- First Normal Form (1NF): Each table has a primary key, and each attribute contains only atomic values.
- Second Normal Form (2NF): Each non-key attribute is dependent on the primary key.
- Third Normal Form (3NF): Each non-key attribute is dependent only on the primary key, and not on any other non-key attribute.

#### Advantages of Normalization
- Reduces data redundancy and inconsistency
- Improves data consistency and accuracy
- Enhances data integrity and reliability
- Simplifies database maintenance and updating

#### Disadvantages of Normalization
- Can result in more tables, which can increase complexity
- May require more joins to retrieve data, which can affect performance
- Can be difficult to implement in some cases, especially for complex databases

#### Conclusion
Database design and normalization are essential concepts in database management. Understanding these concepts and applying them correctly can improve the efficiency, reliability, and accuracy of a database.