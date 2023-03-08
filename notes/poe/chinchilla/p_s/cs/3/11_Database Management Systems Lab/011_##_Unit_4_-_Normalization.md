## Unit 4 - Normalization

Normalization is the process of organizing data in a database to reduce redundancy and dependency. It is an essential technique that helps to avoid data inconsistencies, update anomalies and ensure data integrity. In this unit, we will learn the different levels of normalization and how they are applied to a database.

### Levels of Normalization

There are several levels of normalization, each with its set of rules and requirements. The most common levels of normalization are:

#### 1. First Normal Form (1NF)

The first normal form (1NF) requires that each column in a table must contain atomic values. That is, a column should not contain multiple values or a set of values. It also requires that each table should have a primary key that uniquely identifies each row.

#### 2. Second Normal Form (2NF)

The second normal form (2NF) requires that a table must be in 1NF and every non-key attribute should be dependent on the primary key. That is, there should be no partial dependencies, where a non-key attribute depends on only a part of the primary key.

#### 3. Third Normal Form (3NF)

The third normal form (3NF) requires that a table must be in 2NF and every non-key attribute should be dependent only on the primary key. That is, there should be no transitive dependencies, where a non-key attribute depends on another non-key attribute.

#### 4. Boyce-Codd Normal Form (BCNF)

The Boyce-Codd Normal Form (BCNF) requires that a table must be in 3NF and every determinant should be a candidate key. That is, there should be no overlapping candidate keys or functional dependencies.

### Advantages of Normalization

- Normalization helps to eliminate data redundancy, which reduces storage space and improves database performance.
- Normalization ensures data consistency and integrity, as it reduces the likelihood of update anomalies.
- Normalization makes it easier to maintain and modify the database, as changes can be made without affecting other parts of the database.

### Disadvantages of Normalization

- Normalization can lead to more complex database structures, which can be difficult to understand and maintain.
- Normalization can result in more joins, which can reduce database performance.

### Examples of Normalization

Consider the following table:

| Customer ID | Customer Name | Product ID | Product Name | Quantity |
|-------------|---------------|------------|--------------|----------|
| 1           | John Smith    | 1          | Laptop       | 2        |
| 1           | John Smith    | 2          | Printer      | 1        |
| 2           | Jane Doe      | 1          | Laptop       | 1        |
| 2           | Jane Doe      | 3          | Monitor      | 2        |

This table is not normalized since it contains redundant data. We can normalize it by creating two separate tables:

Customers:

| Customer ID | Customer Name |
|-------------|---------------|
| 1           | John Smith    |
| 2           | Jane Doe      |

Products:

| Product ID | Product Name |
|------------|--------------|
| 1          | Laptop       |
| 2          | Printer      |
| 3          | Monitor      |

Orders:

| Order ID | Customer ID | Product ID | Quantity |
|----------|-------------|------------|----------|
| 1        | 1           | 1          | 2        |
| 2        | 1           | 2          | 1        |
| 3        | 2           | 1          | 1        |
| 4        | 2           | 3          | 2        |

### Applications of Normalization

Normalization is widely used in database design to ensure data consistency and integrity. It is essential in applications such as:

- Banking and finance, where data accuracy is critical.
- E-commerce, where data consistency is essential to avoid errors in orders and payments.
- Healthcare, where data integrity is vital for patient safety.

In conclusion, normalization is a crucial database design technique that helps to ensure data consistency, integrity and performance. Understanding the different levels of normalization and how they can be applied to a database is essential for anyone involved in database design and management.