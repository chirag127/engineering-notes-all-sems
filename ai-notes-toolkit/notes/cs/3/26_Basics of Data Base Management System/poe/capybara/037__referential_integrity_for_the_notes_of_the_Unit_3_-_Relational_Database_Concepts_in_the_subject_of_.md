### Referential Integrity

Relational databases rely on the concept of referential integrity to ensure that data is consistent and accurate. Referential integrity is a set of rules that governs the relationships between tables in a database.

Here are some key points to understand about referential integrity:

- Referential integrity ensures that data in related tables is consistent. For example, if you have a table of orders and a table of customers, referential integrity ensures that every order is associated with a valid customer.
- Referential integrity is enforced through the use of foreign keys. A foreign key is a column in one table that refers to the primary key of another table.
- When you create a relationship between two tables, you can specify how referential integrity should be enforced. For example, you can specify that deleting a customer should also delete all associated orders.
- Enforcing referential integrity can help prevent data inconsistencies, such as orphaned records or invalid relationships.
- Referential integrity can also help improve performance by allowing the database to optimize queries and reduce the need for joins.

When working with relational databases, it is important to understand and follow referential integrity rules to ensure data accuracy and consistency.