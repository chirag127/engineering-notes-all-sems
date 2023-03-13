 Here is the content in markdown format for the topic #### Manipulating in JDBC:

## Manipulating in JDBC

JDBC provides methods to manipulate data in a database. The main ways of manipulation are:

1. Insertion - To insert new rows into a table, we use the `insert` query and the `executeUpdate()` method. For example, to insert into an `employee` table, we can write:

```java
String insertQuery = "insert into employee values(101, 'John', 'Sales', 5000)";
int rowsInserted = stmt.executeUpdate(insertQuery);
```

2. Updation - To update existing rows in a table, we use the `update` query and the `executeUpdate()` method. For example, to increase the salary of all employees by 10%, we can write:

```java
String updateQuery = "update employee set salary = salary * 1.1";
int rowsUpdated = stmt.executeUpdate(updateQuery);
```

3. Deletion - To delete rows from a table, we use the `delete` query and the `executeUpdate()` method. For example, to delete all employees from the `employee` table, we can write:

```java
String deleteQuery = "delete from employee";
int rowsDeleted = stmt.executeUpdate(deleteQuery);
```

Some useful mnemonics to remember the order of manipulation methods in JDBC are:

- IUD - Insert, Update, Delete
- Please Insert Coffee (PIC) - For insertion
- Wait, Update Salary (WUS) - For updation
- Remove Employees (RE) - For deletion

Advantages of JDBC manipulation are:
- Simple API to use
- Supports database agnostic queries
- Secure data access with transactions

Disadvantages are:
- Low-level API, so a lot of boilerplate code needs to be written
- Manual resource management can lead to leaks
- Error handling is verbose

<!-- Additional details, diagrams, examples, etc. can be added here -->