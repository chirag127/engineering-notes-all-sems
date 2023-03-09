 Here is the content in markdown format for the topic ### stored procedures for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System:

### Stored Procedures

- Stored procedures are precompiled database objects that contain SQL and PL/SQL statements to perform a specific task.
- They are stored in the database and can be invoked using SQL statements.
- The key benefits of stored procedures are:
- Increased performance - as the executable code is precompiled and stored in the database, the database can execute it faster as compared to sending the SQL statements from the application to the database each time.
- Reduced network traffic - only the call to the stored procedure needs to be sent to the database, rather than the whole SQL statement.
- Enforced consistency - a single stored procedure can be modified to reflect any change in business logic, which will ensure consistency and correctness.
- Reusability - stored procedures can be reused by multiple applications, thereby reducing effort and maintenance.
- Security - access to data and resources can be more tightly controlled with stored procedures.

**Structure of a stored procedure:**

- CREATE [OR REPLACE] PROCEDURE procedure_name
- (parameter_name [IN | OUT | IN OUT] parameter_data_type, ...)
- IS | AS
- declaration_section
- BEGIN
- executable_section
- [EXCEPTION
- exception_section]
- END [procedure_name];

**Advantages:**
- Increased performance
- Reduced network traffic
- Reusability
- Enforced consistency
- Security

**Disadvantages:**
- Complexity
- Version control
- Debugging difficulties

**Examples:**

- A simple procedure to print "Hello World":

CREATE OR REPLACE PROCEDURE hello_world
IS
BEGIN
    DBMS_OUTPUT.PUT_LINE('Hello World!');
END;

- A procedure to calculate factorial of a number:

CREATE OR REPLACE PROCEDURE factorial(n IN NUMBER)
IS
    fact NUMBER;
BEGIN
    fact := 1;
    FOR i IN 1..n LOOP
        fact := fact * i;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE(n || ' factorial is ' || fact);
END;

**Applications:**
- DBMS tasks like data validation, triggers, etc.
- Complex business logic
- Reusable modules

[Include diagrams/codes/tables if required.]