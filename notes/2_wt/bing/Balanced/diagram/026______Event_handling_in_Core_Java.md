Event handling in Java is the process of controlling an event and performing appropriate action if it occurs. An event is any change in the state of an object, such as a button being clicked, a mouse being moved, or a key being pressed. An event handler is the code or set of instructions that implements the response to an event. It consists of two major components: the event source and the event listener.

The event source is the object that generates or triggers the event. For example, a button is an event source that can generate a click event when the user presses it. The event source has a list of registered event listeners that are interested in the event.

The event listener is the object that receives the notification of the event and performs the action accordingly. For example, a class that implements the ActionListener interface is an event listener that can handle the click event of a button. The event listener must implement the appropriate event handling interface and register itself with the event source.

The following diagram shows the basic structure of event handling in core Java using ASCII art:

#### Event handling in Core Java

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Event Source   |        |  Event Object   |        |  Event Listener |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  - List of      |        |  - Event type   |        |  - Event        |
|    registered   |        |  - Event source |        |    handling     |
|    listeners    |        |  - Event data   |        |    interface    |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  + generate()   |------->|  + getEvent()   |------->|  + handle()     |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```

The event source generates an event object that contains the information about the event, such as the event type, the event source, and the event data. The event object is passed to the getEvent() method of the event listener. The event listener then calls the handle() method to perform the appropriate action based on the event object.