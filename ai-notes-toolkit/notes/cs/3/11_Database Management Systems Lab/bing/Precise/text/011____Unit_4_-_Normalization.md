## Unit 4 - Normalization

Normalization is a process of organizing data in a database. It involves dividing larger tables into smaller, more manageable tables and establishing relationships between them. The goal of normalization is to minimize data redundancy and improve data integrity.

There are several levels of normalization, commonly referred to as normal forms. Each normal form has a set of rules that must be followed in order to achieve that level of normalization. The most commonly used normal forms are:

1. **First Normal Form (1NF):** Each table cell should contain a single value and there should be no repeating groups.
2. **Second Normal Form (2NF):** All non-key attributes should be dependent on the entire primary key.
3. **Third Normal Form (3NF):** All non-key attributes should be directly dependent on the primary key and not on any other non-key attribute.
4. **Boyce-Codd Normal Form (BCNF):** For every non-trivial functional dependency, the determinant must be a candidate key.

Normalization can help to improve the efficiency and flexibility of a database, but it is not always necessary or desirable. In some cases, denormalization (the opposite of normalization) may be used to improve performance. It is important to carefully consider the needs of the database and its users when deciding on the appropriate level of normalization.