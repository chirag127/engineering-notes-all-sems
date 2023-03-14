#### Introduction to AWT in Core Java

- AWT stands for **Abstract Window Toolkit**, which is an API to develop **Graphical User Interface (GUI)** or windows-based applications in Java.
- AWT was Java's first GUI framework, which was introduced in Java 1.0.
- AWT components are **platform-dependent**, which means they are displayed according to the view of the operating system .
- AWT is **heavyweight**, which means its components use the resources of the underlying operating system (OS).
- AWT provides classes for common GUI elements, such as buttons, text fields, labels, scrollbars, checkboxes, radio buttons, menus, dialogs, etc.
- AWT also provides classes for graphics, fonts, colors, images, events, and layouts.
- AWT uses the native GUI toolkit of each platform to create and manage the components, thereby preserving the look and feel of each platform.
- AWT follows a **hierarchy** of classes, where the topmost class is the **Component** class, which represents any GUI element.
- AWT also has a concept of **containers**, which are components that can contain and control the layout of other components.
- The most common containers in AWT are **Window**, **Panel**, **Frame**, and **Dialog**.
- AWT provides methods to add, remove, resize, and repaint components, as well as to handle user input events, such as mouse clicks, keyboard presses, etc.
- AWT is not widely used nowadays, as it has been superseded by more advanced frameworks, such as Swing and JavaFX, which are built on top of AWT.
- However, AWT is still important to know, as it provides the basic functionality and concepts for GUI programming in Java.

Some mnemonics and learning tricks for AWT are:

- AWT = Abstract Window Toolkit = A Window Toolkit
- AWT components are platform-dependent = AWT components look like the platform they run on
- AWT is heavyweight = AWT components are heavy on the OS resources
- AWT hierarchy = Component is the parent of all components
- AWT containers = Containers contain components
- AWT methods = add, remove, resize, repaint, handle events