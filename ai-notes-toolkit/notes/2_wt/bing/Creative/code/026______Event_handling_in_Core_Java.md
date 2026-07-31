#### Event handling in Core Java

Event handling is the mechanism that controls the behavior of an application when the user performs certain actions, such as clicking a button, typing a character, or closing a window. Event handling involves the following steps:

- Creating a source object that can generate events of a specific type, such as a button that can generate action events.
- Implementing a listener interface that defines the methods to handle different types of events, such as an ActionListener that defines the actionPerformed method.
- Registering the listener object with the source object, so that the source object can notify the listener object when an event occurs.
- Defining the logic of the event handler methods, which specify what the application should do in response to the events.

Here is an example of a simple event handling program in Core Java that displays a message when the user clicks a button:

```java
// Import the necessary classes
import java.awt.*;
import java.awt.event.*;

// Create a class that extends Frame and implements ActionListener
public class EventDemo extends Frame implements ActionListener {

  // Declare a button and a label
  Button button;
  Label label;

  // Create a constructor that sets up the GUI components
  public EventDemo() {
    // Set the layout of the frame to FlowLayout
    setLayout(new FlowLayout());

    // Create a button with the text "Click Me"
    button = new Button("Click Me");

    // Create a label with the text "No message"
    label = new Label("No message");

    // Add the button and the label to the frame
    add(button);
    add(label);

    // Register the frame as the listener of the button
    button.addActionListener(this);

    // Set the title, size, and visibility of the frame
    setTitle("Event Demo");
    setSize(300, 100);
    setVisible(true);
  }

  // Define the actionPerformed method that handles the action event
  public void actionPerformed(ActionEvent e) {
    // Get the source of the event
    Object source = e.getSource();

    // If the source is the button, change the text of the label
    if (source == button) {
      label.setText("You clicked the button!");
    }
  }

  // Create the main method that launches the application
  public static void main(String[] args) {
    // Create an instance of the EventDemo class
    EventDemo demo = new EventDemo();
  }
}
```