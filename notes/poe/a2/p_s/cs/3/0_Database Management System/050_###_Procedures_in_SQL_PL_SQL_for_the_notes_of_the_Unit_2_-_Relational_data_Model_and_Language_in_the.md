 Here are the points to cover for the topic ### Procedures in SQL/PL SQL for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System:

1. Procedures: Procedures are named PL/SQL blocks that perform a specific task. A procedure contains a sequence of statements that are executed when the procedure is invoked.
2. Types of Procedures: There are two types of procedures - standalone procedures and packaged procedures.
    - Standalone procedures: Procedures defined outside of any package are known as standalone procedures. They are created using the CREATE PROCEDURE statement.
    - Packaged procedures: Procedures defined within a package are known as packaged procedures. A package is a database object that groups logically related procedures, functions, variables, and other package constructs. Packaged procedures are created using the CREATE PACKAGE statement.
3. Benefits of Procedures:
    - Code reuse: Procedures can be invoked multiple times, thereby reusing the code.
    - Modular programming: Procedures break up complex logic into smaller and more manageable chunks. This improves readability and makes the code easy to maintain.
    - Information hiding: Procedures can hide the implementation details and only expose the necessary interfaces to the callers. This is also known as encapsulation.
    - Better performance: Procedures are parsed once and can be executed multiple times. This can lead to better performance compared to executing the same code multiple times.
4. Examples of Procedures: Here are a few examples of procedures:
    - A procedure to fetch employee details based on the employee number
    - A procedure to update salary of employees belonging to a particular department
    - A procedure to generate monthly reports
5. Advantages and Disadvantages: Some key advantages and disadvantages of procedures are:
    - Advantages: Reusability, modularity, readability, encapsulation, performance
    - Disadvantages: Additional complexity, lack of portability across RDBMS

[You can include detailed examples, diagrams, markdown tables, codes, etc. here to explain the concepts in a more engaging way.]