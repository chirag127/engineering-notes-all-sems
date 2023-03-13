AWT stands for Abstract Window Toolkit, which is an API to develop graphical user interface or window-based applications in Java. AWT components are platform-dependent, meaning that they are displayed according to the view of the operating system. AWT is also heavy-weight, meaning that its components use the resources of the underlying operating system.

The basic architecture of AWT consists of four layers: the user interface components, the peer classes, the native interface, and the native code. The user interface components are the classes that provide the functionality and appearance of the GUI elements, such as buttons, labels, text fields, etc. The peer classes are the classes that communicate with the native interface and the native code to create and manage the actual GUI components on the screen. The native interface is the layer that defines the methods and constants that the peer classes use to interact with the native code. The native code is the layer that contains the platform-specific code that implements the GUI functionality.

The following diagram illustrates the basic architecture of AWT in Core Java using ASCII art:

```
+---------------------+     +---------------------+
| User Interface      |     | Peer Classes        |
| Components          |<--->|                     |
+---------------------+     +---------------------+
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
|                     |     |                     |
+---------------------+     +---------------------+
| Native Interface    |     | Native Code         |
|                     |<--->|                     |
+---------------------+     +---------------------+
```