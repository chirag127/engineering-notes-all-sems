### Depicting asynchronous messages with/without priority for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- An asynchronous message is a message that is sent without causing the sender to wait for a reply . The recipient must be an active class, with the asynchronous message being a hardware or software interrupt. Most of the web-based interactions are asynchronous messages from the browser to the server followed by another asynchronous message going the other way.
- An asynchronous message is the only message type for which you can individually move the sending and receiving points. You can create an asynchronous message with or without a behavior execution specification. A behavior execution specification is a notation that shows the duration of an action or activity in a lifeline.
- In UML, an asynchronous message has an open arrow head . A synchronous message, which is a message that causes the sender to wait for a reply, has a filled arrow head. A lost message, which is a message that is sent to an element outside the scope of the UML diagram, has a cross at the end of the arrow.
- To depict an asynchronous message with priority, you can use a number or a symbol before the message name to indicate the order of execution. For example, `1: messageA` means that messageA has the highest priority and should be executed first. `2: messageB` means that messageB has the second highest priority and should be executed after messageA. Alternatively, you can use a star (*) before the message name to indicate that it has a higher priority than the other messages without a star. For example, `*: messageC` means that messageC has a higher priority than the other messages in the same lifeline.
- To depict an asynchronous message without priority, you can simply omit the number or the symbol before the message name. For example, `messageD` means that messageD has no priority and can be executed at any time. However, it is possible that message delays cause messages to be received in a different order. Therefore, it is important to consider the timing and sequencing of asynchronous messages when designing a system.
- Here is an example of a UML sequence diagram that shows asynchronous messages with and without priority:

```sequence
participant Browser
participant Server
participant Database
Browser->>Server: 1: requestPage
Server->>Database: 2: queryData
Database->>Server: 3: returnData
Server->>Browser: 4: sendPage
Browser->>Server: *: requestImage
Server->>Browser: *: sendImage
Browser-xServer: lostMessage
```