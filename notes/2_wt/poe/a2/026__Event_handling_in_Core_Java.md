 Here is the content in markdown format with formal tone and without external links or emojis:

#### Event handling in Core Java.

1. Events: Events are notifications sent by objects to notify the occurrence of an action or an incident. In Java, events are handled through listeners.
2. Listeners: Listeners are interfaces that contain methods to handle events. They listen to the events and handle them accordingly when they occur. For example, ActionListener listens to action events.
3. Event Sources: These are objects that generate events. For example, a button is an event source that generates action events.
4. Registration: Listeners have to be registered with event sources in order to listen to and handle the events. This is done using methods like addActionListener().
5. Event handling: Once a listener is registered, it handles the events by implementing methods in the listener interface. For example, the actionPerformed() method in ActionListener is implemented to handle action events.
6. Unregistration: If required, listeners can be unregistered from event sources using methods like removeActionListener(). This is done to avoid memory leaks and extraneous events.

The steps for event handling are:
1. Define a listener interface
2. Write an event handling method in the listener interface
3. Define an adapter class that implements the listener interface
4. Register the adapter class as a listener with the event source
5. Unregister the listener if required

Event handling allows loose coupling between objects and enables event-driven programming. It makes applications more responsive and easier to maintain.