### Sequence Diagrams for Unit 1 - Introduction of Software Engineering Lab

A sequence diagram is a type of interaction diagram that shows how objects interact with each other in a particular scenario. In software engineering, sequence diagrams are used to model the interactions between objects in a system. Here are two scenarios for which we can draw sequence diagrams for the notes of Unit 1 - Introduction of Software Engineering Lab.

#### Scenario 1: User login

In this scenario, we will draw a sequence diagram for a user logging into a web application. The following are the steps involved:

1. The user enters their username and password on the login page of the web application.
2. The web application sends a request to the server with the user's credentials.
3. The server verifies the user's credentials and sends a response to the web application.
4. If the user's credentials are correct, the web application redirects the user to their dashboard.
5. The user interacts with the dashboard to perform various tasks.

The following is the sequence diagram for this scenario:

```
User->Web Application: Enter username and password
Web Application->Server: Send request with user's credentials
Server->Web Application: Verify user's credentials
Web Application->User: Redirect to dashboard
User->Web Application: Interact with dashboard
```

#### Scenario 2: Sending an email

In this scenario, we will draw a sequence diagram for sending an email using a web application. The following are the steps involved:

1. The user composes an email and clicks the send button.
2. The web application sends a request to the server with the email details.
3. The server validates the email details and sends a response to the web application.
4. The web application displays a success message to the user.

The following is the sequence diagram for this scenario:

```
User->Web Application: Compose email and click send button
Web Application->Server: Send request with email details
Server->Web Application: Validate email details
Web Application->User: Display success message
```

In conclusion, sequence diagrams are an important tool for modeling the interactions between objects in a system. By drawing sequence diagrams for different scenarios, you can better understand how the system works and identify potential issues.