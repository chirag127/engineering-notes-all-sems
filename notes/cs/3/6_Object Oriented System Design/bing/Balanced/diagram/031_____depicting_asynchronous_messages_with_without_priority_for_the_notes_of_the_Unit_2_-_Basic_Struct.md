Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on depicting asynchronous messages with/without priority for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design:

- An asynchronous message is a message that is sent without causing the sender to wait for a reply. The recipient must be an active class, with the asynchronous message being a hardware or software interrupt.
- An asynchronous message is the only message type for which you can individually move the sending and receiving points. You can create an asynchronous message with or without a behavior execution specification.
- In UML, an asynchronous message has an open arrow head. A synchronous message has a filled arrow head.
- You can use a star (*) symbol to indicate the priority of an asynchronous message. The higher the number of stars, the higher the priority. For example, `a ->> b *` means that a sends an asynchronous message to b with a low priority, while `a ->> b ***` means that a sends an asynchronous message to b with a high priority.
- You can also use a lost message symbol (X) to indicate that an asynchronous message is sent to an element outside the scope of the UML diagram.
- Here is an example of a UML sequence diagram that shows asynchronous messages with and without priority:

```markdown
@startuml
participant a
participant b
participant c
a ->> b * : low priority message
a ->> c ** : medium priority message
a ->> X *** : high priority message to unknown element
@enduml
```

![UML sequence diagram](https://www.plantuml.com/plantuml/png/SoWkIImgAStDuKhEIImkLd1EBLBGjLDmpCbCJbMmKiX8pSd9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ9vL0gNafCJYqjIYqkLWZ