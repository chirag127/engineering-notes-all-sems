### Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

- Normal forms are a set of rules or guidelines for designing relational databases in a way that reduces data redundancy and improves data integrity .
- Normal forms are based on the concept of functional dependency, which is a relationship between two sets of attributes in a relation such that the values of one set determine the values of the other set .
- There are different levels of normal forms, each with more stringent requirements than the previous one. The most common normal forms are first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF)   .
- A relation is said to be in a certain normal form if it satisfies the conditions of that normal form and all the lower normal forms. For example, a relation in 3NF is also in 2NF and 1NF .
- The main benefits of normalizing a database are:
  - It eliminates or reduces data duplication, which saves storage space and improves performance .
  - It ensures data consistency and accuracy, which prevents data anomalies and errors .
  - It facilitates data manipulation and querying, which makes it easier to retrieve and update data .
- The main drawbacks of normalizing a database are:
  - It may increase the number of tables and joins, which can complicate the database design and query processing .
  - It may reduce the efficiency of some queries that require denormalized data, which can affect performance and usability .
  - It may not capture all the business rules and constraints, which can lead to data integrity violations .
- The process of normalizing a database involves the following steps:
  - Identify all the candidate keys and functional dependencies in the relation .
  - Decompose the relation into smaller relations that satisfy the conditions of the desired normal form .
  - Check for any data anomalies or integrity violations in the normalized relations .
  - Refine the normalized relations if necessary to improve the database design .