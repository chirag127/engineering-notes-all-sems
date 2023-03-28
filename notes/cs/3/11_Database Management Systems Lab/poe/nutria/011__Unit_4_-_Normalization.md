
## Unit 4 - Normalization

1. Normalization is the process of reorganizing data in a database so that it meets two basic requirements:
    * Elimination of redundant data (for example, storing the same data in more than one table)
    * Ensuring data dependencies make sense (only storing related data in a table)
2. Normalization usually involves dividing a database into two or more tables and defining relationships between the tables. The objective is to isolate data so that additions, deletions, and modifications of a field can be made in just one table and then propagated through the rest of the database via the defined relationships.
3. Normalization is typically a refinement process after the initial exercise of identifying the data objects that should be in the database, identifying their relationships, and defining the tables and columns.
4. There are two main objectives of the normalization process:
    * Eliminate redundant data
    * Ensure data dependencies make sense
5. Normalization typically involves decomposing a table into smaller (and less redundant) tables, while still ensuring that the data dependencies make sense.
6. There are several normal forms, and the higher the normal form, the less redundancy is present in the data. The normal forms are:
    * First Normal Form (1NF)
    * Second Normal Form (2NF)
    * Third Normal Form (3NF)
    * Boyce-Codd Normal Form (BCNF)
7. In order to achieve a higher normal form, the lower normal forms must first be satisfied. For example, a database must be in 2NF before it can be in 3NF.