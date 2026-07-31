## Unit 4 - Data Base Design & Normalization

Database design is the process of producing a detailed data model of a database. This data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design. A well-designed database is easy to maintain, improves data consistency, and is cost-effective in terms of disk storage space.

Normalization is the process of organizing a database in a way that reduces redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored logically. The different levels of normalization are called normal forms.

1. **First Normal Form (1NF):** Each table cell should contain a single value and each record needs to be unique.
2. **Second Normal Form (2NF):** All non-key attributes are dependent on the primary key.
3. **Third Normal Form (3NF):** All data in a table must be dependent only on the primary key and not on any other non-key attributes.
4. **Boyce-Codd Normal Form (BCNF):** This is a higher version of the Third Normal Form and is used when there are more than one candidate keys in a table.
5. **Fourth Normal Form (4NF):** A table is in 4NF if it has no multi-valued dependencies.
6. **Fifth Normal Form (5NF):** A table is in 5NF if it has no join dependencies.

Normalization helps to reduce data redundancy and improve data integrity. However, it is important to note that normalization is not always the best approach, as it can result in more complex database designs and reduced performance. It is important to strike a balance between normalization and performance when designing a database.