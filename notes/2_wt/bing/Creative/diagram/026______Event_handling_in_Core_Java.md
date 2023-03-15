Event handling in Java is a mechanism that allows a program to respond to user actions or other events, such as mouse clicks, keyboard inputs, timer ticks, etc. Event handling involves three components: event sources, event listeners, and event handlers. Event sources are the objects that generate events, such as buttons, text fields, menus, etc. Event listeners are the objects that register themselves to receive events from event sources, such as action listeners, mouse listeners, key listeners, etc. Event handlers are the methods that implement the logic to handle the events, such as actionPerformed, mouseClicked, keyPressed, etc.

A diagram for event handling in core Java is shown below:

#### Event handling in Core Java
```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Event Source  |----->|  Event Object  |----->|  Event Queue   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  v
       |                                        +----------------+
       |                                        |                |
       |                                        |  Event Dequeue |
       |                                        |                |
       |                                        +----------------+
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  v
       |                                        +----------------+
       |                                        |                |
       |                                        |  Event Dispatch|
       |                                        |                |
       |                                        +----------------+
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  v
       |                                        +----------------+
       |                                        |                |
       |                                        |  Event Listener|
       |                                        |                |
       |                                        +----------------+
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  v
       |                                        +----------------+
       |                                        |                |
       |                                        |  Event Handler |
       |                                        |                |
       |                                        +----------------+
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  v
       |                                        +----------------+
       |                                        |                |
       |                                        |  Program Logic |
       |                                        |                |
       |                                        +----------------+
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  |
       |                                                  v
       |                                        +----------------+
       |                                        |                |
       |                                        |  Program Output|
       |                                        |                |
       |                                        +----------------+
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       v
+----------------+
|                |
|  Event Source  |
|                |
+----------------+
```