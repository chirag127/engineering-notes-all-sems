AWT controls are components that allow a user to interact with your application in various ways. The AWT supports the following types of controls: Labels, Push buttons, Check boxes, Choice lists, Lists, Scroll bars, Text Editing  .

AWT controls are platform-dependent, meaning they are displayed according to the view of the operating system. AWT controls are subclasses of the Component class, which is a subclass of the Container class. A container is a component that can contain other components. The hierarchy of AWT classes is shown below .

#### AWT controls

```
+-----------------+
|    Component    |
+-----------------+
|                 |
+-----------------+
|    Container    |
+-----------------+
|                 |
+-----------------+    +-----------------+
|      Panel      |    |     Window      |
+-----------------+    +-----------------+
|                 |    |                 |
+-----------------+    +-----------------+
|      Applet     |    |      Frame      |
+-----------------+    +-----------------+
|                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |      Dialog     |    |     Button      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |    FileDialog   |    |     Label       |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |     Choice      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |     List        |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |     Checkbox    |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |     Scrollbar   |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |     TextField   |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |     TextArea    |
+-----------------+    +-----------------+    +-----------------+
```