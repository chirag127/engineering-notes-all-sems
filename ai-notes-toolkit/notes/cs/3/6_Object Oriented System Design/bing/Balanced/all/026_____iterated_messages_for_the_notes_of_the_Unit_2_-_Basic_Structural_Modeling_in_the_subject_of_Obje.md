# Iterated Messages

- Iterated messages are a way of representing repeated messages in interaction diagrams, such as sequence diagrams or collaboration diagrams.
- Iterated messages are useful for modeling loops, iterations, or collections of objects that receive the same message.
- Iterated messages are denoted by an asterisk (*) followed by a guard condition in square brackets, such as *[i < 10]* or *[for each item in list]*.
- Iterated messages can have a return value, which is usually a collection of the return values from each iteration.
- Iterated messages can be nested, meaning that one iterated message can contain another iterated message inside its guard condition or body.
- Iterated messages can also be combined with other types of messages, such as synchronous, asynchronous, or create messages.

## Example

- The following sequence diagram shows an example of an iterated message.
- The diagram models a scenario where a user requests a list of books from a library system, and the system returns the books that match the user's criteria.
- The iterated message *[for each book in books]* represents the repeated message that the system sends to each book object to check if it matches the criteria.
- The return value of the iterated message is a collection of books that match the criteria, which is then returned to the user.

![Sequence diagram with iterated message](https://www.guru99.com/images/1/022518_0619_Interaction1.png)