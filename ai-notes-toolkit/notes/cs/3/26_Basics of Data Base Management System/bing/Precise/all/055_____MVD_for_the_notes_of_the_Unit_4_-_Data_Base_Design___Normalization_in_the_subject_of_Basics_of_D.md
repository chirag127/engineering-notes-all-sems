### MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for **Multi-Valued Dependency**.
- It is a type of dependency in which the presence of one or more rows in a table implies the presence of one or more other rows in the same table.
- MVD is used in the process of database normalization, specifically in the **Fourth Normal Form (4NF)**.
- A table is in 4NF if, for every non-trivial multi-valued dependency X ->> Y, X is a superkey.
- A superkey is a set of attributes that uniquely identifies a tuple in a relation.
- MVD can be used to decompose a relation into smaller relations that are in 4NF.
- This can help to eliminate redundancy and improve the efficiency of the database.
