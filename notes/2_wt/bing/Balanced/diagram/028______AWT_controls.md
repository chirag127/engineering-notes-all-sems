#### AWT controls

- AWT stands for Abstract Window Toolkit, which is a set of APIs for creating graphical user interfaces (GUIs) in Java.
- AWT controls are components that allow a user to interact with the GUI in various ways, such as entering text, selecting options, clicking buttons, etc.
- AWT controls are also called heavy-weight components, because they rely on the native operating system (OS) for their appearance and functionality.
- The java.awt package contains the classes and interfaces for AWT controls, such as Label, Button, Checkbox, Choice, List, Scrollbar, TextField, TextArea, etc .
- AWT controls can be added to a container, such as a Frame, Panel, or Applet, using the add() method of the container.
- AWT controls can be customized by setting their properties, such as size, location, color, font, text, etc, using the corresponding methods of the component class.
- AWT controls can also respond to user events, such as mouse clicks, keyboard inputs, etc, by implementing the appropriate listener interfaces and registering them with the component using the addXXXListener() method, where XXX is the type of event.

Example of AWT controls in Java:

```java
//Import the java.awt package
import java.awt.*;

//Create a class that extends Frame
public class AWTControlsExample extends Frame {

  //Declare the AWT controls as instance variables
  private Label lblName;
  private TextField txtName;
  private Button btnSubmit;
  private Checkbox chkAgree;
  private Choice chcColor;
  private List lstFruits;
  private TextArea txtOutput;

  //Create a constructor that initializes the AWT controls and adds them to the frame
  public AWTControlsExample() {
    //Set the layout of the frame to FlowLayout
    setLayout(new FlowLayout());

    //Create a label with the text "Name:"
    lblName = new Label("Name:");

    //Create a text field with 20 columns
    txtName = new TextField(20);

    //Create a button with the text "Submit"
    btnSubmit = new Button("Submit");

    //Create a checkbox with the text "I agree to the terms and conditions"
    chkAgree = new Checkbox("I agree to the terms and conditions");

    //Create a choice with three options: "Red", "Green", and "Blue"
    chcColor = new Choice();
    chcColor.add("Red");
    chcColor.add("Green");
    chcColor.add("Blue");

    //Create a list with four items: "Apple", "Banana", "Orange", and "Grape"
    lstFruits = new List(4);
    lstFruits.add("Apple");
    lstFruits.add("Banana");
    lstFruits.add("Orange");
    lstFruits.add("Grape");

    //Create a text area with 5 rows and 40 columns
    txtOutput = new TextArea(5, 40);

    //Add the AWT controls to the frame
    add(lblName);
    add(txtName);
    add(btnSubmit);
    add(chkAgree);
    add(chcColor);
    add(lstFruits);
    add(txtOutput);

    //Set the title, size, and visibility of the frame
    setTitle("AWT Controls Example");
    setSize(500, 300);
    setVisible(true);
  }

  //Create a main method that creates an instance of the class
  public static void main(String[] args) {
    new AWTControlsExample();
  }
}
```

Output:

![AWT Controls Example](https://dotnettutorials.net/wp-content/uploads/2019/10/AWT-Controls-in-Java.png)