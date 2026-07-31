#### Introduction to AWT in Core Java

AWT stands for Abstract Window Toolkit. It is a package of classes and interfaces that provides a platform-independent way of creating graphical user interfaces (GUIs) in Java. AWT provides components such as buttons, labels, text fields, menus, dialogs, etc. that can be used to create windows, frames, panels, and other GUI elements. AWT also provides classes for handling events, graphics, fonts, colors, images, and other resources.

To use AWT in Core Java, you need to import the java.awt package and its subpackages, such as java.awt.event, java.awt.image, etc. You also need to extend the java.awt.Frame class or use an instance of it to create a window for your GUI. You can then add components to the frame using the add() method or using a layout manager. You can also register listeners for handling user events, such as mouse clicks, keyboard inputs, window closing, etc.

Here is an example of a simple AWT program that creates a window with a button and a label:

```java
//import the necessary packages
import java.awt.*;
import java.awt.event.*;

//create a class that extends Frame
public class AWTExample extends Frame implements ActionListener {

  //declare the components
  Button button;
  Label label;

  //create a constructor
  public AWTExample() {
    //set the title, size, and layout of the frame
    setTitle("AWT Example");
    setSize(300, 200);
    setLayout(new FlowLayout());

    //create and add the button
    button = new Button("Click Me");
    add(button);

    //create and add the label
    label = new Label("Hello, World!");
    add(label);

    //register the action listener for the button
    button.addActionListener(this);

    //make the frame visible
    setVisible(true);
  }

  //override the actionPerformed method to handle the button click
  public void actionPerformed(ActionEvent e) {
    //change the text of the label
    label.setText("You clicked the button!");
  }

  //create the main method
  public static void main(String[] args) {
    //create an instance of the class
    AWTExample example = new AWTExample();
  }
}
```