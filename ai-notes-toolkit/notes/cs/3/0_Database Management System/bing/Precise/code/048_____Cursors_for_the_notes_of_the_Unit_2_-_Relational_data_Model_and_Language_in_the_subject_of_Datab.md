### Cursors

Cursors are a control structure that enables traversal over the records in a database. They allow you to retrieve data from a result set one row at a time, rather than the T-SQL commands that operate on all the rows in the result set at one time. Cursors are used when the user needs to update records in a row-by-row manner.

Here are some key points to remember about cursors:

1. Cursors are used to retrieve data from a result set one row at a time.
2. Cursors are used when the user needs to update records in a row-by-row manner.
3. Cursors are less efficient than using T-SQL commands that operate on all the rows in the result set at one time.
4. Cursors can be either forward-only or scrollable. Forward-only cursors only allow you to move forward through the result set, while scrollable cursors allow you to move both forward and backward.
5. Cursors can be either static or dynamic. Static cursors do not reflect changes made to the data while the cursor is open, while dynamic cursors do reflect changes.
6. Cursors can be either read-only or updatable. Read-only cursors do not allow you to make changes to the data, while updatable cursors do allow changes.
7. Cursors can be either local or global. Local cursors are only visible within the batch, stored procedure, or trigger in which they are declared, while global cursors are visible to all sessions.
