 Here is the content in markdown format for the topic ### Triggers for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System:

Triggers are special stored procedures that get executed automatically when a specified event occurs in a database. They are used to enforce complex business rules or for auditing and data integrity.

Types of Triggers:
1. Data Definition Language (DDL) Triggers - Executed in response to DDL commands like CREATE, ALTER, DROP, etc.
2. Data Manipulation Language (DML) Triggers - Executed in response to DML commands like INSERT, UPDATE, DELETE.
3. Logon Triggers - Executed when a user logs on.
4. Database Triggers - Executed when a database is attached or detached.

Uses of Triggers:
1. Enforce Complex Business Rules - Triggers can be used to enforce complex business rules that cannot be enforced using constraints or stored procedures.
2. Auditing - Triggers can be used to log information about who made changes to which data and when the changes were made. This is useful for auditing.
3. Data Integrity - Triggers can be used to ensure data integrity for example:-
- Ensuring that the sum of values in a child table matches a value in the parent table.
- Preserving referential integrity between two tables.
- Cascading changes to related tables.

Advantages:
1. Centralized Business Logic - Triggers allow you to centralize business logic in the database.
2. Automation - Triggers automate response to events reducing manual effort.
3. Flexibility - Triggers provide more flexibility than constraints. Complex business rules can be implemented using triggers.

Disadvantages:
1. Performance Overhead - There is some performance overhead involved in triggering and executing triggers.
2. Debugging Difficulty - It can be difficult to debug and test triggers thoroughly.
3. Risk of Infinite Loops - There is a possibility of creating infinite loops if triggers are not designed properly.