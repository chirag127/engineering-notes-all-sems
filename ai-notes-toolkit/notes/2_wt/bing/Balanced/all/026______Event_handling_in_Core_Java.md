#### Event handling in Core Java

- Event handling in Core Java is the procedure that controls an event and performs appropriate action if it occurs  .
- An event can be defined as changing the state of an object or behavior, such as clicking a button, moving the mouse, typing a key, etc .
- Event handling in Core Java consists of two major components: the event source and the event listener  .
  - The event source is the object that generates an event, such as a button, a text field, a window, etc  .
  - The event listener is the object that receives the event and responds to it, such as a class, a method, an interface, etc  .
- Event handling in Core Java follows a delegation model, which means that the event source delegates the responsibility of handling the event to the event listener  .
- To perform event handling in Core Java, the following steps are required:
  - Create the event source object and add it to the container, such as a frame, a panel, etc.
  - Implement the event listener interface that corresponds to the type of event, such as ActionListener, MouseListener, KeyListener, etc.
  - Define the event handler method that overrides the abstract method of the event listener interface, such as actionPerformed, mouseClicked, keyPressed, etc.
  - Register the event listener object with the event source object using the addXXXListener method, such as addActionListener, addMouseListener, addKeyListener, etc.
- An example of event handling in Core Java is shown below:

```java
//import the required packages
import java.awt.*;
import java.awt.event.*;

//create a class that implements the ActionListener interface
class MyActionListener implements ActionListener {
  //define the event handler method
  public void actionPerformed(ActionEvent e) {
    //display a message when the button is clicked
    System.out.println("Button clicked");
  }
}

//create a class that extends the Frame class
class MyFrame extends Frame {
  //create a button object
  Button b = new Button("Click me");
  //create an event listener object
  MyActionListener al = new MyActionListener();

  //create a constructor
  public MyFrame() {
    //set the layout of the frame
    setLayout(new FlowLayout());
    //add the button to the frame
    add(b);
    //register the event listener with the button
    b.addActionListener(al);
    //set the size and visibility of the frame
    setSize(300, 200);
    setVisible(true);
  }
}

//create a class that contains the main method
class EventDemo {
  //create a frame object
  static MyFrame f = new MyFrame();

  //main method
  public static void main(String[] args) {
    //do nothing
  }
}
```
- A possible mnemonic to remember the steps of event handling in Core Java is: **CIDER**
  - **C**reate the event source object and add it to the container
  - **I**mplement the event listener interface
  - **D**efine the event handler method
  - **E**vent listener object with the event source object
  - **R**un the program and test the event handling