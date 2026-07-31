### Normal Forms

Normal forms are used in the process of database normalization to reduce data redundancy and improve data integrity. Normalization is the process of organizing data in a database to minimize data redundancy and dependency. There are several normal forms, including:

1. **First Normal Form (1NF):** A relation is in 1NF if and only if the domain of each attribute contains only atomic values, and the value of each attribute contains only a single value from that domain. In other words, each attribute must contain only one value per tuple.

2. **Second Normal Form (2NF):** A relation is in 2NF if it is in 1NF and every non-prime attribute is fully functionally dependent on the primary key. This means that there should be no partial dependencies, where an attribute depends on only part of the primary key.

3. **Third Normal Form (3NF):** A relation is in 3NF if it is in 2NF and every non-prime attribute is non-transitively dependent on the primary key. This means that there should be no transitive dependencies, where an attribute depends on another attribute that depends on the primary key.

4. **Boyce-Codd Normal Form (BCNF):** A relation is in BCNF if it is in 3NF and for every non-trivial functional dependency X -> Y, X is a superkey. This means that there should be no determinants that are not candidate keys.

5. **Fourth Normal Form (4NF):** A relation is in 4NF if it is in BCNF and has no multi-valued dependencies. This means that there should be no dependencies between two sets of attributes that are independent of the primary key.

6. **Fifth Normal Form (5NF):** A relation is in 5NF if it is in 4NF and every join dependency is implied by the candidate keys. This means that there should be no join dependencies that are not implied by the candidate keys.

These normal forms provide a step-by-step process for organizing data in a database to minimize data redundancy and dependency. By following these normal forms, a database designer can create a well-structured and efficient database.