Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of normalization in database management systems.

# Normalization in Database Management Systems

Normalization is a technique to reduce data redundancy and improve data integrity in a database. It involves dividing a large table into smaller tables based on certain rules, and linking them with foreign keys. The main benefits of normalization are:

- It avoids anomalies, such as insertion, deletion, and update anomalies, that can occur when data is duplicated or inconsistent in a database.
- It saves storage space by eliminating redundant data.
- It enhances query performance by reducing the number of joins and scans required.
- It facilitates data consistency and integrity by enforcing constraints and relationships among tables.

## Normal Forms

Normal forms are the levels or stages of normalization that a database can achieve. Each normal form has a set of criteria or rules that a table must satisfy to be in that normal form. The higher the normal form, the more normalized the database is. The most common normal forms are:

- First Normal Form (1NF): A table is in 1NF if it has no repeating groups or arrays, and every attribute is atomic, meaning it cannot be further subdivided. For example, a table that stores the name, address, and phone number of a customer is in 1NF if each attribute is a single value and not a composite value, such as a full name or a street address.
- Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be derived from any other attribute or subset of attributes. For example, a table that stores the order details of a customer is in 2NF if the order number is the primary key and every other attribute, such as the product name, quantity, and price, depends only on the order number and not on any other attribute, such as the customer name or the product category.
- Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be derived from any other non-key attribute. For example, a table that stores the product details of an order is in 3NF if the product ID is the primary key and every other attribute, such as the product name, category, and supplier, depends only on the product ID and not on any other attribute, such as the supplier name or the category name.
- Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies among the attributes. A determinant is an attribute or a set of attributes that uniquely determines another attribute or a set of attributes. For example, a table that stores the employee details of a department is in BCNF if the employee ID is the primary key and the department name is the only other attribute, and there are no other attributes that can determine the department name or the employee ID.

## Examples

Here are some examples of tables in different normal forms.

### Unnormalized Table

| Order Number | Customer Name | Product ID | Product Name | Product Category | Quantity | Price | Supplier Name |
| ------------ | ------------- | ---------- | ------------ | ---------------- | -------- | ----- | ------------- |
| 1001         | Alice         | P001       | Laptop       | Electronics      | 1        | 500   | Tech Inc.     |
| 1002         | Bob           | P002       | Book         | Education        | 2        | 20    | Edu Ltd.      |
| 1002         | Bob           | P003       | Pen          | Stationery       | 5        | 5     | Sta Co.       |
| 1003         | Charlie       | P004       | Shirt        | Clothing         | 3        | 30    | Clo Ltd.      |

This table is not in 1NF because it has a repeating group, the product details, for each order number. It also has data redundancy and anomalies, such as:

- The customer name is repeated for each order number, which wastes storage space and can cause inconsistency if the customer name changes.
- The product name, category, and supplier are repeated for each product ID, which wastes storage space and can cause inconsistency if the product details change.
- The price is repeated for each product ID and quantity, which wastes storage space and can cause inconsistency if the price