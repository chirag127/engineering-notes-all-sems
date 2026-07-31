# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accurately represent the real-world domain and its rules.
  - Ensure data integrity, consistency, and quality.
  - Support efficient data access and manipulation.
  - Facilitate data security and privacy.
  - Allow for data scalability and maintainability.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization helps in achieving the following benefits :
  - Improved database design: Normalization helps in improving the overall design of the database. By organizing the data in a structured and systematic way, normalization makes it easier to design and maintain the database. It also makes the database more flexible and adaptable to changing business needs.
  - Reduced data anomalies: Normalization helps in avoiding data anomalies, such as insertion, deletion, and update anomalies, that can occur due to data redundancy and inconsistency. Normalization ensures that each piece of data is stored in only one place, and that any changes to the data are reflected in all the related tables.
  - Enhanced data security: Normalization helps in enhancing data security by allowing for more granular access control and auditing. Normalization allows for defining different levels of permissions and privileges for different tables and columns, and for tracking the changes made to the data by different users.
  - Increased data efficiency: Normalization helps in increasing data efficiency by reducing the storage space and improving the performance of data operations. Normalization eliminates the need to store duplicate data, and thus saves disk space and memory. Normalization also simplifies the queries and transactions, and thus reduces the network traffic and processing time.

## Normal Forms
- Normal forms are the rules or standards that define the degree of normalization of a database schema.
- Normal forms are based on the concept of functional dependencies, which are the relationships between the attributes of a table that determine how one attribute can be derived from another attribute or a set of attributes.
- Normal forms are applied sequentially, starting from the lowest level (first normal form) to the highest level (fifth normal form), to progressively reduce the redundancy and dependency of data in a database schema.
- The most commonly used normal forms are  :
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values, i.e., each attribute can have only one value for each record, and there are no repeating groups of attributes, i.e., each record can have only one instance of each attribute.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., each non-key attribute can be uniquely identified by the primary key, and not by any subset of the primary key.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., each non-key attribute can be uniquely identified by the primary key, and not by any other non-key attribute or a set of non-key attributes.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., each attribute or a set of attributes that can determine the value of another attribute or a set of attributes is a potential primary key.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and it has no multi-valued dependencies, i.e., there are no attributes or a set of attributes that can have more than one value for a single record, and that are independent of the primary key.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and it has no join dependencies, i.e., there are no subsets of attributes that can be joined together to form the original table, and that are not implied