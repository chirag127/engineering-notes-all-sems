# Call-back mechanism for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- A call-back mechanism is a way of implementing event-driven programming in object-oriented languages that do not support function-valued arguments .
- A call-back mechanism allows an application to handle subscribed events, arising at runtime, through a listener interface .
- A listener interface is an abstract class or an interface that defines one or more methods that will be invoked when an event occurs .
- The subscribers, or the objects that are interested in the events, will need to provide a concrete implementation of the listener interface and register it with the event source  .
- The event source, or the object that generates the events, will keep a list of registered listeners and call their methods when an event happens  .
- A call-back mechanism enables a loose coupling between the event source and the event listeners, as they only depend on the listener interface and not on each other's concrete classes  .
- A call-back mechanism can be implemented using various design patterns, such as the observer pattern, the strategy pattern, or the command pattern .
- A call-back mechanism is useful for designing reactive systems that need to respond to external stimuli, such as user input, network messages, or sensor data  .
- A call-back mechanism is also useful for designing modular systems that can be extended or customized by adding or removing listeners  .