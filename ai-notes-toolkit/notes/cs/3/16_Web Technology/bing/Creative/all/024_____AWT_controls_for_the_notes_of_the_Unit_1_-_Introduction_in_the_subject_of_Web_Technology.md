# AWT Controls

AWT stands for Abstract Window Toolkit, which is a set of APIs for creating graphical user interfaces or web applications in Java. AWT controls are the components that allow a user to interact with the application in various ways, such as buttons, text fields, checkboxes, lists, etc. AWT controls are also known as AWT components or AWT widgets.

## Structure of AWT Controls

AWT controls are organized in a hierarchy of classes, where the superclass of all AWT controls is the `java.awt.Component` class. The `Component` class provides the basic functionality and attributes of any graphical component, such as size, position, visibility, font, color, etc. The `Component` class also defines methods for handling events, such as mouse clicks, keyboard inputs, etc.

The `Component` class has two direct subclasses: `java.awt.Container` and `java.awt.Canvas`. The `Container` class represents a component that can contain other components, such as a window, a panel, a dialog, etc. The `Container` class also manages the layout and positioning of its child components. The `Canvas` class represents a component that can be used for drawing custom graphics, such as shapes, images, etc.

The `Container` class has several subclasses that represent different types of containers, such as:

- `java.awt.Window`: a top-level container that has no border, title bar, or menu bar. It is the superclass of all window types, such as frames, dialogs, etc.
- `java.awt.Frame`: a window that has a border, a title bar, and a menu bar. It is the most commonly used container for creating standalone applications.
- `java.awt.Dialog`: a window that is used for displaying a message or getting some input from the user. It is usually modal, meaning that it blocks the input to other windows until it is closed.
- `java.awt.Panel`: a container that has no border, title bar, or menu bar. It is used for grouping other components within a larger container, such as a frame or a dialog.
- `java.awt.ScrollPane`: a container that has scroll bars for viewing a large component that does not fit in the available space.
- `java.awt.Applet`: a container that is used for creating web applications that can run in a browser.

The `Canvas` class has one subclass: `java.awt.Graphics`. The `Graphics` class provides methods for drawing various shapes, text, images, etc. on a canvas.

The `Component` class also has many subclasses that represent different types of controls, such as:

- `java.awt.Label`: a component that displays a single line of text.
- `java.awt.Button`: a component that triggers an action when clicked by the user.
- `java.awt.TextField`: a component that allows the user to enter a single line of text.
- `java.awt.TextArea`: a component that allows the user to enter multiple lines of text.
- `java.awt.Checkbox`: a component that has two states: checked or unchecked. It is used for selecting or deselecting an option.
- `java.awt.CheckboxGroup`: a component that groups a set of checkboxes, such that only one checkbox can be checked at a time.
- `java.awt.Choice`: a component that displays a drop-down list of options for the user to choose from.
- `java.awt.List`: a component that displays a list of items for the user to select from. It can be single-select or multi-select.
- `java.awt.MenuBar`: a component that displays a horizontal bar of menus at the top of a window.
- `java.awt.Menu`: a component that displays a vertical list of menu items when clicked by the user.
- `java.awt.MenuItem`: a component that represents a single menu item that can trigger an action when selected by the user.
- `java.awt.PopupMenu`: a component that displays a pop-up menu when triggered by the user.
- `java.awt.FileDialog`: a component that displays a file chooser dialog for the user to select a file or a directory.
- `java.awt.ColorChooser`: a component that displays a color chooser dialog for the user to select a color.
- `java.awt.FontChooser`: a component that displays a font chooser dialog for the user to select a font.
- `java.awt.Image`: a component that displays an image.
- `java.awt.MediaTracker`: a component that tracks the loading of images and other media.
- `java.awt.Scrollbar`: a component that allows the user to scroll through a large component or a range of values.
- `java.awt.Toolkit`: a component that provides