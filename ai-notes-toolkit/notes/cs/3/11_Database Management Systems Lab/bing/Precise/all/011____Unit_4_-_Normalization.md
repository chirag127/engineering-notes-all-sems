## Unit 4 - Normalization

Normalization is a process of organizing data in a database. It involves dividing larger tables into smaller, less redundant tables and defining relationships between them. The main goal of normalization is to minimize data redundancy and dependency.

There are several levels of normalization, also known as normal forms. Each normal form has a set of rules that must be followed in order to achieve that level of normalization. The most commonly used normal forms are:

1. **First Normal Form (1NF):** Each table cell should contain a single value and there should be no repeating groups.
2. **Second Normal Form (2NF):** All non-key attributes should be dependent on the entire primary key.
3. **Third Normal Form (3NF):** All non-key attributes should be directly dependent on the primary key and not on any other non-key attribute.
4. **Boyce-Codd Normal Form (BCNF):** This is a stronger version of 3NF where all determinants must be candidate keys.

Normalization helps to reduce data redundancy and improve data integrity. However, it is important to note that normalization is not always the best solution for every situation. In some cases, denormalization may be necessary for performance reasons.