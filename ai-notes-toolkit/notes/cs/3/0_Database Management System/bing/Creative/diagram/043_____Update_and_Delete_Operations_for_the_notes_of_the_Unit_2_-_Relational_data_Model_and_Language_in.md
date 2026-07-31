Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Database Management System. Here is the content for the topic of Update and Delete Operations for the notes of the Unit 2 - Relational data Model and Language.

### Update and Delete Operations

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes for one or more tuples in a relation.
- Delete operations can remove one or more tuples from a relation.
- Both update and delete operations can be specified using a condition that determines which tuples are affected by the operation.
- The condition can be based on the values of the attributes, the results of arithmetic or logical expressions, or the results of subqueries.
- Update and delete operations can be performed using SQL commands or using a graphical user interface (GUI) provided by the database management system (DBMS).

#### SQL Commands for Update and Delete Operations

- The SQL command for updating data in a relation is UPDATE. The general syntax is:

```sql
UPDATE relation_name
SET attribute_name = expression, ...
WHERE condition;
```

- The UPDATE command modifies the values of the specified attributes for the tuples that satisfy the condition.
- The expression can be a constant, a variable, a function, or a subquery.
- If the condition is omitted, all the tuples in the relation are updated.
- For example, the following command updates the salary of the employee with ID 101 to 5000 in the EMPLOYEE relation:

```sql
UPDATE EMPLOYEE
SET salary = 5000
WHERE emp_id = 101;
```

- The SQL command for deleting data from a relation is DELETE. The general syntax is:

```sql
DELETE FROM relation_name
WHERE condition;
```

- The DELETE command removes the tuples that satisfy the condition from the relation.
- If the condition is omitted, all the tuples in the relation are deleted.
- For example, the following command deletes the employee with ID 102 from the EMPLOYEE relation:

```sql
DELETE FROM EMPLOYEE
WHERE emp_id = 102;
```

#### GUI for Update and Delete Operations

- Some DBMSs provide a GUI that allows users to perform update and delete operations on a relation by using a mouse and a keyboard.
- The GUI typically displays the relation as a table, where each row represents a tuple and each column represents an attribute.
- The user can select one or more rows or cells and edit or delete them using the GUI tools.
- The GUI may also provide options to filter, sort, or search the data in the relation.
- The GUI may also generate the corresponding SQL commands for the update and delete operations and execute them on the database.
- For example, the following figure shows a GUI for updating and deleting data in the EMPLOYEE relation:

![GUI for update and delete operations](https://i.imgur.com/9X9y8Za.png)

- The user can select the salary cell of the employee with ID 101 and change its value to 5000 using the keyboard.
- The user can also select the row of the employee with ID 102 and click on the delete button to remove it from the relation.
- The GUI may generate the following SQL commands for these operations and execute them on the database:

```sql
UPDATE EMPLOYEE
SET salary = 5000
WHERE emp_id = 101;

DELETE FROM EMPLOYEE
WHERE emp_id = 102;
```