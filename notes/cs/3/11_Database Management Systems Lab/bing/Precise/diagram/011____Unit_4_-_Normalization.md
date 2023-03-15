## Unit 4 - Normalization

Normalization is the process of organizing data in a database. This includes creating tables and establishing relationships between those tables according to rules designed to protect the data and make the database more flexible by eliminating redundancy and inconsistent dependency.

There are several levels of normalization, each with its own set of rules and guidelines. These levels are referred to as normal forms and include:

1. **First Normal Form (1NF):** Each table cell should contain a single value and each record needs to be unique.
2. **Second Normal Form (2NF):** All non-key attributes are dependent on the primary key.
3. **Third Normal Form (3NF):** All data in a table must be dependent only on the primary key and not on any other non-key attributes.
4. **Boyce-Codd Normal Form (BCNF):** This is a slightly stronger version of the Third Normal Form and ensures that there are no determinants in the table that are not candidate keys.
5. **Fourth Normal Form (4NF):** A table is in 4NF if it has no multi-valued dependencies.
6. **Fifth Normal Form (5NF):** A table is in 5NF if it cannot be further decomposed without loss of data.

Normalization helps to reduce data redundancy and improve data integrity. It is an important step in the design of a database and should be carefully considered during the planning phase.