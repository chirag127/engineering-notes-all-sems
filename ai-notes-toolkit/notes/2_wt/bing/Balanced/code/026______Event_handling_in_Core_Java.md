#### Event handling in Core Java

Event handling is the mechanism that controls the behavior of an application when the user performs certain actions, such as clicking a button, typing a character, or moving the mouse. In Core Java, event handling is based on the following concepts:

- An event is an object that represents a state change in a source. For example, when the user clicks a button, an `ActionEvent` object is created.
- A source is an object that generates an event. For example, a button is a source that can generate `ActionEvent` objects.
- A listener is an object that implements a specific interface and defines methods to handle different types of events. For example, an `ActionListener` is a listener that can handle `ActionEvent` objects.
- A handler is a method that is invoked when an event occurs. For example, the `actionPerformed` method is a handler that is invoked when an `ActionEvent` occurs.
- A registration is a process that binds a listener to a source, so that the listener can receive events from the source. For example, the `addActionListener` method is used to register an `ActionListener` to a button.

To implement event handling in Core Java, the following steps are required:

- Define a listener class that implements the appropriate interface and provides the handler methods for the events of interest.
- Create an instance of the listener class and register it with the source using the appropriate method.
- Write the logic for the handler methods to perform the desired actions when the events occur.

For example, the following code shows how to implement event handling for a button click event:

```java
// Define a listener class that implements ActionListener
class ButtonListener implements ActionListener {
  // Provide the handler method for ActionEvent
  public void actionPerformed(ActionEvent e) {
    // Perform the desired action when the button is clicked
    System.out.println("Button clicked!");
  }
}

// Create a button and a listener object
Button button = new Button("Click Me");
ButtonListener listener = new ButtonListener();

// Register the listener with the button
button.addActionListener(listener);

// Add the button to a frame and make it visible
Frame frame = new Frame("Event Handling Example");
frame.add(button);
frame.setSize(300, 200);
frame.setVisible(true);
```