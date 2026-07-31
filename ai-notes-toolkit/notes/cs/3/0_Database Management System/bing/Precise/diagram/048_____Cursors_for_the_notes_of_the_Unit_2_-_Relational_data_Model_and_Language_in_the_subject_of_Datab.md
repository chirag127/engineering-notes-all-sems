### Cursors

Cursors are a control structure that enables traversal over the records in a database. They allow you to retrieve data from a result set one row at a time, rather than the T-SQL commands that operate on all the rows in the result set at one time.

Here are some key points to remember about cursors:

1. Cursors are used to retrieve data from a result set one row at a time.
2. Cursors are used when the user needs to update records in a result set one at a time.
3. Cursors can be used to perform operations on a row-by-row basis, rather than on the entire result set at once.
4. Cursors are used when the user needs to perform an operation on a specific row in the result set.
5. Cursors can be either forward-only or scrollable. Forward-only cursors only move forward through the result set, while scrollable cursors can move both forward and backward.
6. Cursors can be either read-only or updatable. Read-only cursors only allow the user to retrieve data from the result set, while updatable cursors allow the user to update the data in the result set.
7. Cursors can be either static or dynamic. Static cursors do not reflect changes made to the data in the result set, while dynamic cursors do reflect changes made to the data in the result set.
8. Cursors can be either local or global. Local cursors are only visible within the scope of the current batch, stored procedure, or trigger, while global cursors are visible to all sessions.
