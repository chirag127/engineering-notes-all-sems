#### Event handling in Core Java

Event handling in Core Java is the process of controlling an event and performing appropriate action if it occurs. An event is a change in the state of an object or a user action, such as clicking a button, moving the mouse, typing a key, etc. An event handler is a code or a set of instructions that is executed when an event occurs. It consists of two major components: event sources and event listeners.

Event sources are the objects that generate events, such as buttons, text fields, menus, etc. Event listeners are the objects that receive events and handle them, such as action listeners, mouse listeners, key listeners, etc. Event sources and event listeners are connected by a mechanism called event delegation, which allows the event source to delegate the responsibility of handling the event to the event listener.

The following diagram illustrates the basic architecture of event handling in Core Java:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Event Source  |       |  Event Object  |       | Event Listener |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |  generate event       |                       |
       +---------------------->|                       |
       |                       |                       |
       |                       |  notify listener      |
       |                       +---------------------->|
       |                       |                       |
       |                       |  handle event         |
       |                       |<----------------------+
       |                       |                       |
       |                       |                       |
       V                       V                       V
```

The steps to perform event handling in Core Java are:

1. Create an event source object and add it to the GUI component.
2. Create an event listener object that implements the appropriate listener interface for the event type.
3. Register the event listener object with the event source object using the addXXXListener() method, where XXX is the event type.
4. Define the event handler method in the event listener object that overrides the abstract method of the listener interface. The event handler method takes an event object as a parameter and performs the desired action.