#### Introduction to AWT in Core Java

AWT (Abstract Window Toolkit) is a Java API that provides a graphical user interface (GUI) for Java programs. It is part of the Java Foundation Classes (JFC) and includes classes for creating windows, dialogs, buttons, text fields, and other GUI components.

Here is an ASCII diagram that shows the hierarchy of some of the main classes in the AWT package:

```
java.lang.Object
   |
   +--java.awt.Component
       |
       +--java.awt.Container
           |
           +--java.awt.Panel
           |   |
           |   +--java.awt.Applet
           |
           +--java.awt.Window
               |
               +--java.awt.Frame
                   |
                   +--java.awt.Dialog
```

In this diagram, each class is a subclass of the class above it. For example, `java.awt.Panel` is a subclass of `java.awt.Container`, which is a subclass of `java.awt.Component`, which is a subclass of `java.lang.Object`. This means that a `Panel` object inherits all the methods and fields of a `Container`, a `Component`, and an `Object`.
