### Normal Forms

Normal forms are used in database design to reduce data redundancy and eliminate undesirable characteristics like insertion, update and deletion anomalies. Normalization typically involves dividing a database into smaller and less redundant tables and defining relationships between them. The objective is to isolate data so that additions, deletions, and modifications of a field can be made in just one table and then propagated through the rest of the database using the defined relationships.

There are several normal forms, including:

1. **First Normal Form (1NF):** Each table cell should contain a single value and each record needs to be unique.
2. **Second Normal Form (2NF):** All non-key attributes are dependent on the primary key.
3. **Third Normal Form (3NF):** All data in a table must be dependent only on the primary key and not on any other non-key attributes.
4. **Boyce-Codd Normal Form (BCNF):** For every non-trivial functional dependency X → Y, X must be a superkey.
5. **Fourth Normal Form (4NF):** A table should not have multi-valued dependencies.
6. **Fifth Normal Form (5NF):** Also known as Project-Join Normal Form (PJNF), a table should not have join dependencies that are not implied by the candidate keys.

These normal forms are used to progressively eliminate redundancy and improve the design of a database. It is important to note that normalization is not always the best approach and that denormalization may be necessary in some cases to improve performance. However, normalization is a crucial step in the design of a well-structured and efficient database.