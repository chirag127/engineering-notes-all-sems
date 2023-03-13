#### Event handling in Core Java

- Event handling is a mechanism that allows a program to respond to user actions or other occurrences, such as mouse clicks, keyboard presses, timer events, etc.
- Event handling involves three components: event sources, event listeners, and event objects.
- Event sources are the objects that generate events, such as buttons, text fields, menus, etc. Event sources have methods to register and unregister event listeners.
- Event listeners are the objects that receive and process events, such as implementing an interface or extending a class that defines the methods for handling specific types of events. Event listeners have to be registered with the event sources to receive events from them.
- Event objects are the instances of classes that encapsulate the information about the events, such as the source, the type, the time, the location, etc. Event objects are passed as parameters to the event listener methods.
- Event handling in Core Java follows the delegation model, which means that the event source delegates the responsibility of handling the event to the event listener. The event source and the event listener are loosely coupled and can interact through the event object.
- Event handling in Core Java can be implemented in two ways: using the standard Java library classes and interfaces, or using the inner classes and lambda expressions.
- Using the standard Java library classes and interfaces involves the following steps:
  - Define a class that implements the appropriate event listener interface for the type of event to be handled, such as ActionListener, MouseListener, KeyListener, etc. The event listener interface defines one or more abstract methods that have to be overridden by the implementing class.
  - Create an instance of the event listener class and register it with the event source using the addXXXListener() method, where XXX is the type of event, such as addActionListener(), addMouseListener(), addKeyListener(), etc.
  - Override the event listener methods to provide the logic for handling the events. The event listener methods receive an event object as a parameter, which can be used to access the information about the event.
  - Example:

```java
// Define a class that implements the ActionListener interface
class MyActionListener implements ActionListener {
  // Override the actionPerformed() method
  public void actionPerformed(ActionEvent e) {
    // Get the source of the event
    Object source = e.getSource();
    // Perform some action based on the source
    if (source instanceof Button) {
      // Cast the source to a Button object
      Button button = (Button) source;
      // Get the label of the button
      String label = button.getLabel();
      // Display the label in the console
      System.out.println("You clicked the button: " + label);
    }
  }
}

// Create an instance of the event listener class
MyActionListener listener = new MyActionListener();

// Create a button and register the listener with it
Button button = new Button("Click Me");
button.addActionListener(listener);
```

- Using the inner classes and lambda expressions involves the following steps:
  - Define an anonymous inner class that implements the appropriate event listener interface for the type of event to be handled, and create an instance of it. The anonymous inner class can be defined as a parameter to the addXXXListener() method of the event source, or as a separate variable. The anonymous inner class has to override the event listener methods to provide the logic for handling the events.
  - Alternatively, use a lambda expression to create an instance of the event listener interface. A lambda expression is a concise way of defining a functional interface, which is an interface that has only one abstract method. The lambda expression can be defined as a parameter to the addXXXListener() method of the event source, or as a separate variable. The lambda expression has to provide the logic for handling the events, without the need of overriding the event listener methods.
  - Example:

```java
// Define an anonymous inner class that implements the ActionListener interface
button.addActionListener(new ActionListener() {
  // Override the actionPerformed() method
  public void actionPerformed(ActionEvent e) {
    // Get the source of the event
    Object source = e.getSource();
    // Perform some action based on the source
    if (source instanceof Button) {
      // Cast the source to a Button object
      Button button = (Button) source;
      // Get the label of the button
      String label = button.getLabel();
      // Display the label in the console
      System.out.println("You clicked the button: " + label);
    }
  }
});

// Alternatively, use a lambda expression to create an instance of the ActionListener interface
button.addActionListener(e -> {
  // Get the source of the event
  Object source = e.getSource();
  // Perform some action based on the source
  if (source instanceof Button) {
    // Cast the source to