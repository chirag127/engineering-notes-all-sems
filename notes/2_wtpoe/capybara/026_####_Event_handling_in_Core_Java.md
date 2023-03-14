#### Event handling in Core Java

In Core Java, event handling is a mechanism to handle the events that occur during the execution of a program. Events can be anything from a button click to a key press or a mouse movement. The event handling mechanism consists of two components:

1. Event Sources: The objects that generate the events are called event sources. For example, a button is an event source that generates an event when it is clicked.

2. Event Listeners: The objects that receive and handle the events are called event listeners. For example, a button click event can be handled by an ActionListener.

##### Types of Events:
There are many types of events in Core Java. Some of the commonly used events are:

- ActionEvent: This event is generated when a button is clicked or a menu item is selected.
- KeyEvent: This event is generated when a key is pressed or released.
- MouseEvent: This event is generated when the mouse is moved or clicked.
- WindowEvent: This event is generated when a window is opened, closed, or resized.

##### Event Handling Procedure:
The event handling procedure consists of the following steps:

1. Define an event source object.
2. Create an event listener object.
3. Register the event listener object with the event source object.
4. Implement the event handling method in the event listener object.

##### Mnemonics and Learning Tricks:
One mnemonic to remember the steps of event handling is "DERI" which stands for Define, Event, Register, Implement.

Another trick is to remember that the event handling procedure is like a telephone call. The event source is the person making the call, the event listener is the person receiving the call, and the event handling method is the conversation between them.

##### Advantages of Event Handling:
- It allows for interactive and responsive programs.
- It separates the event handling logic from the main program logic, making the code more modular and easier to maintain.
- It allows for multiple event listeners to be registered with a single event source, providing flexibility in the design of the program.

##### Disadvantages of Event Handling:
- It can add complexity to the program, especially when dealing with multiple event sources and listeners.
- It can be difficult to debug event handling code due to the asynchronous nature of events.

##### Examples:
Here is an example of how to handle a button click event in Core Java:

```java
import java.awt.*;
import java.awt.event.*;

public class ButtonExample implements ActionListener {
   private Button button;
   private Label label;
   
   public ButtonExample() {
      Frame frame = new Frame("Button Example");
      button = new Button("Click Me");
      label = new Label();
      button.addActionListener(this);
      frame.add(button, BorderLayout.CENTER);
      frame.add(label, BorderLayout.SOUTH);
      frame.pack();
      frame.setVisible(true);
   }
   
   public void actionPerformed(ActionEvent e) {
      label.setText("Button Clicked");
   }
   
   public static void main(String[] args) {
      new ButtonExample();
   }
}
```

##### Applications:
Event handling is used in many types of applications, including:
- Graphical User Interfaces (GUIs)
- Games
- Web applications
- Mobile applications