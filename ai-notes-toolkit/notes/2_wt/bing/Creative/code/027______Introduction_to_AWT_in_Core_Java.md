#### Introduction to AWT in Core Java

AWT stands for Abstract Window Toolkit, which is an API (Application Programming Interface) for creating graphical user interface (GUI) or window-based applications in Java . AWT provides various components like button, label, checkbox, etc. used as objects inside a Java program. AWT components are platform-dependent, which means that they are displayed according to the view of the operating system . AWT also provides a well-designed object-oriented interface to the low-level services and resources of the operating system, such as graphics, fonts, colors, events, etc.

To use AWT in a Java program, we need to import the `java.awt` package, which contains all the classes and interfaces for AWT components and events. We also need to extend the `java.awt.Frame` class, which represents a window with a title bar and borders. The `Frame` class has methods to add components, set the size and location, and show or hide the window. We also need to implement the `java.awt.event.WindowListener` interface, which provides methods to handle the window events, such as closing, opening, activating, etc.

Here is an example of a simple AWT program that creates a window with a button and a label:

```java
//import the java.awt package
import java.awt.*;

//import the java.awt.event package
import java.awt.event.*;

//create a class that extends Frame and implements WindowListener
public class AWTExample extends Frame implements WindowListener {

  //declare the components
  Button button;
  Label label;

  //create a constructor
  public AWTExample() {
    //set the layout of the window
    setLayout(new FlowLayout());

    //create a button with a label
    button = new Button("Click Me");

    //create a label with some text
    label = new Label("Hello World");

    //add the components to the window
    add(button);
    add(label);

    //add the window listener to the window
    addWindowListener(this);
  }

  //override the windowClosing method to close the window
  public void windowClosing(WindowEvent e) {
    //dispose the window
    dispose();
  }

  //override the other window listener methods with empty bodies
  public void windowOpened(WindowEvent e) {}
  public void windowClosed(WindowEvent e) {}
  public void windowIconified(WindowEvent e) {}
  public void windowDeiconified(WindowEvent e) {}
  public void windowActivated(WindowEvent e) {}
  public void windowDeactivated(WindowEvent e) {}

  //create a main method
  public static void main(String[] args) {
    //create an instance of the class
    AWTExample awtExample = new AWTExample();

    //set the size of the window
    awtExample.setSize(300, 200);

    //set the title of the window
    awtExample.setTitle("AWT Example");

    //set the visibility of the window
    awtExample.setVisible(true);
  }
}
```