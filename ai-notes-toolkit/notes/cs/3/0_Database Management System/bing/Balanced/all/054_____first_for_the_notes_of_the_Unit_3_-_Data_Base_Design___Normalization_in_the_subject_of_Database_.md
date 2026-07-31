# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, establishing the relationships and constraints, and choosing the appropriate data models and storage formats.
- Database design aims to achieve the following objectives:
  - Accuracy: The database should accurately represent the real-world domain and the business rules of the application.
  - Efficiency: The database should allow fast and easy access, insertion, update, and deletion of data, while minimizing the storage space and processing overhead.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Flexibility: The database should be able to accommodate changing data requirements and business needs, and support new features and functionalities.

## Normalization
- Normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity and organization of data.
- Normalization helps in achieving the following benefits:
  - Improved Database Design: Normalization helps in improving the overall design of the database. By organizing the data in a structured and systematic way, normalization makes it easier to design and maintain the database. It also makes the database more flexible and adaptable to changing business needs.
  - Reduced Data Anomalies: Normalization helps in reducing the data anomalies, such as insertion, update, and deletion anomalies, that may arise due to redundant and dependent data. Data anomalies can cause data inconsistency and corruption, and affect the quality and reliability of the database.
  - Enhanced Data Integrity: Normalization helps in enhancing the data integrity, by enforcing the constraints and rules on the data. Data integrity ensures that the data is valid, accurate, and consistent, and conforms to the business logic and expectations.
  - Optimized Performance: Normalization helps in optimizing the performance of the database, by reducing the data duplication and the number of joins required to retrieve the data. Normalization also facilitates the use of indexes and query optimization techniques, which can improve the speed and efficiency of the database operations.

## Normal Forms
- Normal forms are the standards or rules that define the level of normalization of a database schema. Normal forms are based on the concept of functional dependencies, which describe the relationship between the attributes of a table.
- Functional dependency: A functional dependency is a constraint that specifies that the value of one or more attributes (called the determinant) determines the value of another attribute (called the dependent).
- For example, in a table that stores the student ID, name, and email of students, the student ID determines the name and email of the student. This can be written as: student ID -> name, email
- The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values, i.e., each attribute has a single value for each tuple (row), and there are no repeating groups of attributes.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no dependencies on non-key attributes.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, i.e., there are no attributes that depend on a set of attributes rather than a single attribute.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and there are no join dependencies, i.e., there are no attributes that depend on the combination of two or more tables rather than a single table.