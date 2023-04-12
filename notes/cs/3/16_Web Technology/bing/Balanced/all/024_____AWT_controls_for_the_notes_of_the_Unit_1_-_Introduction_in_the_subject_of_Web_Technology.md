# AWT Controls

AWT stands for Abstract Window Toolkit, which is a set of APIs for creating graphical user interfaces or web applications in Java. AWT controls are the components that allow a user to interact with the application in various ways, such as entering text, clicking buttons, selecting options, etc. AWT controls are also known as AWT components or AWT widgets.

Some of the common AWT controls are:

- Label: A component that displays a single line of text, usually for identification purposes.
- Button: A component that triggers an action when clicked by the user.
- TextField: A component that allows the user to enter a single line of text.
- TextArea: A component that allows the user to enter multiple lines of text.
- Checkbox: A component that represents a binary choice, either on or off.
- CheckboxGroup: A component that groups a set of checkboxes, allowing only one to be selected at a time.
- Choice: A component that displays a drop-down list of options, allowing the user to select one.
- List: A component that displays a scrollable list of items, allowing the user to select one or more.
- Canvas: A component that provides a blank area for drawing graphics or images.
- Scrollbar: A component that allows the user to scroll through a large area of content.
- Dialog: A component that displays a pop-up window with a title, a message, and optionally some buttons.
- FileDialog: A component that displays a file chooser dialog, allowing the user to select a file or a directory.

All AWT controls are subclasses of the java.awt.Component class, which provides the basic functionality and properties of a graphical component, such as size, position, visibility, background color, font, etc. AWT controls can be added to a container, which is another type of component that can hold other components. The most common container is the java.awt.Panel class, which provides a generic area for grouping components. A panel can be added to another container, such as a java.awt.Window class, which represents a top-level window with a title bar, a border, and optionally a menu bar. A window can be either a java.awt.Frame class, which is a normal window that can be resized, minimized, maximized, or closed by the user, or a java.awt.Dialog class, which is a modal window that blocks the input to other windows until it is closed.

The following diagram shows the hierarchy of AWT controls and containers:

![AWT Hierarchy](https://www.educba.com/wp-content/uploads/2019/11/Java-AWT-Controls-1.png)

To create and use AWT controls, you need to import the java.awt package, which contains all the classes and interfaces for AWT. You also need to implement the java.awt.event.ActionListener interface, which defines the method actionPerformed(ActionEvent e) that is invoked when a user performs an action on a component, such as clicking a button. You can register an action listener to a component by calling the addActionListener(ActionListener l) method of the component. You can also implement other event listener interfaces, such as java.awt.event.ItemListener, java.awt.event.KeyListener, java.awt.event.MouseListener, etc., depending on the type of events you want to handle.

The following code snippet shows an example of creating and using some AWT controls:

```java
import java.awt.*;
import java.awt.event.*;

public class AWTExample extends Frame implements ActionListener {

    // Declare some AWT controls
    Label l1, l2, l3;
    Button b1, b2;
    TextField tf1, tf2;
    Checkbox cb1, cb2, cb3;
    CheckboxGroup cbg;
    Choice ch;
    List ls;

    public AWTExample() {
        // Set the title and layout of the frame
        super("AWT Example");
        setLayout(new FlowLayout());

        // Create and add the label components
        l1 = new Label("Enter your name:");
        l2 = new Label("Select your gender:");
        l3 = new Label("Select your hobbies:");
        add(l1);
        add(l2);
        add(l3);

        // Create and add the button components
        b1 = new Button("Submit");
        b2 = new Button("Reset");
        add(b1);
        add(b2);

        // Create and add the text field components
        tf1 = new TextField(20);
        tf2 = new TextField(20);
        add(tf1);
        add(tf2);

        // Create and add the checkbox components
        cb1 = new Checkbox("Male

```
