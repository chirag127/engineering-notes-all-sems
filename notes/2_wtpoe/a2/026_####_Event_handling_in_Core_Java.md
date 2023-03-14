 Here is the content in markdown format for the topic #### Event handling in Core Java:

#### Event handling in Core Java

- Events in Java are objects that encapsulate some state change in the source. They are used for asynchronous communication between objects.
- The source object fires or raises an event. The listener objects that are interested in that particular event can handle it. This is known as event handling.
- The Java Event model is based on the Observer design pattern. The object that fires the event is known as the subject and the listeners that handle the event are known as observers.
- The `java.util.EventObject` class is the base class for all events in Java. The `java.awt.AWTEvent` class is the base class for AWT events. The `java.util.EventListener` interface is implemented by all listener interfaces.
- The commonly used events in Core Java are:
  - ActionEvent - fired when a button is clicked, menu item selected, etc. Used with Swing components.
  - MouseEvent - fired when mouse-related actions occur like click, drag, move, etc. Used with AWT and Swing components.
  - KeyEvent - fired when keyboard-related actions occur like key press, key release, etc. Used with AWT and Swing components.
  - WindowEvent - fired when a window is opened, closed, iconified, deiconified, etc. Used with AWT and Swing components.
- To handle events:
  - Implement the appropriate listener interface like ActionListener, MouseListener, etc.
  - Register the listener object with the source using methods like addActionListener(), addMouseListener(), etc.
  - The source will call the appropriate method in the listener interface when the event occurs. For ex: actionPerformed() method in ActionListener.
- Advantages:
  - Decouples the source and listener. The source doesn't need to know which listeners are listening to it.
  - Supports multicasting - a single event can be handled by multiple listeners.
  - Follows observer pattern leading to loosely coupled and flexible design.
- Disadvantages:
  - The listener has to implement several empty methods even if it is interested in only one type of event.
  - The source and listener are tightly coupled by the listener registration process.
- Common mnemonics:
  - Occurrence of event - Something happened (state change)
  - Event object - Encapsulates what happened
  - Listener - Interested in event
  - Register - Sign up to know about events
  - Handle - Respond to event occurrence