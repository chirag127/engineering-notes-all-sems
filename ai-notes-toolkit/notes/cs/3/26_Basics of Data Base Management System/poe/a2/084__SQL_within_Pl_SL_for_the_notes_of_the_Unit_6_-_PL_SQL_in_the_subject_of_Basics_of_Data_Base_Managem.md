 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### SQL within Pl/SL for the notes of the Unit 6 - PL/SQL

1. SQL statements can be embedded within PL/SQL blocks using executation statements like EXECUTE IMMEDIATE or OPEN FOR, FETCH, CLOSE.
2. The advantages of embedding SQL in PL/SQL are:
- Avoid context switching between SQL and PL/SQL.
- Enhanced performance as the SQL statement need not leave the PL/SQL engine.
- Tight integration between SQL and PL/SQL.
3. The examples of embedding SQL in PL/SQL are:
EXECUTE IMMEDIATE 'CREATE TABLE emp1 AS SELECT * FROM emp WHERE 1=0';
OPEN c1 FOR 'SELECT ename FROM emp';
FETCH c1 INTO ename;
CLOSE c1;
4. However, there are some disadvantages too like:
- The SQL statement cannot be a Data Definition Language (DDL) statement if it is dynamically constructed.
- The SQL statement cannot contain a semicolon ; within it. It can lead to syntax errors.
- There are limitations on the types of SQL statements that can be executed dynamically.

The above points cover the key aspects of embedding SQL within PL/SQL for the given topic. Please let me know if you would like me to elaborate on any of the points or add more points to the content.