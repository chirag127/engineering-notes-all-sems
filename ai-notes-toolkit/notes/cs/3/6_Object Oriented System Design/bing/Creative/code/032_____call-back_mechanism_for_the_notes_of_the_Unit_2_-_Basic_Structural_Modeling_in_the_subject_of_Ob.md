### Call-back mechanism for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- A call-back mechanism is a way of allowing an application to handle subscribed events, arising at runtime, through a listener interface .
- A listener interface is an abstract class or an interface that defines one or more methods that will be invoked by the event source when the event occurs .
- The event source is an object that can generate events and notify the registered listeners about them .
- The event object is an object that encapsulates the information about the event, such as the source, the type, the time, and any additional data .
- The subscribers are the objects that implement the listener interface and provide a concrete implementation of the methods that will handle the events .
- The call-back mechanism works as follows :
  - The event source registers the listeners that want to be notified about the events.
  - The event source generates an event and creates an event object to store the event information.
  - The event source iterates over the registered listeners and invokes the appropriate method on each listener, passing the event object as an argument.
  - The listener receives the event object and performs the desired action based on the event information.
- The call-back mechanism is useful for implementing the observer pattern, which is a behavioral design pattern that defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically .
- The call-back mechanism is also useful for implementing the strategy pattern, which is a behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it .
- The call-back mechanism can be implemented in different ways depending on the programming language and the features it supports, such as function pointers, closures, delegates, lambda expressions, etc .