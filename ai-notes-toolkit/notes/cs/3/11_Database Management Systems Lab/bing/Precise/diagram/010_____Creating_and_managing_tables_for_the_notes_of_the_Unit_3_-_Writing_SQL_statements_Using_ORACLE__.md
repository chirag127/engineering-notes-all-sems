### Creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

1. **Creating Tables**: To create a table in ORACLE/MYSQL, the `CREATE TABLE` statement is used. The basic syntax is `CREATE TABLE table_name (column1 datatype, column2 datatype, column3 datatype, ...);`. The column parameters specify the names of the columns of the table and the datatypes define the type of data that can be stored in the column.

2. **Inserting Data**: To insert data into a table, the `INSERT INTO` statement is used. The basic syntax is `INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);`. The column names are optional, but if used, the values must be listed in the same order as the columns.

3. **Updating Data**: To update existing data in a table, the `UPDATE` statement is used. The basic syntax is `UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;`. The `WHERE` clause specifies which records should be updated. If the `WHERE` clause is not used, all records in the table will be updated.

4. **Deleting Data**: To delete data from a table, the `DELETE` statement is used. The basic syntax is `DELETE FROM table_name WHERE condition;`. The `WHERE` clause specifies which records should be deleted. If the `WHERE` clause is not used, all records in the table will be deleted.

5. **Altering Tables**: To add, modify or delete columns in an existing table, the `ALTER TABLE` statement is used. The basic syntax to add a column is `ALTER TABLE table_name ADD column_name datatype;`. To modify a column, the syntax is `ALTER TABLE table_name MODIFY COLUMN column_name datatype;`. To delete a column, the syntax is `ALTER TABLE table_name DROP COLUMN column_name;`.

6. **Dropping Tables**: To delete a table and all its data, the `DROP TABLE` statement is used. The basic syntax is `DROP TABLE table_name;`. This command will permanently delete the table and all its data.

These are the basic commands for creating and managing tables in ORACLE/MYSQL for the subject of Database Management Systems Lab. It is important to practice these commands to become proficient in writing SQL statements.