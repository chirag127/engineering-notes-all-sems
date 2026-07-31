### Normal Forms for the Notes of the Unit 3 - Data Base Design & Normalization in the Subject of Database Management System

- Normal forms are a set of rules or guidelines for designing relational database tables in a way that reduces data redundancy and improves data integrity.
- Normal forms are based on the concept of functional dependency, which is a relationship between two or more attributes of a table such that the value of one attribute determines the value of another attribute.
- There are different levels of normal forms, each with a stricter set of requirements than the previous one. The most common normal forms are first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF).
- A table is said to be in a certain normal form if it satisfies all the conditions of that normal form and all the previous normal forms. For example, a table is in 3NF if it is in 2NF and also satisfies the 3NF condition.
- The main benefits of normalizing a database are:
  - It eliminates or reduces data duplication, which saves storage space and improves performance.
  - It ensures data consistency and accuracy, which prevents data anomalies and errors.
  - It facilitates data manipulation and querying, which simplifies the database design and maintenance.

- The main drawbacks of normalizing a database are:
  - It may increase the number of tables and joins, which can affect the complexity and efficiency of some queries.
  - It may require more foreign keys and indexes, which can increase the overhead of insert, update, and delete operations.
  - It may not reflect the natural or logical structure of some data domains, which can affect the usability and understandability of the database.

- The following are the definitions and examples of the common normal forms:

  - First normal form (1NF): A table is in 1NF if it does not contain any composite or multi-valued attributes, i.e., each attribute has a single atomic value. For example, a table that stores the name, address, and phone numbers of customers is not in 1NF if the phone number attribute can have multiple values for a customer. To convert it to 1NF, we can either split the phone number attribute into separate attributes for each type of phone number (e.g., home, work, mobile), or create a separate table for phone numbers with a foreign key reference to the customer table.

  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there is no partial dependency. For example, a table that stores the order details of customers is not in 2NF if it has a composite primary key of order ID and product ID, and also has attributes such as customer name, product name, and product price. In this case, the customer name is partially dependent on the order ID, and the product name and price are partially dependent on the product ID. To convert it to 2NF, we can create separate tables for customers, products, and orders, and link them with foreign keys.

  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there is no transitive dependency. For example, a table that stores the order details of customers is not in 3NF if it has attributes such as order ID, customer ID, customer address, product ID, product name, and product price. In this case, the customer address is transitively dependent on the customer ID, and the product name and price are transitively dependent on the product ID. To convert it to 3NF, we can remove the customer address, product name, and product price from the order table, and store them in the customer and product tables respectively.

  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there is no non-trivial functional dependency where the left-hand side is not a superkey. For example, a table that stores the enrollment details of students is not in BCNF if it has attributes such as student ID, course ID, instructor ID, and grade. In this case, the instructor ID determines the course ID, which is a non-trivial functional dependency where the left-hand side is not a superkey. To convert it to BCNF, we can split the table into two tables, one