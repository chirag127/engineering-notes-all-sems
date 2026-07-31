# Sequence Diagram for Software Engineering Lab

A sequence diagram is a type of interaction diagram that shows the sequence of messages exchanged between objects in a system to perform a specific functionality. It is used to illustrate the interactions between objects in a system in the order that they occur. Sequence diagrams are useful for software developers and business professionals to understand the requirements of a new system or to document an existing process.

## Components of Sequence Diagram

A sequence diagram consists of the following components:

- **Objects**: Objects are the entities that participate in the interaction. They are represented by rectangles with the object name and an optional classifier. For example, `user:Customer` or `controller:LoginController`.
- **Lifelines**: Lifelines are vertical dashed lines that indicate the existence of an object over time. They are attached to the objects and extend downwards along the timeline of the diagram.
- **Messages**: Messages are the communication between objects. They are represented by horizontal arrows with the message name and an optional sequence number. For example, `1: login(username, password)` or `2: validate(username, password)`. There are different types of messages, such as synchronous, asynchronous, reply, create, destroy, etc.
- **Activation boxes**: Activation boxes are thin rectangles that show the period of time an object is active or executing a message. They are attached to the lifelines and extend horizontally along the message arrows.
- **Frames**: Frames are optional rectangular boxes that enclose a part of the interaction. They are used to indicate different regions or fragments of the diagram, such as loops, alternatives, options, etc. They have a label in the top left corner that specifies the type of the fragment. For example, `alt` for alternative, `loop` for loop, `opt` for option, etc.

## Examples of Sequence Diagram

Here are two examples of sequence diagrams for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab.

### Example 1: Login Scenario

This sequence diagram shows the interaction between a user and a login controller to perform a login functionality. The user enters the username and password and sends a login message to the login controller. The login controller validates the credentials and sends a reply message to the user with the result. If the login is successful, the user is redirected to the home page. If the login fails, the user is shown an error message.

```sequence
user:Customer->controller:LoginController: 1: login(username, password)
activate controller
controller->controller: 2: validate(username, password)
controller-->user: 3: reply(result)
deactivate controller
alt result == success
user->home:Home: 4: redirect()
else result == failure
user->error:Error: 5: show()
end
```

### Example 2: Registration Scenario

This sequence diagram shows the interaction between a user and a registration controller to perform a registration functionality. The user enters the personal details and sends a register message to the registration controller. The registration controller creates a new account object and sends a reply message to the user with the result. If the registration is successful, the user is redirected to the login page. If the registration fails, the user is shown an error message.

```sequence
user:Customer->controller:RegistrationController: 1: register(details)
activate controller
controller->account:Account: 2: create(details)
activate account
account-->controller: 3: reply(result)
deactivate account
controller-->user: 4: reply(result)
deactivate controller
alt result == success
user->login:Login: 5: redirect()
else result == failure
user->error:Error: 6: show()
end
```