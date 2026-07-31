## Unit 6 - PL/SQL

PL/SQL stands for Procedural Language/Structured Query Language. It is a block-structured language used to write programs that can be executed on an Oracle database. PL/SQL is a powerful language that enables developers to create complex database applications with ease. Here are some key points to keep in mind when studying PL/SQL:

### 1. PL/SQL Block Structure

- A PL/SQL program consists of blocks of code that are executed sequentially.
- Each block begins with the keyword `DECLARE` and ends with the keyword `END`.
- The code within a block can include declarations, assignments, control structures (e.g. IF-THEN-ELSE), loops (e.g. FOR, WHILE), and SQL statements.
- Blocks can be nested within other blocks.

### 2. PL/SQL Variables and Constants

- PL/SQL supports several types of variables, including scalar variables (e.g. integers, strings), collections (e.g. arrays), and user-defined types.
- Variables can be declared within a block using the `DECLARE` keyword.
- Constants can also be defined using the `CONSTANT` keyword.

### 3. PL/SQL Control Structures

- PL/SQL provides several control structures for making decisions and looping through code.
- `IF-THEN-ELSE` statements can be used to execute different code depending on a condition.
- `CASE` statements can be used to execute different code depending on the value of a variable.
- Loops such as `FOR` and `WHILE` can be used to repeat code a certain number of times or until a condition is met.

### 4. PL/SQL Cursors

- Cursors are used to process a set of rows returned from a database query.
- PL/SQL provides both implicit and explicit cursors.
- Implicit cursors are automatically created for SELECT statements that return a single row.
- Explicit cursors must be declared and opened before they can be used to process a result set.

### 5. PL/SQL Exceptions

- Exceptions are used to handle errors that occur during program execution.
- PL/SQL provides a number of built-in exceptions, such as `NO_DATA_FOUND` and `TOO_MANY_ROWS`.
- Developers can also define their own exceptions using the `EXCEPTION` keyword.

### 6. PL/SQL Stored Procedures and Functions

- Stored procedures and functions are reusable blocks of code that can be called from other PL/SQL programs.
- Stored procedures do not return a value, while functions do.
- Both stored procedures and functions can have parameters that are passed in when they are called.

By mastering PL/SQL, developers can create powerful database applications that can manipulate and process data with ease. It is an essential skill for anyone working with Oracle databases.