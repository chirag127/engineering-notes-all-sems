#### Event handling in Core Java

Event handling is a mechanism in Core Java that allows a user to interact with a graphical user interface (GUI) by performing actions such as clicking a button, selecting an item from a list, or entering text into a text field. These actions generate events, which are then handled by the program to perform the desired action.

Here are some key points to remember about event handling in Core Java:

1. An event is an object that represents a change in the state of a GUI component, such as a button being clicked or a key being pressed.
2. Event handling involves three main components: the event source, the event object, and the event listener.
3. The event source is the GUI component that generates the event, such as a button or a text field.
4. The event object contains information about the event, such as the type of event and the source of the event.
5. The event listener is an object that receives the event and performs the appropriate action in response to the event.
6. Event listeners are registered with the event source using the `addActionListener` method or a similar method.
7. When an event is generated, the event source calls the appropriate method on the registered event listener, passing the event object as a parameter.
8. The event listener then performs the appropriate action in response to the event, such as updating the GUI or performing a calculation.

In summary, event handling in Core Java allows a user to interact with a GUI by generating events, which are then handled by the program to perform the desired action. This involves the use of event sources, event objects, and event listeners.