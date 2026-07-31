### Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

- Normal forms are used to eliminate or reduce redundancy in database tables and to ensure data integrity.
- Normalization is the process of structuring a relational database in accordance with a series of normal forms.
- There are different levels of normal forms, each with more stringent requirements than the previous one. The most common normal forms are 1NF, 2NF, 3NF, and BCNF.
- A relation is in 1NF if it does not contain any composite or multi-valued attribute. That is, each attribute should be atomic and have a single value for each tuple.
- A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there should be no partial dependency of any attribute on the primary key.
- A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there should be no transitive dependency of any attribute on the primary key.
- A relation is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there should be no dependency of any attribute on a non-key attribute.
- Normalization helps to avoid anomalies such as insertion, deletion, and update anomalies that can occur when data is redundant or inconsistent.
- Normalization also helps to improve the performance and efficiency of the database by reducing the size of the tables and the number of joins required.
- Normalization has some drawbacks such as increased complexity, loss of information, and reduced query flexibility.