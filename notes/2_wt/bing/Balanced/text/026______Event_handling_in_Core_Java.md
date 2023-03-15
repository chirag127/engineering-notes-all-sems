#### Event handling in Core Java

- An event is an action or occurrence that happens during the execution of a program, such as clicking a button, typing a key, moving a mouse, etc.
- Event handling is the process of responding to events by performing some tasks, such as updating the user interface, validating the input, executing a command, etc.
- Event handling in Core Java involves three components: event sources, event listeners, and event objects.
- An event source is an object that generates events, such as a button, a text field, a window, etc. An event source can have one or more event listeners registered with it.
- An event listener is an object that implements a specific interface that defines one or more methods to handle events of a particular type, such as ActionListener, MouseListener, WindowListener, etc. An event listener can be registered with one or more event sources.
- An event object is an instance of a class that encapsulates the information about an event, such as the source, the type, the time, the coordinates, etc. An event object is passed as a parameter to the event listener methods when an event occurs.
- The basic steps of event handling in Core Java are:

  1. Create an event source object and add it to the user interface.
  2. Create an event listener object and implement the event listener interface methods.
  3. Register the event listener object with the event source object using the appropriate method, such as addActionListener, addMouseListener, addWindowListener, etc.
  4. Write the code to perform the desired tasks in the event listener methods.