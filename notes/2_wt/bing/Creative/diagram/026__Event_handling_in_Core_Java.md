Event handling in Core Java is the mechanism to control the events and to decide what should happen after an event occurs. An event can be defined as changing the state of an object or behavior by performing actions, such as clicking a button, moving the mouse, pressing a key, etc. Core Java follows the delegation event model, which has sources and listeners. Sources are the objects that generate events, such as buttons, text fields, menus, etc. Listeners are the objects that handle the events, such as action listeners, mouse listeners, key listeners, etc. To perform event handling, we need to register the source with the listener using the addTypeListener() method, where Type represents the type of event.

The following diagram illustrates the basic architecture of event handling in Core Java using ASCII art:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Event        |      |    Event        |      |    Listener     |
|    Source       |----->|    Object       |----->|    Interface    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Button       |----->|    ActionEvent  |----->|    ActionListener|
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    TextField    |----->|    TextEvent    |----->|    TextListener |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Mouse        |----->|    MouseEvent   |----->|    MouseListener|
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Keyboard     |----->|    KeyEvent     |----->|    KeyListener  |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```