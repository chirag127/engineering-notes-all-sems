### Sequence Diagrams for Scenarios in Software Engineering Lab

A sequence diagram is a type of interaction diagram that shows how processes operate with one another and in what order. It is a graphical representation of the interactions between objects in a system. Here are two scenarios for the notes of Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab:

1. **Scenario 1: User Login**
    - The user opens the login page of the application.
    - The user enters their username and password.
    - The application validates the user's credentials.
    - If the credentials are valid, the user is logged in and redirected to the home page.
    - If the credentials are invalid, an error message is displayed.

```
User -> Application: Open Login Page
User -> Application: Enter Username and Password
Application -> Application: Validate Credentials
Application -> User: Login Successful (if valid)
Application -> User: Display Error (if invalid)
```

2. **Scenario 2: User Registration**
    - The user opens the registration page of the application.
    - The user enters their personal information and creates a username and password.
    - The application validates the user's information and checks if the username is available.
    - If the information is valid and the username is available, the user's account is created and they are redirected to the login page.
    - If the information is invalid or the username is unavailable, an error message is displayed.

```
User -> Application: Open Registration Page
User -> Application: Enter Personal Information and Create Username and Password
Application -> Application: Validate Information and Check Username Availability
Application -> User: Account Created (if valid and available)
Application -> User: Display Error (if invalid or unavailable)
```