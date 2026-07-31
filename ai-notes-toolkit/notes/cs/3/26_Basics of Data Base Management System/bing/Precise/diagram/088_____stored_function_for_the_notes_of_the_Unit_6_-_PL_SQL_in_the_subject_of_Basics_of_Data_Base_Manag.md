### Stored Function
A stored function is a subprogram that is stored in the database and can be invoked by SQL statements. It is similar to a stored procedure, with the main difference being that a function returns a value, while a procedure does not. Here are some key points to remember about stored functions in PL/SQL:

1. A stored function can be called from a SELECT statement, while a stored procedure cannot.
2. A stored function must return a value, while a stored procedure does not have to.
3. A stored function can be used in an expression, while a stored procedure cannot.
4. A stored function can be called from another stored function or procedure, while a stored procedure can only be called from another procedure.
5. A stored function can be used in a DML statement, while a stored procedure cannot.

In summary, a stored function is a subprogram that is stored in the database and can be invoked by SQL statements. It is similar to a stored procedure, but it returns a value and can be used in expressions and SELECT statements. It is a powerful tool for encapsulating and reusing code in a database application.