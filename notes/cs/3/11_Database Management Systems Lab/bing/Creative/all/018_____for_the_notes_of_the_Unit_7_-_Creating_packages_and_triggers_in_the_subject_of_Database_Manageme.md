# Unit 7 - Creating packages and triggers in the subject of Database Management Systems Lab

## Packages
- Packages are PL/SQL constructs that enable the grouping of related PL/SQL objects, such as procedures, variables, cursors, functions, constants, and type declarations.
- A package can have two parts: a specification and a body.
- The specification declares the public objects that can be accessed by other PL/SQL programs.
- The body defines the implementation of the objects declared in the specification, as well as private objects that are not visible outside the package.
- Packages can improve the performance, modularity, reusability, and maintainability of PL/SQL code.
- To create a package, you use the following statement:

```sql
CREATE [OR REPLACE] PACKAGE package_name AS
-- package specification
END package_name;
```

- To create a package body, you use the following statement:

```sql
CREATE [OR REPLACE] PACKAGE BODY package_name AS
-- package body
END package_name;
```

## Triggers
- Triggers are stored procedures that are executed automatically when a specified event occurs on a table or view.
- Triggers can be used to enforce business rules, maintain data integrity, audit data changes, or perform other actions based on the event.
- Triggers can be classified into two types: row-level triggers and statement-level triggers.
- Row-level triggers are executed for each row affected by the event, while statement-level triggers are executed once for the whole event.
- Triggers can also be classified into three types based on the timing of the event: before triggers, after triggers, and instead of triggers.
- Before triggers are executed before the event takes place, after triggers are executed after the event takes place, and instead of triggers are executed in place of the event.
- To create a trigger, you use the following statement :

```sql
CREATE [OR REPLACE] TRIGGER trigger_name
[ BEFORE | AFTER | INSTEAD OF] event
ON table_name
[ FOR EACH ROW ]
[ trigger_body ]
```

- The event can be one or more of the following: INSERT, UPDATE, DELETE, or a combination of them using OR.
- The FOR EACH ROW clause specifies whether the trigger is a row-level trigger or a statement-level trigger.
- The trigger_body contains the PL/SQL code to be executed when the trigger fires.