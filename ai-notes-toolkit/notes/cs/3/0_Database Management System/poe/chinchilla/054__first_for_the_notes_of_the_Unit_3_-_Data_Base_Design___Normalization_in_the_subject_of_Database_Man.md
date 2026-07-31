### Unit 3: Database Design & Normalization

Database design is the process of creating a database schema that represents the requirements of the system. The schema defines the structure of the database, including tables, columns, and relationships between them. Normalization is a technique used in database design to eliminate redundancy and improve data integrity.

#### Entity-Relationship Model

The entity-relationship (ER) model is a graphical representation of the database schema. It defines entities (objects or concepts) and their relationships. The ER model consists of:

- Entity: A real-world object or concept that has attributes (properties) and can be uniquely identified. For example, a customer, an order, or a product.
- Attribute: A property of an entity, such as the name or the age of a customer.
- Relationship: A connection between two or more entities. For example, an order is placed by a customer.

#### Normalization

Normalization is a process of organizing the data in a database to reduce redundancy and improve data integrity. There are several normal forms, each with its own set of rules to achieve normalization. The most commonly used normal forms are:

- First Normal Form (1NF): Eliminate repeating groups and create a separate table for each set of related data.
- Second Normal Form (2NF): Eliminate partial dependencies by removing columns that depend on only part of the primary key.
- Third Normal Form (3NF): Eliminate transitive dependencies by removing columns that depend on non-key attributes.

#### Denormalization

Denormalization is the process of intentionally adding redundancy to a database schema to improve performance. Denormalization can be used when querying the database is more frequent than updating it. However, it should be used with caution as it can lead to data inconsistency and complexity.

#### Summary

- Database design is the process of creating a database schema that represents the requirements of the system.
- The ER model is a graphical representation of the database schema that defines entities, attributes, and relationships between them.
- Normalization is a technique used in database design to eliminate redundancy and improve data integrity.
- Denormalization is the process of intentionally adding redundancy to a database schema to improve performance.
- Normalization should be used to achieve data integrity, while denormalization should be used to improve performance only when necessary.