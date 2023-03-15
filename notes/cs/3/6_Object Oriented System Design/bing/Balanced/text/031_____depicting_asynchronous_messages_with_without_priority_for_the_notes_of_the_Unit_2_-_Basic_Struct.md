### Depicting asynchronous messages with/without priority for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- An asynchronous message is a message that is sent without causing the sender to wait for a reply . The recipient must be an active class, with the asynchronous message being a hardware or software interrupt. Most of the web-based interactions are asynchronous messages from the browser to the server followed by another asynchronous message going the other way.
- An asynchronous message is the only message type for which you can individually move the sending and receiving points. You can create an asynchronous message with or without a behavior execution specification. A behavior execution specification is a notation that shows the duration of an action or a state in a lifeline.
- In UML, an asynchronous message has an open arrow head . A synchronous message, which is a message that causes the sender to wait for a reply, has a filled arrow head. An example of a synchronous message is a method call in an object-oriented language.
- To depict an asynchronous message with priority, you can use a number or a symbol in front of the message name to indicate the order of execution. For example, 1:sendEmail() means that this message has the highest priority and should be executed first. Alternatively, you can use a star (*) to indicate that the message has a lower priority than the others. For example, *:updateStatus() means that this message can be executed later or skipped if necessary.
- To depict an asynchronous message without priority, you can simply omit the number or the symbol in front of the message name. For example, notifyUser() means that this message has no specific priority and can be executed at any time.
- Here is an example of a UML sequence diagram that shows asynchronous messages with and without priority:

```markdown
@startuml
participant Browser
participant Server
Browser ->> Server : 1:login()
activate Server
Server ->> Browser : 2:showHomePage()
activate Browser
Browser ->> Server : *:sendFeedback()
deactivate Browser
Server ->> Browser : 3:acknowledgeFeedback()
activate Browser
deactivate Browser
deactivate Server
@enduml
```

![UML sequence diagram example](https://www.plantuml.com/plantuml/png/SoWkIImgAStDuKhEIImkLd1EBLBGjLDmpCbCJbMmKiX8pSd9vL0gNafCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJYqgB4fCJ