Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on depicting asynchronous messages with/without priority for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design.

- An **asynchronous message** is a message that is sent without causing the sender to wait for a reply. The recipient must be an active class, with the asynchronous message being a hardware or software interrupt.
- An asynchronous message can be created with or without a **behavior execution specification**, which is a visual representation of the duration of the behavior invoked by the message.
- An asynchronous message can also have a **priority**, which is a value that indicates the urgency or importance of the message. The priority can be specified as a number, a keyword, or a symbol.
- In UML diagrams, an asynchronous message is shown with an **open arrow head**. A synchronous message, which is a message that causes the sender to wait for a reply, is shown with a **filled arrow head**.
- An asynchronous message can also be a **lost message**, which is a message that is sent to an element outside the scope of the UML diagram. A lost message is shown with a **crossed circle** at the end of the message line.
- An example of a UML diagram with asynchronous messages with/without priority and behavior execution specification is shown below:

```markdown
@startuml
participant A
participant B
participant C
A ->> B : msg1 (high priority)
activate B
B ->> C : msg2 (low priority)
activate C
C ->> A : msg3
deactivate C
A ->> B : msg4
deactivate B
A ->> C : msg5 (lost message)
@enduml
```

![UML diagram with asynchronous messages](https://www.plantuml.com/plantuml/png/SoWkIImgAStDuKhEIImkLd1EBLBGjLDmpCbCJbMmKiX8pSd9vL0gNafCJYqjLW00)