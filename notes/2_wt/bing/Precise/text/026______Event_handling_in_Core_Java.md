#### Event handling in Core Java
Event handling in Core Java refers to the mechanism that controls the event and decides what should happen if an event occurs. This mechanism has the following key components:
1. **Event Source**: An event is generated from a source. A source is an object that generates an event. This occurs when the internal state of that object changes in some way.
2. **Event Object**: The event is represented by an object that gives information about the event and its source.
3. **Event Listener**: The listener is notified when an event occurs. It processes the event and then returns.
4. **Event Handler**: The handler is the method that processes the event. It is defined in the listener.

In Core Java, event handling is implemented using the delegation event model. This model defines standard and consistent mechanisms to generate and process events. The main advantage of this model is that it allows a clean separation between the components of an application. The event source and the event listener can be created and modified independently.

The delegation event model has the following characteristics:
- The event source is responsible for providing information about the event to the listener.
- The listener is responsible for processing the event.
- The event object contains information about the event and its source.
- The event handler is the method that is called when the event occurs.

In summary, event handling in Core Java is a powerful mechanism that allows developers to create interactive applications. It is based on the delegation event model, which provides a clean separation between the components of an application and allows for the creation of reusable and modular code.