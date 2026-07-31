# Call-back mechanism

- A call-back mechanism is a way of implementing event-driven programming in object-oriented languages.
- A call-back mechanism allows an object to register its interest in a certain event and provide a method to be invoked when that event occurs.
- A call-back mechanism consists of three components: an event source, an event listener, and a call-back method.
- An event source is an object that generates events, such as a button, a timer, or a network connection.
- An event listener is an object that implements an interface that defines one or more call-back methods. The event listener registers itself with the event source using a method such as `addEventListener`.
- A call-back method is a method that is defined by the event listener interface and is invoked by the event source when the corresponding event occurs. The call-back method may receive parameters that provide information about the event, such as its type, source, or data.
- A call-back mechanism enables a loose coupling between the event source and the event listener, as they only need to agree on the interface and not on the implementation details.
- A call-back mechanism also enables a dynamic and flexible behavior, as the event listener can change its response to the event based on the context or the state of the system.
- A call-back mechanism is widely used in graphical user interfaces, network programming, asynchronous operations, and other scenarios that involve interaction or concurrency.