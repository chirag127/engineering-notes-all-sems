### Third Normal Forms

In database management system, normalization is the process of organizing data in a database in a way that reduces redundancy and dependency. Third Normal Forms (3NF) is the next level of normalization after Second Normal Forms (2NF). Here are some important points to keep in mind when understanding 3NF.

#### What is 3NF?

Third Normal Forms (3NF) is a database normalization technique that ensures that every non-key attribute in a table is dependent only on the primary key. In simpler terms, a table is in 3NF if it has no repeating groups and every non-key attribute is dependent on the primary key. 

#### How to achieve 3NF?

To achieve 3NF, we have to follow the three normal form rules:

1. The table must be in Second Normal Form (2NF).
2. The table must not have any transitive functional dependencies.
3. All non-key attributes must be dependent on the primary key.

#### Advantages of 3NF

- Eliminates redundancy and dependency in the database.
- Improves data consistency and accuracy.
- Enhances database performance and speed.
- Facilitates easy maintenance and updates.

#### Disadvantages of 3NF

- Can result in more complex database design.
- May require extra effort in designing the database schema.

#### Examples of 3NF

Consider a table called "Orders" with the following attributes:

- Order ID (primary key)
- Customer ID
- Customer Name
- Product ID
- Product Name
- Product Description
- Order Date
- Quantity
- Total Price

Here, "Order ID" is the primary key and every other attribute is dependent on it. However, "Customer Name" is also dependent on "Customer ID" which is not part of the primary key. To make it in 3NF, we have to separate the customer details into a separate table.

#### Applications of 3NF

- Used in designing complex databases with multiple tables and relationships.
- Suitable for large-scale enterprise applications where data consistency and accuracy are critical.

In conclusion, 3NF is an important concept in database normalization that helps in achieving data consistency, accuracy and efficiency. It is essential to understand the rules and guidelines of 3NF to design a robust and reliable database schema.