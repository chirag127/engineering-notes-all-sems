 Here is the content written in markdown format for the topic ## Unit 7 - Creating packages and triggers:

## Unit 7 - Creating packages and triggers

1. Packages:
    - Packages are schema objects that groups related database objects like procedures, functions, sequences, synonyms, etc.
    - Using packages helps in easier management, accessing and control of the related database objects.
    - Packages can have two parts:
        - Package specification (spec): Acts as an interface to the package. Declares all the objects that are accessible to users.
        - Package body: Contains the implementation details of all the objects declared in the package spec.
    - Advantages:
        - Modular approach: logically groups related objects
        - Information hiding: hides the implementation details
        - Overloading: supports function overloading
        - Default values: can specify default values for parameters
    - Examples:
        - Create a package to handle employee related operations like calculating salary, annual bonus, etc.

2. Triggers:
    - Triggers are special types of stored procedures that get executed automatically when a specified database event occurs.
    - The events could be data manipulation events like INSERT, UPDATE or DELETE.
    - Triggers help in implementing business rules, auditing data changes, updating other tables, etc.
    - Types:
        - Row level: executed once for each row affected
        - Statement level: executed only once for the triggering statement
        - BEFORE: executed before the event occurs
        - AFTER: executed after the event occurs
    - Examples:
        - Trigger to update an audit table with old and new values when a record is updated in an employee table.
        - Trigger to restrict DELETE operations on a table.

- The points elaborate on the topics in detail with examples and cover the key concepts and terms to learn about creating packages and triggers.
- The content can be helpful as study material to read and learn about these concepts for exams. Please let me know if you would like me to elaborate on any part of the content further.