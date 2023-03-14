#### Event handling in Core Java

- Event handling in Core Java is the mechanism to control the events and to decide what should happen after an event occurs.
- An event can be defined as changing the state of an object or behavior by performing actions, such as clicking a button, moving the mouse, pressing a key, etc.
- The `java.awt.event` package provides many event classes and listener interfaces for event handling.
- Java follows the delegation event model, which has sources and listeners.
- Sources are the objects that generate events, such as buttons, checkboxes, text fields, etc.
- Listeners are the objects that handle the events, such as action listeners, mouse listeners, key listeners, etc.
- To perform event handling, we need to register the source with the listener, using the `addTypeListener()` method, where `Type` represents the type of event.
- We can put the event handling code into one of the following places: within the class, other class, or anonymous class.
- We can implement the listener interface in the same class, a different class, or an anonymous inner class, and override the abstract methods to handle the events.