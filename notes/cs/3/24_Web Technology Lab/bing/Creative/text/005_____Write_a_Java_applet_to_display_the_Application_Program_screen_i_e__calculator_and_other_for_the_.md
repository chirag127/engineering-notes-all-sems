### Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

- A Java applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly .
- A Java applet program for calculator can use a grid layout to arrange buttons for the digits and for the addition, subtraction, multiplication, and division operations.
- A Java applet program for calculator can also use a text field to display the first and second numbers and results .
- A Java applet program for calculator can add an action listener to each button to perform the corresponding arithmetic operation.
- A Java applet program for calculator can use the following steps to create and run the applet:

  - Import the necessary packages, such as java.applet, java.awt, and java.awt.event.
  - Define a class that extends the Applet class and implements the ActionListener interface.
  - Declare the components, such as buttons, text fields, and labels, as instance variables of the class.
  - Override the init() method to initialize the components and add them to the applet.
  - Override the actionPerformed() method to handle the button clicks and perform the calculations.
  - Compile the applet class and create an HTML file that contains the <applet> tag with the appropriate attributes, such as code, width, and height.
  - Run the applet using a web browser or an applet viewer.

- A sample code for a Java applet program for calculator is given below:

```java
// Import the necessary packages
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

// Define a class that extends the Applet class and implements the ActionListener interface
public class CalculatorApplet extends Applet implements ActionListener {

  // Declare the components as instance variables
  Button b1, b2, b3, b4, b5, b6, b7, b8, b9, b0, bAdd, bSub, bMul, bDiv, bEq, bClr;
  TextField tf;
  Label l;
  String op;
  int num1, num2, result;

  // Override the init() method to initialize the components and add them to the applet
  public void init() {
    // Set the layout to grid layout with 4 rows and 4 columns
    setLayout(new GridLayout(4, 4));

    // Create the buttons and assign them labels
    b1 = new Button("1");
    b2 = new Button("2");
    b3 = new Button("3");
    b4 = new Button("4");
    b5 = new Button("5");
    b6 = new Button("6");
    b7 = new Button("7");
    b8 = new Button("8");
    b9 = new Button("9");
    b0 = new Button("0");
    bAdd = new Button("+");
    bSub = new Button("-");
    bMul = new Button("*");
    bDiv = new Button("/");
    bEq = new Button("=");
    bClr = new Button("C");

    // Create the text field and assign it a size
    tf = new TextField(10);

    // Create the label and assign it a text
    l = new Label("Calculator");

    // Add the components to the applet
    add(l);
    add(tf);
    add(b1);
    add(b2);
    add(b3);
    add(bAdd);
    add(b4);
    add(b5);
    add(b6);
    add(bSub);
    add(b7);
    add(b8);
    add(b9);
    add(bMul);
    add(bClr);
    add(b0);
    add(bEq);
    add(bDiv);

    // Add the action listener to each button
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
    b4.addActionListener(this);
    b5.addActionListener(this);
    b6.addActionListener(this);
    b7.addActionListener(this);
    b8.addActionListener(this);
    b9.addActionListener(this);
    b0.addActionListener(this);
    bAdd.addActionListener(this);
    bSub.addActionListener(this);
    bMul.addActionListener(this);
    bDiv.addActionListener(this);
    bEq.addActionListener(this);
    bClr.addActionListener(this);
  }

  // Override the actionPerformed() method to handle the button clicks and

```
