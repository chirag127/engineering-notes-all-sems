### Procedures in SQL/PL SQL

A procedure is a named PL/SQL block that performs one or more actions. Procedures are similar to functions, but they do not return a value. Instead, they are used to perform actions such as modifying the database or interacting with other PL/SQL blocks.

Here are some key points to remember about procedures in SQL/PL SQL:

1. Procedures are created using the `CREATE PROCEDURE` statement.
2. Procedures can accept input parameters, which are passed to the procedure using the `IN` keyword.
3. Procedures can also have output parameters, which are used to return values from the procedure using the `OUT` keyword.
4. Procedures can be called from other PL/SQL blocks, or from other procedures or functions.
5. Procedures can be used to perform a wide range of actions, including data manipulation, transaction control, and error handling.

Here is an example of a simple procedure that accepts an input parameter and uses it to update a record in the database:

```sql
CREATE PROCEDURE update_employee_salary (emp_id IN NUMBER, new_salary IN NUMBER)
IS
BEGIN
    UPDATE employees
    SET salary = new_salary
    WHERE employee_id = emp_id;
END;
```

This procedure accepts two input parameters: `emp_id` and `new_salary`. It uses these parameters to update the salary of the employee with the specified ID in the `employees` table.

To call this procedure, you would use the following syntax:

```sql
BEGIN
    update_employee_salary(123, 5000);
END;
```

This would call the `update_employee_salary` procedure and pass it the values `123` and `5000` as input parameters. The procedure would then use these values to update the salary of the employee with ID `123` in the `employees` table.

In summary, procedures are a powerful tool in SQL/PL SQL that allow you to perform a wide range of actions and encapsulate complex logic in a reusable and modular way. They are an essential part of any well-designed PL/SQL application.