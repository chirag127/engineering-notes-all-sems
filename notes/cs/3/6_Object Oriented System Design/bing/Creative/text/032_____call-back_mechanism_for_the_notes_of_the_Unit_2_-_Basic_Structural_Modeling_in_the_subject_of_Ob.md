### Call-back mechanism

- A call-back mechanism is a way of implementing event-driven programming in object-oriented languages .
- A call-back mechanism allows an application to handle subscribed events, arising at runtime, through a listener interface.
- A listener interface is an abstract class or an interface that defines one or more methods that will be invoked when an event occurs .
- The subscribers, or the objects that are interested in the events, will need to provide a concrete implementation of the listener interface methods .
- The subscribers will then register themselves with the event source, or the object that generates the events, using a call-back register mechanism.
- The event source will keep a list of function objects, or references to the listener methods, and call them back when an event happens .
- A call-back mechanism enables a loose coupling between the event source and the event listeners, as they only need to agree on the listener interface .
- A call-back mechanism also enables a dynamic and flexible behavior of the application, as the event source can notify different listeners depending on the context and the event type .