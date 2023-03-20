### Unit 7: Creating Packages and Triggers in Database Management Systems Lab

#### Packages

- A package is a logical grouping of related functions, procedures, and other types of database objects.
- Packages provide modularity, better organization, and reusability of code.
- A package consists of two parts: specification and body.
- The specification contains the public interface of the package, which is visible to the outside world.
- The body contains the implementation details of the package, which are hidden from the outside world.
- The CREATE PACKAGE statement is used to create a package.
- The package can be called using the package name followed by the procedure or function name.

#### Triggers

- A trigger is a special type of stored procedure that is automatically invoked in response to certain events, such as insert, update, or delete operations on a table.
- Triggers can be used to enforce business rules, audit changes, or perform complex data transformations.
- Triggers are defined on a table or view and are associated with one or more of the following events: BEFORE INSERT, AFTER INSERT, BEFORE UPDATE, AFTER UPDATE, BEFORE DELETE, and AFTER DELETE.
- The CREATE TRIGGER statement is used to create a trigger.
- The trigger can be written in PL/SQL or SQL.
- Triggers can be disabled or enabled using the ALTER TRIGGER statement.
- The trigger code can access the old and new values of the affected rows using the :OLD and :NEW keywords, respectively.

#### Differences between Packages and Triggers

| Packages | Triggers |
| --- | --- |
| Logical grouping of related functions and procedures | Special type of stored procedure |
| Provides modularity, organization, and reusability of code | Automatically invoked in response to certain events |
| Consists of specification and body | Defined on a table or view |
| Public interface visible to the outside world | Associated with one or more of the following events: BEFORE INSERT, AFTER INSERT, BEFORE UPDATE, AFTER UPDATE, BEFORE DELETE, and AFTER DELETE |
| Implementation details hidden from the outside world | Can be written in PL/SQL or SQL |

#### Conclusion

In conclusion, packages and triggers are powerful features of the Oracle database that can greatly enhance the modularity, organization, and reusability of code. By using packages, database developers can create libraries of related functions and procedures that can be easily called from other parts of the application. By using triggers, database developers can enforce business rules, audit changes, or perform complex data transformations in a transparent and efficient manner.