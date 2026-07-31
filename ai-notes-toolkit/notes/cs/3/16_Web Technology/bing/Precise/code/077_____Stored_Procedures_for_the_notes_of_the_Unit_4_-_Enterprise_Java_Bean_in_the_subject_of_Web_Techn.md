### Stored Procedures

Stored procedures are a type of database object that can be used to encapsulate a series of SQL statements into a single, reusable routine. They are commonly used in enterprise applications to perform complex data manipulation tasks, such as inserting, updating, or deleting data in multiple tables.

Some benefits of using stored procedures include:

1. Improved performance: Since stored procedures are pre-compiled, they can execute more quickly than dynamic SQL statements.
2. Reduced network traffic: By encapsulating multiple SQL statements into a single stored procedure, the amount of data sent between the application and the database server can be reduced.
3. Enhanced security: Stored procedures can be used to enforce data access controls, by only allowing certain users to execute specific procedures.
4. Easier maintenance: By centralizing data manipulation logic into stored procedures, it can be easier to make changes to the application's data access layer.

In the context of Enterprise Java Beans (EJB), stored procedures can be called from session beans using the Java Database Connectivity (JDBC) API. This allows EJBs to interact with the database in a more efficient and secure manner.