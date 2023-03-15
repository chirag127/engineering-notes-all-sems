### Syntax and Constructs for the Notes of the Unit 6 - PL/SQL in the Subject of Basics of Data Base Management System

- PL/SQL stands for Procedural Language/Structured Query Language. It is an extension of SQL that adds procedural features to the relational database language.
- PL/SQL allows users to define and execute blocks of code that can manipulate data, handle exceptions, create variables, constants, cursors, procedures, functions, triggers, and packages .
- The basic unit of PL/SQL is a block, which consists of three sections: declaration, execution, and exception. The declaration section is optional and defines the variables, constants, cursors, and user-defined exceptions. The execution section is mandatory and contains the executable statements that perform the logic of the block. The exception section is optional and handles the errors that may occur during the execution of the block.
- The syntax of a PL/SQL block is as follows:

```
DECLARE
  --optional declarations
BEGIN
  --mandatory executable statements
EXCEPTION
  --optional exception handlers
END;
/
```

- PL/SQL supports many data types, such as scalar, composite, reference, and large object (LOB) types. Scalar types include numeric, character, boolean, and date types. Composite types include record and collection types. Reference types include cursor and REF CURSOR types. LOB types include BLOB, CLOB, NCLOB, and BFILE types.
- PL/SQL identifiers are names of constants, variables, exceptions, procedures, cursors, and reserved words. They must start with a letter and can be followed by letters, numerals, dollar signs, underscores, and number signs. They cannot exceed 30 characters in length.
- PL/SQL supports many operators, such as arithmetic, comparison, logical, set, and string operators. They are used to perform calculations, comparisons, and manipulations on data values.
- PL/SQL supports many control structures, such as conditional, iterative, and sequential structures. They are used to control the flow of execution of the block. Conditional structures include IF-THEN-ELSE, CASE, and NULL statements. Iterative structures include LOOP, WHILE-LOOP, FOR-LOOP, and EXIT statements. Sequential structures include GOTO and NULL statements.
- PL/SQL supports many SQL statements, such as SELECT, INSERT, UPDATE, DELETE, MERGE, and CALL statements. They are used to query and modify data in the database. PL/SQL also supports some SQL clauses, such as INTO, VALUES, and RETURNING clauses. They are used to assign query results to variables, specify values for insert or update operations, and return values from DML statements.
- PL/SQL supports many built-in functions, such as character, numeric, date, conversion, and miscellaneous functions. They are used to perform various operations on data values, such as formatting, manipulation, calculation, and conversion.
- PL/SQL supports many built-in packages, such as DBMS_OUTPUT, UTL_FILE, DBMS_SQL, and DBMS_JOB packages. They are used to perform various tasks, such as displaying output, reading and writing files, executing dynamic SQL, and scheduling jobs.