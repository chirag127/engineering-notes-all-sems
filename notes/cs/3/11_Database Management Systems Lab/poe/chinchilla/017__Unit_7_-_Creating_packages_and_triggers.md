## Unit 7 - Creating packages and triggers

In this unit, we will learn about creating packages and triggers in Oracle PL/SQL. Following are the key concepts that we will cover:

### Packages

- A package is a collection of related procedures, functions, variables, and cursors that are stored together as a single program unit in the database.
- Packages provide a way to organize code and make it more modular, reusable, and easier to maintain.
- A package has two parts: the specification and the body. The specification contains the public interface of the package, including the declarations of the procedures, functions, and variables that can be called from outside the package. The body contains the implementation of the package, including the actual code for the procedures and functions.
- To create a package, we use the CREATE PACKAGE statement, followed by the package specification and the package body.

### Triggers

- A trigger is a special type of stored procedure that is automatically executed in response to certain events, such as inserting, updating, or deleting data in a table.
- Triggers can be used to enforce business rules, maintain data integrity, and perform complex calculations or data transformations.
- A trigger has two parts: the trigger event and the trigger action. The trigger event specifies the condition that triggers the execution of the trigger, such as a row being inserted into a table. The trigger action specifies the code that is executed when the trigger is fired.
- To create a trigger, we use the CREATE TRIGGER statement, followed by the trigger name, the trigger event, and the trigger action.

### Creating Packages

To create a package, we follow these steps:

1. Create the package specification using the CREATE PACKAGE statement. The package specification includes the declarations of the procedures, functions, and variables that can be called from outside the package.
2. Create the package body using the CREATE PACKAGE BODY statement. The package body includes the implementation of the procedures and functions declared in the package specification.
3. Test the package by calling its procedures and functions from outside the package.

### Creating Triggers

To create a trigger, we follow these steps:

1. Identify the table and the trigger event that will trigger the execution of the trigger.
2. Write the trigger action, which is the code that will be executed when the trigger is fired.
3. Create the trigger using the CREATE TRIGGER statement, followed by the trigger name, the trigger event, and the trigger action.
4. Test the trigger by inserting, updating, or deleting data in the table and verifying that the trigger is executed as expected.

### Conclusion

In this unit, we learned about creating packages and triggers in Oracle PL/SQL. Packages provide a way to organize code and make it more modular and reusable, while triggers can be used to enforce business rules and maintain data integrity. By following the steps outlined in this unit, we can create packages and triggers that are efficient, maintainable, and reliable.