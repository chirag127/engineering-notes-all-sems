### Unit 5 - Creating Cursor

In this unit, we will be focusing on the concept of cursors in database management systems. Cursors are used to retrieve data from the database one row at a time, which can be useful in situations where you need to perform operations on each row individually.

#### What is a Cursor?

A cursor is a database object that enables the traversal and manipulation of results from a query. It is essentially a pointer to a specific row within a result set. Cursors are commonly used in database applications to allow users to navigate through large amounts of data in a controlled and efficient manner.

#### Types of Cursors

There are two main types of cursors:

1. Forward-only cursor: This type of cursor allows you to move only forward through the result set, one row at a time. Once you have moved past a row, you cannot return to it. This type of cursor is commonly used when you only need to read through the data once.

2. Scrollable cursor: This type of cursor allows you to move both forward and backward through the result set, and allows you to return to rows that you have already visited. This type of cursor is useful when you need to perform operations on the data that require you to revisit certain rows multiple times.

#### Creating a Cursor in SQL

To create a cursor in SQL, you first need to declare it and define the SELECT statement that will be used to retrieve the data. You can then open the cursor and start fetching rows one at a time. Finally, you should close the cursor once you have finished working with the data.

Here is an example of how to create a cursor in SQL:

```
DECLARE @employee_id INT;
DECLARE @employee_name VARCHAR(50);

DECLARE employee_cursor CURSOR FOR
SELECT employee_id, employee_name
FROM employees
WHERE department = 'Sales';

OPEN employee_cursor;

FETCH NEXT FROM employee_cursor INTO @employee_id, @employee_name;

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT 'Employee ID: ' + CAST(@employee_id AS VARCHAR(10)) + ', Employee Name: ' + @employee_name;
    FETCH NEXT FROM employee_cursor INTO @employee_id, @employee_name;
END;

CLOSE employee_cursor;
DEALLOCATE employee_cursor;
```

#### Advantages of Cursors

- Cursors allow you to retrieve data from the database one row at a time, which can be useful when working with large result sets.

- Cursors enable you to perform operations on each row individually, which can be useful when you need to update or delete data.

- Cursors are useful when you need to traverse the data in a non-linear manner.

#### Disadvantages of Cursors

- Cursors can be slow and resource-intensive, especially when working with large result sets.

- Cursors can be difficult to use correctly, and can lead to bugs and errors if not used properly.

- Cursors can be less efficient than other methods of retrieving data from the database, such as using a single SELECT statement.

#### Conclusion

In conclusion, cursors are a useful tool for working with data in database applications. They allow you to retrieve and manipulate data one row at a time, which can be useful in a variety of situations. However, cursors can also be slow and resource-intensive, and should be used with caution.