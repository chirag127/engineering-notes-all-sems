### Call-back mechanism for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- A call-back mechanism is a way of allowing an application to handle events that occur at runtime by using a listener interface .
- A listener interface is an abstract class or an interface that defines one or more methods that the application needs to implement to respond to the events .
- The application that wants to handle the events is called the subscriber or the client, and the application that generates the events is called the publisher or the server .
- The subscriber registers its interest in the events by providing a concrete implementation of the listener interface to the publisher .
- The publisher keeps a reference to the listener object and invokes its methods when the events occur .
- This way, the subscriber and the publisher are loosely coupled, meaning that they do not depend on each other's implementation details .
- A call-back mechanism is useful for implementing event-driven programming, where the application logic is determined by the occurrence of events rather than by a predefined sequence of steps .
- A call-back mechanism can also be used to implement inversion of control, where the control flow of the application is inverted from the usual caller-callee relationship to a callee-caller relationship .
- A call-back mechanism can be implemented in different ways depending on the programming language and the design pattern used   .
- Some examples of call-back mechanisms are function pointers, closures, delegates, events, observers, strategies, and commands   .