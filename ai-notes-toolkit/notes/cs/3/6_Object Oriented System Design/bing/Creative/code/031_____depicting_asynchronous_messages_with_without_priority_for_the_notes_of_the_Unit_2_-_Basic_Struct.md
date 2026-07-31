# Depicting asynchronous messages with/without priority for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- An asynchronous message is a message that is sent without causing the sender to wait for a reply .
- The recipient of an asynchronous message must be an active class, with the asynchronous message being a hardware or software interrupt.
- An asynchronous message can have a behavior execution specification, which is a visual representation of the execution of the message on the receiver's lifeline.
- An asynchronous message can also be a lost message, which is a message that is sent to an element outside the scope of the UML diagram.
- In UML, an asynchronous message has an open arrow head  .
- A synchronous message, on the other hand, has a filled arrow head and causes the sender to wait for a reply before continuing execution .
- To depict asynchronous messages with priority, one can use a number or a symbol in front of the message name to indicate the order of execution.
- For example, `1: messageA` means that messageA has the highest priority and should be executed first, while `2: messageB` means that messageB has the second highest priority and should be executed after messageA.
- Alternatively, one can use a dashed line to connect the sending and receiving points of an asynchronous message, and use a solid line for a synchronous message.
- For example, `->> messageA` means that messageA is an asynchronous message, while `-> messageB` means that messageB is a synchronous message.
- Here is an example of a UML sequence diagram that depicts asynchronous messages with and without priority:

```
@startuml
participant A
participant B
participant C
A ->> B : 1: messageA
A ->> C : 2: messageB
B -> C : messageC
@enduml
```

![UML sequence diagram example](https://www.planttext.com/api/plantuml/img/SoWkIImgAStDuKhEIImkLd1EBLBGjLDmpCbCJbMmKiX8pSd9vL0GcfS2j0XABYqioIX9B4b5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9BqfEp4j5wSaZDImkLWZ9