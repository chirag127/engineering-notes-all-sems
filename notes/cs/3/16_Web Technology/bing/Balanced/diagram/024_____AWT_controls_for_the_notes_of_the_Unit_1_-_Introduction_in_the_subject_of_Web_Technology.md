### AWT controls

AWT stands for Abstract Window Toolkit, which is a set of APIs for creating graphical user interfaces or web applications in Java. AWT controls are the components that allow a user to interact with the application in various ways, such as entering text, clicking buttons, selecting options, etc. AWT controls are also known as AWT components or AWT widgets.

Some of the common AWT controls are:

- Label: A component that displays a single line of text, usually for identification purposes.
- Button: A component that triggers an action when clicked by the user.
- CheckBox: A component that represents a binary choice, such as yes/no or on/off. It can be checked or unchecked by the user.
- CheckBoxGroup: A component that groups a set of CheckBoxes, such that only one CheckBox can be checked at a time within the group.
- List: A component that displays a list of items, from which the user can select one or more items.
- TextField: A component that allows the user to enter a single line of text.
- TextArea: A component that allows the user to enter multiple lines of text.
- Choice: A component that displays a drop-down list of items, from which the user can select one item.
- Canvas: A component that provides a blank area for drawing graphics or images.
- Image: A component that displays an image file.
- Scrollbar: A component that allows the user to scroll through a large area of content, such as a text or an image.
- Dialog: A component that displays a pop-up window with a title, a message, and optionally some buttons or other controls.
- FileDialog: A component that displays a file chooser dialog, which allows the user to select a file or a directory from the file system.

The following diagram shows the hierarchy of AWT controls, which are subclasses of the Component class:

```
Component
|
+--Container
|  |
|  +--Window
|  |  |
|  |  +--Frame
|  |  |
|  |  +--Dialog
|  |     |
|  |     +--FileDialog
|  |
|  +--Panel
|  |  |
|  |  +--Applet
|  |
|  +--ScrollPane
|
+--Label
|
+--Button
|
+--Checkbox
|
+--Choice
|
+--List
|
+--Scrollbar
|
+--TextField
|
+--TextArea
|
+--Canvas
```