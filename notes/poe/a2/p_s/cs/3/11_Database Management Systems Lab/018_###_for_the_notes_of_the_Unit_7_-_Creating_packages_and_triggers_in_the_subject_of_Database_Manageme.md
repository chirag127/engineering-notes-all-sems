 Here are the notes for Unit 7 - Creating packages and triggers in Database Management Systems Lab:

### Packages

- Packages are database objects that group related procedures, functions, variables, and other package constructs.
- They allow logically related code to be bundled together and treated as a unit.
- Packages can be created in two parts: package specification and package body.
- Package specification contains interfaces to the package, including procedure and function declarations.
- Package body contains the implementation details, actual procedures and functions.
- Advantages: Modularization,information hiding,easy maintenance.
- Examples: Payroll processing package,order processing package, etc.

### Triggers

- Triggers are database objects that are triggered by events such as insert, update or delete of a table row.
- They are used to automate some actions which need to be performed when a particular event occurs.
- There are two types of triggers:
-- Row level triggers: Triggered for each row affected. Example: Maintain an audit table to track changes.
-- Statement level triggers: Triggered once for the triggering statement. Example: Enforce business rules or restrictions.
- Triggers can be created on tables or views and can be inserted, updated or deleted triggers.
- Advantages: Maintain integrity,auditing,security.
- Examples: Insert an entry in audit table when a record is inserted/updated/deleted from an employee table.

[Further details and diagrams can be included here as required.]