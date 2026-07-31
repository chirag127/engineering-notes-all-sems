# Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

## Introduction

- Database normalization is a database design principle for organizing data in an organized and consistent way.
- It helps you avoid redundancy and maintain the integrity of the database.
- It also helps you eliminate undesirable characteristics associated with insertion, deletion, and updating.
- Normal forms are used to eliminate or reduce redundancy in database tables.
- Normal forms are based on the concept of functional dependency, which is a relationship between two or more attributes of a table.
- A table is said to be in a certain normal form if it satisfies certain conditions or rules.

## Types of Normal Forms in DBMS

- Normal forms are of four major forms: 1NF, 2NF, 3NF, and BCNF.
- A majority of the database systems have their databases normalized up to the 3NF in DBMS.
- But here are the normal forms that are used in DBMS:

### 1NF (First Normal Form)

- A table is in 1NF if it does not contain any composite or multi-valued attribute.
- A composite attribute is an attribute that can be further divided into sub-attributes, such as address, name, etc.
- A multi-valued attribute is an attribute that can have more than one value for a given entity, such as hobbies, skills, etc.
- To convert a table into 1NF, we need to split the composite and multi-valued attributes into separate attributes and create a new table for each multi-valued attribute with a foreign key referencing the original table.

### 2NF (Second Normal Form)

- A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
- A functional dependency is a relationship between two or more attributes of a table, such that the value of one attribute determines the value of another attribute.
- A non-key attribute is an attribute that is not part of the primary key.
- A primary key is a set of attributes that uniquely identifies each record in a table.
- A full functional dependency is a functional dependency where the entire set of attributes in the primary key is required to determine the value of another attribute.
- To convert a table into 2NF, we need to identify the partial dependencies, where a non-key attribute depends on only a part of the primary key, and remove them by creating a new table with the dependent attributes and a foreign key referencing the original table.

### 3NF (Third Normal Form)

- A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
- A transitive dependency is a functional dependency where a non-key attribute depends on another non-key attribute, which in turn depends on the primary key.
- To convert a table into 3NF, we need to identify the transitive dependencies and remove them by creating a new table with the dependent attributes and a foreign key referencing the original table.

### BCNF (Boyce-Codd Normal Form)

- A table is in BCNF if it is in 3NF and every determinant is a candidate key.
- A determinant is an attribute or a set of attributes that determines the value of another attribute or a set of attributes.
- A candidate key is a set of attributes that can uniquely identify each record in a table and is a minimal subset of the superkey.
- A superkey is a set of attributes that can uniquely identify each record in a table.
- To convert a table into BCNF, we need to identify the dependencies where a determinant is not a candidate key and remove them by creating a new table with the dependent attributes and a foreign key referencing the original table.

## Conclusion

- Normal forms are a way of ensuring that the database design is optimal and free of anomalies.
- Normal forms are based on the concept of functional dependency, which is a relationship between two or more attributes of a table.
- Normal forms are of four major forms: 1NF, 2NF, 3NF, and BCNF.
- Each normal form has a set