#### Event handling in Core Java

- An event is an action or occurrence that happens during the execution of a program, such as clicking a button, moving the mouse, typing a key, etc.
- Event handling is the process of responding to an event by performing some tasks, such as updating the user interface, validating the input, executing a command, etc.
- Event handling in Core Java involves the following components:
  - Event source: The object that generates an event, such as a button, a text field, a window, etc.
  - Event listener: The object that receives the notification of an event and defines the logic to handle it, such as a class that implements an interface or extends an abstract class.
  - Event object: The object that encapsulates the information about an event, such as its type, source, time, etc.
- Event handling in Core Java follows the delegation model, which means that the event source delegates the responsibility of handling the event to the event listener.
- To handle an event in Core Java, the following steps are required:
  - Register the event listener with the event source, using methods such as `addActionListener()`, `addMouseListener()`, `addWindowListener()`, etc.
  - Implement the event listener interface or extend the event adapter class, and override the methods that correspond to the events of interest, such as `actionPerformed()`, `mouseClicked()`, `windowClosing()`, etc.
  - In the event listener methods, write the code to handle the event, using the event object as a parameter, and access its methods and fields, such as `getSource()`, `getType()`, `getX()`, `getY()`, etc.