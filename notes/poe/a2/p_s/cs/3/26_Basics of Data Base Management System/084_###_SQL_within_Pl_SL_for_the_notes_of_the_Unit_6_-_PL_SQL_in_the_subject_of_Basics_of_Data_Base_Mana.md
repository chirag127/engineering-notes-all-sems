 Here is the content in markdown format for the given topic:

### SQL within Pl/SL for the notes of the Unit 6 - PL/SQL

PL/SQL is a procedural extension of SQL that allows embedding of SQL statements within PL/SQL blocks. This enables the user to use the computational capabilities of procedural language with the data manipulation and retrieval power of SQL.

Following are the key points about using SQL within PL/SQL:

1. SQL statements can be used within PL/SQL to query and manipulate data from database tables. These SQL statements follow the same syntax and semantics as direct SQL statements.
2. PL/SQL supports all types of SQL statements - DDL, DML, DCL, and TCL. These can be used to create, alter, drop database objects, insert, update, delete data, grant/revoke privileges, commit/rollback transactions, etc.
3. The SQL statements within PL/SQLblocks can return zero, one, or multiple values through cursors or RETURN statements. These returned values can then be used in the PL/SQL logic.
4. The SQL statements within PL/SQL blocks are implicitly committed when the PL/SQL block completes execution. This can be controlled using COMMIT/ROLLBACK statements within the PL/SQL block.
5. PL/SQL offers some advantages over direct SQL statements such as -
    - Encapsulation of business logic
    - Exception handling
    - Improved performance (due to reduced calls between PL/SQL and SQL engine)
    - Modular programming
    - Robustness and reusability

The following is a simple example of a PL/SQL block using an INSERT SQL statement:

DECLARE
    emp_id NUMBER;
BEGIN
    INSERT INTO employees (name, department)
        VALUES ('John Doe', 'Sales');
    emp_id := employees_sequence.NEXTVAL;
END;

The above block inserts a new employee record into the `employees` table and then fetches the generated employee ID using a sequence.