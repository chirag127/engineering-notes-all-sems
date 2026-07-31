### Sequence Diagrams for Software Engineering Lab

A sequence diagram is a type of interaction diagram that shows how processes operate with one another and in what order. It is a construct of a message sequence chart. Here are two scenarios for the notes of Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab:

#### Scenario 1: User Login

1. The user enters their username and password on the login page.
2. The system validates the user's credentials.
3. If the credentials are valid, the system logs the user in and displays the user's home page.
4. If the credentials are invalid, the system displays an error message.

```
User -> System: Enter username and password
System -> System: Validate credentials
alt credentials are valid
    System -> User: Display home page
else credentials are invalid
    System -> User: Display error message
end
```

#### Scenario 2: User Registration

1. The user enters their personal information on the registration page.
2. The system validates the user's information.
3. If the information is valid, the system creates a new user account and logs the user in.
4. If the information is invalid, the system displays an error message.

```
User -> System: Enter personal information
System -> System: Validate information
alt information is valid
    System -> System: Create new user account
    System -> User: Log user in
else information is invalid
    System -> User: Display error message
end
```