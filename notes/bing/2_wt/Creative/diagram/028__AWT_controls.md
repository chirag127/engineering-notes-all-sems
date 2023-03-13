AWT controls are components that allow a user to interact with your application in various ways. The AWT supports the following types of controls: Labels, Push buttons, Check boxes, Choice lists, Lists, Scroll bars, and Text Editing  .

#### AWT controls

The following diagram illustrates the basic architecture of AWT controls using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
| java.awt.Component |<---| java.awt.Label |<---| java.awt.Button |
+-----------------+    +-----------------+    +-----------------+
          ^                      ^                      ^
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
+-----------------+    +-----------------+    +-----------------+
| java.awt.Container |<---| java.awt.Panel |<---| java.awt.ScrollPane |
+-----------------+    +-----------------+    +-----------------+
          ^                      ^                      ^
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
          |                      |                      |
+-----------------+    +-----------------+    +-----------------+
| java.awt.Window |<---| java.awt.Frame |<---| java.awt.Dialog |
+-----------------+    +-----------------+    +-----------------+
```

Each control is a subclass of the java.awt.Component class, which provides the basic functionality for all components. Some controls, such as Panel, ScrollPane, Window, Frame, and Dialog, are subclasses of the java.awt.Container class, which allows them to contain other components  .