### Normal Forms for the Notes of the Unit 4 - Database Design & Normalization in the Subject of Basics of Database Management System

In the process of database design and development, normalization is a crucial step that is used to organize the data in a more efficient and effective manner. Normalization is a process of removing data redundancy and improving data consistency by breaking down large tables into smaller, more manageable tables. In this section, we will discuss the various normal forms that are used in the database design process.

#### First Normal Form (1NF)

The first normal form (1NF) is the most basic level of normalization. It states that all tables must have a primary key, and all attributes must have atomic values (i.e., indivisible values). In other words, each column in a table should contain only one value, and each value should be unique.

#### Second Normal Form (2NF)

The second normal form (2NF) builds upon the first normal form. It states that a table must be in 1NF and that all non-key attributes must be fully dependent on the primary key. In other words, a table should not have any partial dependencies.

#### Third Normal Form (3NF)

The third normal form (3NF) builds upon the second normal form. It states that a table must be in 2NF and that all non-key attributes must be independent of each other. In other words, a table should not have any transitive dependencies.

#### Boyce-Codd Normal Form (BCNF)

The Boyce-Codd normal form (BCNF) is an extension of the third normal form. It states that a table must be in 3NF and that all functional dependencies must be on the primary key. In other words, a table should not have any overlapping candidate keys.

#### Fourth Normal Form (4NF)

The fourth normal form (4NF) is used to eliminate multi-valued dependencies. It states that a table must be in BCNF and that all non-key attributes must be independent of each other. In other words, a table should not have any non-trivial multi-valued dependencies.

#### Fifth Normal Form (5NF)

The fifth normal form (5NF) is also known as the projection-join normal form. It is used to eliminate join dependencies. It states that a table must be in 4NF and that all join dependencies must be implied by the candidate keys.

In conclusion, normalization is a crucial step in the database design process. By breaking down large tables into smaller, more manageable tables, we can improve data consistency, eliminate data redundancy, and improve overall database performance. The various normal forms provide guidelines for designing normalized databases that are efficient, effective, and easy to use.