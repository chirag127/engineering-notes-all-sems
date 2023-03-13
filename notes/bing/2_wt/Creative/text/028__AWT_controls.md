#### AWT controls

- AWT stands for Abstract Window Toolkit, which is a set of APIs for creating graphical user interfaces (GUIs) in Java .
- AWT controls are components that allow a user to interact with the GUI in various ways, such as entering text, selecting options, clicking buttons, etc .
- AWT controls are also called heavy-weight components, because they rely on the native operating system (OS) for their appearance and functionality .
- The java.awt package provides classes for AWT controls, such as Label, Button, Checkbox, Choice, List, Scrollbar, TextField, TextArea, etc .
- Some of the commonly used AWT controls are:

  - Label: A component for displaying text in a container.
  - Button: A component for triggering an action when clicked.
  - Checkbox: A component for selecting or deselecting an option in a binary state.
  - Choice: A component for selecting one option from a drop-down list.
  - List: A component for displaying and selecting multiple items from a scrollable list.
  - Scrollbar: A component for adjusting the visible portion of a container or a component.
  - TextField: A component for entering and editing a single line of text.
  - TextArea: A component for entering and editing multiple lines of text.

- To use AWT controls, you need to import the java.awt package, create an instance of the desired control class, and add it to a container, such as a Frame or a Panel .
- For example, the following code snippet creates a Label, a Button, and a TextField, and adds them to a Frame:

```java
import java.awt.*;
public class AWTExample {
  public static void main(String[] args) {
    // Create a frame
    Frame frame = new Frame("AWT Example");
    // Set the layout manager
    frame.setLayout(new FlowLayout());
    // Create a label
    Label label = new Label("Enter your name:");
    // Create a button
    Button button = new Button("Submit");
    // Create a text field
    TextField textField = new TextField(20);
    // Add the components to the frame
    frame.add(label);
    frame.add(textField);
    frame.add(button);
    // Set the size and visibility of the frame
    frame.setSize(300, 200);
    frame.setVisible(true);
  }
}
```