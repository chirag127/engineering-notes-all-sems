 Here is the content in markdown format for the given topic:

### Database Design & Normalization (Unit 3 Notes)

1. Database Design
- The design of a database involves planning a logical and physical structure of database to accommodate the data needs of an organization.
- The main goal of database design is to make the database as simple as possible and ensure data consistency, minimize data redundancy and make the data access efficient.
- The steps involved in database design are:
-- Determining requirements: Gathering requirements, analyzing users' needs, understanding the nature of data.
-- Conceptual design: Identifying entities and relationships, creating Entity-Relationship (ER) diagrams.
-- Logical design: Translating ER diagrams into tables, establishing relationships between tables.
-- Physical design: Deciding data types for attributes, size of tables, indexes, etc.

2. Normalization
- Normalization is a process of organizing the data in a database by ensuring:
-- Atomicity: The attribute values should be atomic.
-- Consistency: The attribute values should be consistent.
-- Dependency: The attributes should have dependencies.

There are three normal forms:
1NF: The table has unique column names. No two rows have identical data in all columns.
2NF: The table is in 1NF and has no partial dependency. No non-prime attribute is dependent on a proper subset of a candidate key.
3NF: The table is in 2NF and has no transitive dependency. No non-prime attribute is dependent on other non-prime attributes.

[Additional details, diagrams, examples can be added here for better understanding]