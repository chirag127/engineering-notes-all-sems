### Update and Delete Operations in SQL

SQL is a language that allows you to manipulate data in relational databases. SQL has several commands that let you perform different operations on data, such as inserting, updating, deleting, and selecting records. In this section, we will focus on the update and delete operations in SQL.

#### Update Operation

The update operation is used to modify the existing records in the database. You can use the UPDATE command to change the values of one or more columns in a table or a view. The syntax of the UPDATE command is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

The table_name is the name of the table or view that you want to update. The SET clause specifies the columns and the new values that you want to assign to them. You can update multiple columns by separating them with commas. The WHERE clause is optional, but it is recommended to use it to limit the records that are affected by the update. The condition is a logical expression that determines which records match the criteria for the update. If you omit the WHERE clause, all the records in the table or view will be updated, which may not be what you want.

For example, suppose you have a table called students that stores the information of students in a school. The table has the following columns: id, name, grade, and score. You can use the UPDATE command to change the grade and score of a student with id 1:

```sql
UPDATE students
SET grade = 'A', score = 95
WHERE id = 1;
```

This command will update the grade and score columns of the record where the id column is equal to 1. The other records in the table will not be affected.

#### Delete Operation

The delete operation is used to remove the records in the database that are no longer required. You can use the DELETE command to delete one or more records from a table or a view. The syntax of the DELETE command is:

```sql
DELETE FROM table_name
WHERE condition;
```

The table_name is the name of the table or view that you want to delete from. The WHERE clause is optional, but it is recommended to use it to specify the records that you want to delete. The condition is a logical expression that determines which records match the criteria for the deletion. If you omit the WHERE clause, all the records in the table or view will be deleted, which may not be what you want.

For example, suppose you have a table called students that stores the information of students in a school. The table has the following columns: id, name, grade, and score. You can use the DELETE command to delete the record of a student with id 2:

```sql
DELETE FROM students
WHERE id = 2;
```

This command will delete the record where the id column is equal to 2. The other records in the table will not be affected.