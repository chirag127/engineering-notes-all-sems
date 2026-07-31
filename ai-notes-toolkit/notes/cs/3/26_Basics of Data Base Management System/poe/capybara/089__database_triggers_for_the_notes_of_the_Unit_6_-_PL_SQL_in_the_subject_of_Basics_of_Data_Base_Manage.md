### Database Triggers for the Notes of the Unit 6 - PL/SQL in the Subject of Basics of Database Management System

Database triggers are an essential feature of PL/SQL that allows you to execute a set of actions automatically when a specific event occurs in the database. It is a piece of code that is executed in response to a specific event, such as a change in a table or view, or an attempt to log in to the database. Here are some important points to keep in mind when working with database triggers:

- **Creating Triggers:** To create a trigger, you must first define the event that will activate it. This is done using a combination of a DDL (Data Definition Language) statement and a PL/SQL block that defines the actions to be taken when the trigger is activated. 

- **Types of Triggers:** There are three types of triggers: DML Triggers, DDL Triggers, and System Triggers. DML triggers are activated by DML (Data Manipulation Language) events such as INSERT, UPDATE, and DELETE statements. DDL triggers are activated by DDL (Data Definition Language) events such as CREATE, ALTER, and DROP statements. System triggers are activated by system events such as database startup and shutdown.

- **Trigger Code:** The code inside the trigger block can include any valid PL/SQL code. You can use variables, loops, and conditional statements to perform complex actions based on the event that triggered the code.

- **Trigger Execution Order:** If multiple triggers are defined for the same event, they are executed in the order they were created. You can also control the order of execution by specifying a firing order for the triggers.

- **Disabling Triggers:** You can disable a trigger using the ALTER TRIGGER statement. This is useful if you need to temporarily suspend the trigger's actions or modify its code.

- **Error Handling:** Triggers can raise exceptions if an error occurs during their execution. You can handle these exceptions using the EXCEPTION block inside the trigger code.

Database triggers are a powerful tool that can help you automate tasks and enforce data integrity in your database. By understanding how they work and how to create them, you can take full advantage of their capabilities and improve the efficiency and reliability of your database.