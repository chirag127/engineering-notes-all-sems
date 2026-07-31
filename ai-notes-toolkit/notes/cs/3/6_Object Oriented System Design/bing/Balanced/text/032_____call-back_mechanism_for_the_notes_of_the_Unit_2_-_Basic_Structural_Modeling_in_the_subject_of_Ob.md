### Call-back mechanism

- A call-back mechanism is a way of implementing event-driven programming in object-oriented languages.
- It allows an application to handle subscribed events, arising at runtime, through a listener interface .
- The listener interface defines one or more abstract methods that correspond to the events of interest.
- The subscribers (or clients) of the events will need to provide a concrete implementation of the interface methods, and register themselves with the event source (or server).
- The event source will keep a list of registered listeners, and invoke their methods when the events occur .
- The call-back mechanism enables a loose coupling between the event source and the event listeners, as they only depend on the interface and not on each other's concrete classes.
- The call-back mechanism can be used to implement various design patterns, such as observer, strategy, command, and template method .