# Unit 7 - Creating packages and triggers in the subject of Database Management Systems Lab

## Packages
- Packages are PL/SQL constructs that enable the grouping of related PL/SQL objects, such as procedures, variables, cursors, functions, constants, and type declarations.
- A package can have two parts: a specification and a body. The specification defines the interface of the package, which includes the declarations of the objects that can be referenced from outside the package. The body implements the logic of the package, which includes the definitions of the objects declared in the specification.
- Packages can provide modularity, encapsulation, reusability, and performance benefits for PL/SQL applications.
- To create a package, you use the following statement:

```sql
CREATE [OR REPLACE] PACKAGE package_name AS
-- package specification
END package_name;
/
CREATE [OR REPLACE] PACKAGE BODY package_name AS
-- package body
END package_name;
/
```

## Triggers
- Triggers are stored procedures that are executed automatically when a specified event occurs on a table or view.
- Triggers can be used to enforce business rules, audit data changes, replicate data, or perform other actions based on the event.
- Triggers can be classified by the timing of their execution (before or after the event), the type of event that activates them (insert, update, or delete), and the scope of their effect (for each row or for each statement) .
- To create a trigger, you use the following statement:

```sql
CREATE TRIGGER trigger_name [ BEFORE | AFTER] event ON table_name
trigger_type
BEGIN
-- trigger_logic
END;
```

: https://www.sqltutorial.org/sql-triggers/
: https://afteracademy.com/blog/what-is-a-trigger-in-dbms/
: https://docs.oracle.com/cd/A97630_01/win.920/a97251/ch3.htm