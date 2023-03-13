#### Event handling in Core Java

- An event is an action or occurrence that happens during the execution of a program, such as clicking a button, typing a key, moving a mouse, etc.
- Event handling is the process of responding to events by defining the logic or behavior that should be executed when an event occurs.
- Event handling in Core Java involves the following components:
  - Event sources: The objects that generate events, such as buttons, text fields, menus, etc.
  - Event listeners: The objects that receive events and perform the appropriate actions, such as implementing an interface or extending a class that defines the event handling methods.
  - Event objects: The objects that encapsulate the information about an event, such as the source, the type, the time, the coordinates, etc.
- Event handling in Core Java follows the delegation model, which means that the event source delegates the responsibility of handling the event to a separate event listener object.
- To handle an event in Core Java, the following steps are required:
  - Create an event source object and register one or more event listeners to it using the `addXXXListener()` method, where `XXX` is the type of the event, such as `Action`, `Mouse`, `Key`, etc.
  - Implement the event listener interface or extend the event adapter class that corresponds to the type of the event, and override the event handling methods that are invoked when the event occurs.
  - Write the logic or behavior that should be executed inside the event handling methods, using the event object as a parameter to access the information about the event.