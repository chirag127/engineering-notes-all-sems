### Procedures in SQL/PL SQL for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

Procedures are a set of SQL statements that perform a specific task. They are used to encapsulate a set of operations or functionality that can be reused and executed multiple times. SQL/PL SQL provides the ability to create procedures that can be stored in the database and executed whenever required. Here are the procedures in SQL/PL SQL that you should know for the Unit 2 - Relational data Model and Language in the subject of Database Management System:

1. Creating a procedure:
   - To create a procedure in SQL/PL SQL, use the CREATE PROCEDURE statement.
   - The basic syntax for creating a procedure is as follows:
     ```
     CREATE PROCEDURE procedure_name
     AS
     BEGIN
        -- SQL statements
     END;
     ```
   - The procedure_name is the name of the procedure, and the SQL statements are the set of operations that the procedure will execute.

2. Executing a procedure:
   - To execute a procedure in SQL/PL SQL, use the EXECUTE or CALL statement.
   - The basic syntax for calling a procedure is as follows:
     ```
     EXECUTE procedure_name;
     ```
   - The procedure_name is the name of the procedure that you want to execute.

3. Passing parameters to a procedure:
   - Procedures can accept parameters in SQL/PL SQL.
   - The basic syntax for passing parameters to a procedure is as follows:
     ```
     CREATE PROCEDURE procedure_name(parameter1 datatype, parameter2 datatype)
     AS
     BEGIN
        -- SQL statements that use the parameters
     END;
     ```
   - The parameters are defined in the parentheses after the procedure name and their data types are specified.

4. Using cursors in a procedure:
   - Cursors are used to retrieve and process data row by row in SQL/PL SQL.
   - The basic syntax for using a cursor in a procedure is as follows:
     ```
     CREATE PROCEDURE procedure_name
     AS
     BEGIN
        DECLARE cursor_name CURSOR FOR select_statement;
        -- SQL statements that use the cursor
     END;
     ```
   - The cursor_name is the name of the cursor, and the select_statement is the SELECT statement used to retrieve data.

5. Handling exceptions in a procedure:
   - Exceptions are runtime errors that can occur in SQL/PL SQL procedures.
   - The basic syntax for handling exceptions in a procedure is as follows:
     ```
     CREATE PROCEDURE procedure_name
     AS
     BEGIN
        -- SQL statements
        EXCEPTION
           WHEN exception_name THEN
              -- SQL statements to handle the exception
     END;
     ```
   - The exception_name is the name of the exception that you want to handle, and the SQL statements are the statements that will execute when the exception occurs.

By understanding and mastering these procedures in SQL/PL SQL, you can efficiently manage and manipulate data in the relational data model and language.