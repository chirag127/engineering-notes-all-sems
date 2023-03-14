#### Event handling in Core Java

- Event handling is a mechanism that allows a program to respond to user actions or other occurrences, such as mouse clicks, keyboard presses, timer ticks, etc.
- Event handling involves three components: event sources, event listeners, and event objects.
- Event sources are the objects that generate events, such as buttons, text fields, menus, etc. Event sources have methods to register and unregister event listeners.
- Event listeners are the objects that receive and process events, such as action listeners, mouse listeners, key listeners, etc. Event listeners implement interfaces that define one or more methods to handle specific types of events.
- Event objects are the instances of classes that encapsulate the information about an event, such as its source, type, time, location, etc. Event objects are passed as parameters to the event listener methods.
- The process of event handling in core Java can be summarized as follows:
  - An event source registers one or more event listeners using the appropriate methods, such as `addActionListener`, `addMouseListener`, `addKeyListener`, etc.
  - When an event occurs, the event source creates an event object and invokes the corresponding method on each registered event listener, passing the event object as a parameter.
  - The event listener receives the event object and performs the appropriate action, such as updating the user interface, performing calculations, etc.
- A common pattern for event handling in core Java is to use anonymous inner classes or lambda expressions to create and register event listeners, such as:

```java
// Using an anonymous inner class
button.addActionListener(new ActionListener() {
  @Override
  public void actionPerformed(ActionEvent e) {
    // Handle the button click
  }
});

// Using a lambda expression
button.addActionListener(e -> {
  // Handle the button click
});
```

- Some advantages of event handling in core Java are:
  - It allows for a modular and decoupled design, where the event sources and event listeners are independent of each other and can be reused or replaced easily.
  - It allows for a responsive and interactive user interface, where the program can react to user actions or other events in real time.
  - It allows for a flexible and extensible framework, where new types of events and event listeners can be added or removed without affecting the existing code.
- Some disadvantages of event handling in core Java are:
  - It can introduce complexity and verbosity, especially when there are many event sources and event listeners involved, or when the event listener code is long or complicated.
  - It can introduce performance and memory overhead, as each event object and event listener consumes some resources, and the event dispatching and handling may take some time.
  - It can introduce concurrency and synchronization issues, as events may occur in different threads and may require access to shared resources, such as variables, files, databases, etc.