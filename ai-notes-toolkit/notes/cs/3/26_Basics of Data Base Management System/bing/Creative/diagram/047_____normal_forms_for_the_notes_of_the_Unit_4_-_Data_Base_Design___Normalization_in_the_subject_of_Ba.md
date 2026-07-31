Hello, I am Sydney, your AI assistant. I can help you with your topic of normal forms for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System. Here is some information that I have gathered from the web:

### Normal Forms in DBMS

- Normal forms are used to eliminate or reduce redundancy in database tables.
- Normal forms are based on the concept of functional dependency, which is a relationship between two or more attributes of a table.
- Normal forms are of four major forms: 1NF, 2NF, 3NF, and BCNF. A majority of the database systems have their databases normalized up to the 3NF in DBMS.
- There are also other higher normal forms, such as 4NF, 5NF, and 6NF, but they are rarely used in practice.

#### First Normal Form (1NF)

- A table is in 1NF if it does not contain any composite or multi-valued attribute.
- A composite attribute is an attribute that can be further divided into sub-attributes, such as name, address, etc.
- A multi-valued attribute is an attribute that can have more than one value for a given entity, such as hobbies, skills, etc.
- To convert a table into 1NF, we need to split the composite and multi-valued attributes into separate attributes and create a new table for each multi-valued attribute with a foreign key referencing the original table.

#### Second Normal Form (2NF)

- A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
- A functional dependency is a relationship between two or more attributes of a table, such that the value of one attribute determines the value of another attribute.
- A non-key attribute is an attribute that is not part of the primary key or any candidate key of the table.
- A primary key is a set of attributes that uniquely identifies each record in the table.
- A candidate key is a set of attributes that can uniquely identify each record in the table and is a potential primary key.
- To convert a table into 2NF, we need to remove the partial dependencies, which are the dependencies of non-key attributes on a subset of the primary key, and create a new table for each partial dependency with a foreign key referencing the original table.

#### Third Normal Form (3NF)

- A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
- A transitive dependency is a dependency of a non-key attribute on another non-key attribute that is dependent on the primary key.
- To convert a table into 3NF, we need to remove the transitive dependencies and create a new table for each transitive dependency with a foreign key referencing the original table.

#### Boyce-Codd Normal Form (BCNF)

- A table is in BCNF if it is in 3NF and every determinant is a candidate key.
- A determinant is an attribute or a set of attributes that determines the value of another attribute or a set of attributes.
- To convert a table into BCNF, we need to remove the dependencies of non-key attributes on non-candidate keys and create a new table for each dependency with a foreign key referencing the original table.

I hope this information is helpful for your study. If you have any questions or need more details, please let me know.😊