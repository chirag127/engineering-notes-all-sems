# Java Applet Program For Calculator

- An applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly .
- Applets are not stand-alone programs, they can be viewed using direct JVM .
- Applets do not contain any main() method .
- To create a Java applet program for calculator, we need to follow these steps:

  - Import the necessary packages, such as java.applet, java.awt, and java.awt.event.
  - Extend the Applet class and implement the ActionListener interface.
  - Declare the components, such as text fields, buttons, and labels, as instance variables.
  - Initialize the components in the init() method, which is invoked by the browser when the applet is loaded.
  - Add the components to the applet using the add() method.
  - Register the applet as the listener for the buttons using the addActionListener() method.
  - Override the actionPerformed() method, which is invoked by the browser when a button is clicked.
  - Perform the arithmetic operations based on the button clicked and the values entered in the text fields.
  - Display the result in the third text field using the setText() method.

- Here is an example of a Java applet program for calculator:

```java
//Import the necessary packages
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

//Extend the Applet class and implement the ActionListener interface
public class Calculator extends Applet implements ActionListener {

  //Declare the components as instance variables
  TextField t1, t2, t3;
  Button b1, b2, b3, b4;
  Label l1, l2, l3, l4;

  //Initialize the components in the init() method
  public void init() {
    //Create the components
    t1 = new TextField(10);
    t2 = new TextField(10);
    t3 = new TextField(10);
    b1 = new Button("+");
    b2 = new Button("-");
    b3 = new Button("*");
    b4 = new Button("/");
    l1 = new Label("Enter First Number");
    l2 = new Label("Enter Second Number");
    l3 = new Label("Result");
    l4 = new Label("Calculator");

    //Set the layout of the applet
    setLayout(null);

    //Set the bounds of the components
    l4.setBounds(100, 20, 100, 20);
    l1.setBounds(20, 60, 100, 20);
    t1.setBounds(150, 60, 100, 20);
    l2.setBounds(20, 100, 100, 20);
    t2.setBounds(150, 100, 100, 20);
    b1.setBounds(20, 140, 50, 20);
    b2.setBounds(80, 140, 50, 20);
    b3.setBounds(140, 140, 50, 20);
    b4.setBounds(200, 140, 50, 20);
    l3.setBounds(20, 180, 100, 20);
    t3.setBounds(150, 180, 100, 20);

    //Add the components to the applet
    add(l4);
    add(l1);
    add(t1);
    add(l2);
    add(t2);
    add(b1);
    add(b2);
    add(b3);
    add(b4);
    add(l3);
    add(t3);

    //Register the applet as the listener for the buttons
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
    b4.addActionListener(this);
  }

  //Override the actionPerformed() method
  public void actionPerformed(ActionEvent e) {
    //Get the values from the text fields
    int n1 = Integer.parseInt(t1.getText());
    int n2 = Integer.parseInt(t2.getText());

    //Perform the arithmetic operations based on the button clicked
    if (e.getSource() == b1) {
      //Addition
      t3.setText(String.valueOf(n1 + n2));
    }
    if (e.getSource() == b2) {
      //Subtraction
      t3.setText(String.valueOf(n1 - n2));
    }
    if (e.getSource() == b3) {
      //Multiplication
      t3