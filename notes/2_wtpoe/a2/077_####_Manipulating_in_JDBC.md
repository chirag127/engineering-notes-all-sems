 Here is the content in markdown format for the topic #### Manipulating in JDBC:

### Manipulating in JDBC

JDBC provides methods to manipulate data in a database. The main methods for manipulation are:

- INSERT - To insert new rows into a table
- UPDATE - To update existing rows in a table
- DELETE - To delete rows from a table

Here are some key points and learning tricks for these methods:

**INSERT**

- Use `PreparedStatement` object's `setXXX()` methods to bind values to parameters
- Then call `executeUpdate()` method to execute the insert query
- Returns the number of rows inserted
- Good mnemonic: I(nsert) values, then update (execute)

**UPDATE**

- Use `setXXX()` methods to bind new values to parameters
- Then call `executeUpdate()` method to execute the update query
- Returns the number of rows updated
- Good mnemonic: U(pdate) set values, then update

**DELETE**

- Directly call `executeUpdate()` method to execute the delete query
- Returns the number of rows deleted
- No values to bind, simply execute the delete query
- Mnemonic: Just DELETE, nothing to set

Advantages of using prepared statements for manipulation:

- Prevent SQL injection attacks by binding values to parameters
- Often more efficient than creating separate statements each time
- Reusable for multiple executions

Disadvantages:

- Requires care to bind values in correct order to parameters
- Can be confusing for complex queries with many parameters

[Additional details, diagrams, examples, etc. can be added here if required...]