#### Introduction to AWT in Core Java

AWT stands for Abstract Window Toolkit, which is an API (Application Programming Interface) for creating graphical user interfaces (GUIs) or windows-based applications in Java. AWT components are platform-dependent, which means that they are displayed according to the view of the operating system (OS). AWT is also heavy-weight, which means that its components use the resources of the underlying OS.

AWT provides a common set of tools for GUI design that work on a variety of platforms. The user interface elements provided by AWT are implemented using native platform versions of the components. These components are called peer components. AWT also provides layout managers, event handling, graphics, images, fonts, and colors to support GUI development.

The following diagram shows the hierarchy of AWT classes and interfaces:

```
+---------------------+
|      Object         |
+---------------------+
          ^
          |
+---------------------+
|    Component        |
+---------------------+
          ^
          |
+---------------------+---------------------+---------------------+
|    Container        |    MenuComponent    |    GraphicsDevice   |
+---------------------+---------------------+---------------------+
          ^                      ^                      ^
          |                      |                      |
+---------------------+---------------------+---------------------+
|    Window           |    MenuBar          |    GraphicsConfig.  |
+---------------------+---------------------+---------------------+
          ^                      ^                      ^
          |                      |                      |
+---------------------+---------------------+---------------------+
|    Frame            |    Menu             |    Graphics2D       |
+---------------------+---------------------+---------------------+
          ^                      ^                      ^
          |                      |                      |
+---------------------+---------------------+---------------------+
|    Dialog           |    MenuItem         |    GraphicsContext  |
+---------------------+---------------------+---------------------+
          ^                      ^                      ^
          |                      |                      |
+---------------------+---------------------+---------------------+
|    FileDialog       |    CheckboxMenuItem |    GraphicsDevice   |
+---------------------+---------------------+---------------------+
```

Some of the commonly used AWT components are:

- Button: A clickable component that performs an action when pressed.
- Label: A component that displays a single line of text.
- TextField: A component that allows the user to enter a single line of text.
- TextArea: A component that allows the user to enter multiple lines of text.
- Checkbox: A component that can be checked or unchecked by the user.
- RadioButton: A component that can be selected or deselected by the user, usually in a group of mutually exclusive options.
- List: A component that displays a list of items that the user can select from.
- Choice: A component that displays a drop-down list of items that the user can choose from.
- Scrollbar: A component that allows the user to scroll through a large amount of content.
- Canvas: A component that provides a blank area for drawing graphics or custom components.