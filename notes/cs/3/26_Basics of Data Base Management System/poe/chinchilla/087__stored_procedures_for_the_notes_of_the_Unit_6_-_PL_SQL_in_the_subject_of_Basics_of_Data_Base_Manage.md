### Stored Procedures for the Notes of Unit 6 - PL/SQL in the Subject of Basics of Database Management System

Stored procedures are an essential part of PL/SQL programming. A stored procedure is a precompiled program that can be called by other programs or users to perform a specific task. It is a module of code that can be reused and shared among different applications. In this unit, we will discuss the basics of stored procedures in PL/SQL.

Here are some important points to note about stored procedures:

- A stored procedure is a set of SQL statements that are compiled and stored in the database.
- It is executed by calling the procedure name from another program or user.
- Stored procedures can be used to perform complex operations that involve multiple SQL statements.
- They can be used to encapsulate business logic and provide a secure and efficient way of accessing and manipulating data.
- Stored procedures can be used to improve performance by reducing network traffic and improving response times.
- They can be used to automate repetitive tasks and provide a standard way of performing operations across different applications.
- Stored procedures can be written in PL/SQL, which is a procedural language that extends SQL with programming constructs such as loops, variables, and control structures.

Here are some steps to create a stored procedure in PL/SQL:

1. Define the procedure name and input/output parameters.
2. Write the SQL statements that will be executed by the procedure.
3. Compile the procedure using the CREATE PROCEDURE statement.
4. Test the procedure by executing it from another program or user.

Here is an example of a stored procedure that retrieves the details of a customer from the database:

```sql
CREATE PROCEDURE get_customer_details (cust_id IN NUMBER, 
                                       cust_name OUT VARCHAR2,
                                       cust_email OUT VARCHAR2)
IS
BEGIN
  SELECT customer_name, customer_email
  INTO cust_name, cust_email
  FROM customers
  WHERE customer_id = cust_id;
END;
```

In this example, the procedure takes an input parameter `cust_id` and two output parameters `cust_name` and `cust_email`. It retrieves the customer details from the database and assigns them to the output parameters.

To call this procedure from another program or user, you would use the following syntax:

```sql
DECLARE
  customer_name VARCHAR2(50);
  customer_email VARCHAR2(50);
BEGIN
  get_customer_details(1, customer_name, customer_email);
  DBMS_OUTPUT.PUT_LINE('Customer Name: ' || customer_name);
  DBMS_OUTPUT.PUT_LINE('Customer Email: ' || customer_email);
END;
```

In this example, we are calling the `get_customer_details` procedure with the customer ID of 1. The procedure returns the customer name and email, which we assign to the `customer_name` and `customer_email` variables. We then display the results using the `DBMS_OUTPUT.PUT_LINE` statement.

In conclusion, stored procedures are an important part of PL/SQL programming. They provide a way of encapsulating business logic and improving performance by reducing network traffic and improving response times. By following the steps outlined above, you can create your own stored procedures and use them to perform complex operations in your applications.