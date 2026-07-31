# Sequence Diagram for Software Engineering Lab

A sequence diagram is a type of interaction diagram that shows the sequence of messages exchanged between objects in a system to perform a specific functionality. It is used to illustrate the interactions between objects in a system and the order in which they occur. Sequence diagrams are useful for software engineering because they help to understand the requirements of a new system or to document an existing process.      

To draw a sequence diagram, you need to identify the following components:

- The objects involved in the interaction and their lifelines
- The messages sent and received by the objects and their types (synchronous, asynchronous, reply, etc.)
- The activation bars that show the periods of activity of the objects
- The time constraints and conditions that govern the interaction
- The loops, alternatives, and fragments that represent the different scenarios of the interaction

Here are two examples of sequence diagrams for the notes of the Unit 1 - Introduction of Software Engineering Lab:

## Example 1: Login Scenario

This sequence diagram shows the interaction between a user, a login form, and a database when the user tries to log in to a system.

![Login Sequence Diagram](https://i.imgur.com/4Z4J4XO.png)

The steps are:

1. The user enters the username and password in the login form and clicks the login button.
2. The login form sends a synchronous message to the database to check the credentials.
3. The database returns a reply message with the result of the validation.
4. If the result is true, the login form sends an asynchronous message to the user to display the welcome page.
5. If the result is false, the login form sends an asynchronous message to the user to display an error message.

## Example 2: Registration Scenario

This sequence diagram shows the interaction between a user, a registration form, a database, and an email service when the user tries to register to a system.

![Registration Sequence Diagram](https://i.imgur.com/4Z4J4XO.png)

The steps are:

1. The user enters the personal information and the email address in the registration form and clicks the register button.
2. The registration form sends a synchronous message to the database to check if the email address is already taken.
3. The database returns a reply message with the result of the check.
4. If the result is false, the registration form sends a synchronous message to the database to create a new account.
5. The database returns a reply message with the confirmation of the creation.
6. The registration form sends an asynchronous message to the email service to send a verification email to the user.
7. The email service sends a reply message to the registration form with the status of the email delivery.
8. The registration form sends an asynchronous message to the user to display a success message and a link to verify the email address.
9. If the result is true, the registration form sends an asynchronous message to the user to display an error message and a suggestion to use a different email address.