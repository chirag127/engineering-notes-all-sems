Database testing for web applications is the process of checking the data integrity, consistency, and functionality of the database that is used by the web application. Database testing involves verifying the schema, tables, triggers, stored procedures, and other database components. Database testing also checks the performance, security, and backup/recovery of the database.

The following diagram illustrates the basic architecture of a database testing for web applications using ASCII art:

```
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|   Web Browser    | <----> |   Web Server     | <----> |   Database       |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  User Interface  |        |  Application     |        |  Schema          |
|                  |        |  Logic           |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  Test Cases      |        |  Test Cases      |        |  Test Cases      |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
```

The test cases for each layer of the architecture are:

- Web Browser: Test the user interface of the web application, such as the layout, navigation, functionality, usability, compatibility, and accessibility.
- Web Server: Test the application logic of the web application, such as the business rules, validations, transactions, error handling, and security.
- Database: Test the database of the web application, such as the data integrity, consistency, functionality, performance, security, and backup/recovery.