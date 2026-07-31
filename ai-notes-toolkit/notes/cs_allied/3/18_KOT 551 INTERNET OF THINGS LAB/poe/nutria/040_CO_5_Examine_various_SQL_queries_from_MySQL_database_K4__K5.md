
# CO 5 Examine various SQL queries from MySQL database K4, K5
1. A basic SELECT query can be used to retrieve all the records from a table. This query takes the form of `SELECT * FROM table_name`.
2. The WHERE clause is used to filter the results of a query. It can be used to select specific records based on certain criteria. For example, `SELECT * FROM table_name WHERE field_name = 'value'` will only return records where the field_name is equal to 'value'.
3. The ORDER BY clause is used to sort the results of a query. The syntax for this clause is `ORDER BY field_name ASC|DESC`.
4. The LIMIT clause is used to limit the number of records returned by a query. The syntax for this clause is `LIMIT number_of_records`.
5. The INSERT statement is used to add records to a table. The syntax for this statement is `INSERT INTO table_name (field_name1, field_name2, ...) VALUES (value1, value2, ...)`.
6. The UPDATE statement is used to modify existing records in a table. The syntax for this statement is `UPDATE table_name SET field_name1 = value1, field_name2 = value2, ... WHERE field_name = 'value'`.
7. The DELETE statement is used to remove records from a table. The syntax for this statement is `DELETE FROM table_name WHERE field_name = 'value'`.
8. The LIKE operator is used to search for records that match a certain pattern. The syntax for this operator is `SELECT * FROM table_name WHERE field_name LIKE 'pattern'`.
9. The IN operator is used to search for records that match a certain set of values. The syntax for this operator is `SELECT * FROM table_name WHERE field_name IN (value1, value2, ...)`.
10. The BETWEEN operator is used to search for records within a certain range. The syntax for this operator is `SELECT * FROM table_name WHERE field_name BETWEEN value1 AND value2`.