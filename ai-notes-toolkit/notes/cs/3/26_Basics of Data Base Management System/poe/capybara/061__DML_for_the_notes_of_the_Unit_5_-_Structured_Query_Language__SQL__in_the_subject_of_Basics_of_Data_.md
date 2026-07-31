### DML for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

DML stands for Data Manipulation Language. It is used to manipulate the data stored in the database. DML commands are used to retrieve, insert, update and delete records in a database. Here are some important DML commands that you should know:

#### SELECT Command
- SELECT command is used to retrieve data from a table.
- It is the most commonly used command in SQL.
- Syntax: SELECT column_name(s) FROM table_name;

#### INSERT Command
- INSERT command is used to insert new records into a database.
- Syntax: INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);

#### UPDATE Command
- UPDATE command is used to update existing records in a database.
- Syntax: UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;

#### DELETE Command
- DELETE command is used to delete records from a database.
- Syntax: DELETE FROM table_name WHERE condition;

#### TRUNCATE Command
- TRUNCATE command is used to delete all the records from a table.
- It is a faster way to delete all the records from a table as compared to DELETE command.
- Syntax: TRUNCATE TABLE table_name;

#### COMMIT and ROLLBACK Command
- COMMIT command is used to permanently save the changes made to the database.
- ROLLBACK command is used to undo the changes made to the database.
- Syntax: COMMIT; and ROLLBACK;

By learning and understanding these DML commands, you will be able to manipulate the data in the database and perform various operations on it. It is important to practice these commands and understand their syntax to use them effectively in the real-world scenarios.