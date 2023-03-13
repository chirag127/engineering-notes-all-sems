Prepared Statements in JDBC are a special type of statements that allow you to execute parameterized queries against the database. A parameter is represented by a question mark (?) symbol in JDBC. Prepared Statements are precompiled by the database and can be executed multiple times with different values for the parameters. Prepared Statements extend the Statement interface and provide methods to set the values for the parameters and execute the query.

#### Prepared Statements in JDBC

The following diagram illustrates the basic architecture of a Prepared Statement in JDBC:

```
+-----------------+      +-----------------+      +-----------------+
| Java Application|      | JDBC Driver     |      | Database        |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| 1. Create a     |      |                 |      |                 |
| PreparedStatement|----->|                 |      |                 |
| object with a   |      |                 |      |                 |
| parameterized   |      |                 |      |                 |
| query           |      |                 |      |                 |
|                 |      |                 |      |                 |
| 2. Set the      |      |                 |      |                 |
| values for the  |----->|                 |      |                 |
| parameters using|      |                 |      |                 |
| setter methods  |      |                 |      |                 |
|                 |      |                 |      |                 |
| 3. Execute the  |      |                 |      |                 |
| PreparedStatement|----->| 4. Send the     |----->| 5. Compile and  |
| object using    |      | query and the   |      | execute the     |
| executeQuery()  |      | parameters to   |      | query with the  |
| or executeUpdate()|     | the database    |      | parameters      |
|                 |      |                 |      |                 |
| 6. Process the  |<-----| 7. Return the   |<-----| 6. Return the   |
| ResultSet or    |      | ResultSet or    |      | ResultSet or    |
| update count    |      | update count    |      | update count    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```