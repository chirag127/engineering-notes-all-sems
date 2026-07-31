#### AWT controls

AWT controls are components that allow a user to interact with your application in various ways. AWT stands for Abstract Window Toolkit, which is a set of APIs for creating graphical user interfaces (GUIs) in Java  .

Some of the commonly used AWT controls are  :

- Label: A component for displaying text in a container.
- Button: A component that triggers an action when clicked.
- Checkbox: A component that can be in either an on (true) or off (false) state.
- Choice: A component that displays a pop-up menu of items.
- List: A component that displays a list of items that can be selected.
- Scrollbar: A component that allows scrolling through a large amount of data.
- TextComponent: An abstract superclass for components that allow editing text, such as TextField and TextArea.

To use AWT controls, you need to import the java.awt package, which contains all the classes for AWT API . You also need to create a container, such as a Frame or a Panel, to hold the controls. You can then add the controls to the container using the add() method. You can also set the properties of the controls, such as size, position, color, font, etc., using various methods and constructors.

Here is an example of creating a simple GUI with AWT controls:

```java
//import the java.awt package
import java.awt.*;

//create a class that extends Frame
public class AWTExample extends Frame {

  //create a constructor
  public AWTExample() {
    //set the title of the frame
    setTitle("AWT Example");
    //set the size of the frame
    setSize(300, 200);
    //set the layout of the frame
    setLayout(new FlowLayout());
    //create a label
    Label label = new Label("Hello, world!");
    //add the label to the frame
    add(label);
    //create a button
    Button button = new Button("Click me");
    //add the button to the frame
    add(button);
    //create a checkbox
    Checkbox checkbox = new Checkbox("Check me");
    //add the checkbox to the frame
    add(checkbox);
    //create a choice
    Choice choice = new Choice();
    //add some items to the choice
    choice.add("Red");
    choice.add("Green");
    choice.add("Blue");
    //add the choice to the frame
    add(choice);
    //create a list
    List list = new List(4, false);
    //add some items to the list
    list.add("Apple");
    list.add("Banana");
    list.add("Orange");
    list.add("Grape");
    //add the list to the frame
    add(list);
    //create a scrollbar
    Scrollbar scrollbar = new Scrollbar(Scrollbar.HORIZONTAL, 0, 10, 0, 100);
    //add the scrollbar to the frame
    add(scrollbar);
    //create a text field
    TextField textField = new TextField(10);
    //add the text field to the frame
    add(textField);
    //create a text area
    TextArea textArea = new TextArea(5, 20);
    //add the text area to the frame
    add(textArea);
    //make the frame visible
    setVisible(true);
  }

  //create a main method
  public static void main(String[] args) {
    //create an instance of the class
    AWTExample example = new AWTExample();
  }
}
```

This is how the GUI looks like:

![AWT Example](https://dotnettutorials.net/wp-content/uploads/2019/11/AWT-Controls-in-Java.png)