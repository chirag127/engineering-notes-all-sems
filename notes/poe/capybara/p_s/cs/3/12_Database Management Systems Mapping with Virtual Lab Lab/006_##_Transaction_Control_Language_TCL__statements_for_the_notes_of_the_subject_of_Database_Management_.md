## Transaction Control Language(TCL) statements

Transaction Control Language(TCL) statements are used to manage transactions in a database. These statements are responsible for creating, modifying, and deleting transactions in a database.

### Types of TCL Statements

There are three types of TCL statements:

1. COMMIT statement: The COMMIT statement is used to make the changes made in a transaction permanent. Once a COMMIT statement is executed, the changes made in the transaction are written to the database.

2. ROLLBACK statement: The ROLLBACK statement is used to undo the changes made in a transaction. If a transaction is not committed and a ROLLBACK statement is executed, the changes made in the transaction are undone.

3. SAVEPOINT statement: The SAVEPOINT statement is used to create a savepoint within a transaction. A savepoint is a point in a transaction where you can rollback the transaction to if necessary.

### Advantages of TCL Statements

- TCL statements provide a way to manage transactions in a database.
- They can be used to ensure data consistency in a database.
- They provide a way to undo changes made in a transaction if necessary.

### Disadvantages of TCL Statements

- Overuse of TCL statements can lead to performance issues in a database.
- Improper use of TCL statements can lead to data inconsistency in a database.

### Example

```
BEGIN TRANSACTION;
UPDATE customers SET balance = balance - 100 WHERE customer_id = 1;
SAVEPOINT my_savepoint;
UPDATE customers SET balance = balance + 100 WHERE customer_id = 2;
ROLLBACK TO my_savepoint;
COMMIT;
```

In this example, we start a transaction and update the balance of a customer with ID 1. Then we create a savepoint within the transaction and update the balance of a customer with ID 2. We then rollback the transaction to the savepoint we created and finally commit the transaction.

### Applications

TCL statements are commonly used in applications that require database transactions. These applications include:

- E-commerce websites
- Banking applications
- Inventory management systems
- Order processing systems

In conclusion, TCL statements are an important part of managing transactions in a database. They provide a way to ensure data consistency and can be used to undo changes made in a transaction if necessary. However, improper use of TCL statements can lead to performance issues and data inconsistency, so it is important to use them appropriately.