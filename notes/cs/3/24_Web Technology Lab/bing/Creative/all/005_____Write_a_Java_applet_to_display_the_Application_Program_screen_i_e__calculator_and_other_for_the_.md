# Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

- A Java applet is a small Java application that can be embedded in a web browser and run on the client-side.
- A Java applet can display dynamic content, such as a calculator, using graphical user interface (GUI) components and event handling.
- To write a Java applet for a calculator, we need to follow these steps:

  - Import the necessary packages, such as `java.applet`, `java.awt`, and `java.awt.event`.
  - Define a class that extends the `Applet` class and implements the `ActionListener` interface.
  - Declare and initialize the GUI components, such as text fields, buttons, and labels, as instance variables of the class.
  - Override the `init()` method of the `Applet` class to add the GUI components to the applet and register the action listeners for the buttons.
  - Override the `actionPerformed()` method of the `ActionListener` interface to perform the arithmetic operations based on the button clicked and the input values entered in the text fields.
  - Compile and run the applet using an applet viewer or a web browser.

- Here is an example of a Java applet for a simple calculator that can perform addition, subtraction, multiplication, and division:

```java
// Import the necessary packages
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

// Define a class that extends the Applet class and implements the ActionListener interface
public class CalculatorApplet extends Applet implements ActionListener {

  // Declare and initialize the GUI components as instance variables of the class
  TextField tf1, tf2, tf3; // Text fields for input and output
  Button b1, b2, b3, b4; // Buttons for arithmetic operations
  Label l1, l2, l3; // Labels for instructions

  // Override the init() method of the Applet class to add the GUI components to the applet and register the action listeners for the buttons
  public void init() {
    // Set the layout of the applet to grid layout with 4 rows and 2 columns
    setLayout(new GridLayout(4, 2));

    // Create and initialize the GUI components
    tf1 = new TextField(10); // Text field for the first input value
    tf2 = new TextField(10); // Text field for the second input value
    tf3 = new TextField(10); // Text field for the output value
    tf3.setEditable(false); // Make the output text field non-editable
    b1 = new Button("+"); // Button for addition
    b2 = new Button("-"); // Button for subtraction
    b3 = new Button("*"); // Button for multiplication
    b4 = new Button("/"); // Button for division
    l1 = new Label("Enter the first number:"); // Label for the first input value
    l2 = new Label("Enter the second number:"); // Label for the second input value
    l3 = new Label("Result:"); // Label for the output value

    // Add the GUI components to the applet
    add(l1); // Add the label for the first input value to the first row and first column
    add(tf1); // Add the text field for the first input value to the first row and second column
    add(l2); // Add the label for the second input value to the second row and first column
    add(tf2); // Add the text field for the second input value to the second row and second column
    add(l3); // Add the label for the output value to the third row and first column
    add(tf3); // Add the text field for the output value to the third row and second column
    add(b1); // Add the button for addition to the fourth row and first column
    add(b2); // Add the button for subtraction to the fourth row and second column
    add(b3); // Add the button for multiplication to the fifth row and first column
    add(b4); // Add the button for division to the fifth row and second column

    // Register the action listeners for the buttons
    b1.addActionListener(this); // Register the action listener for the addition button
    b2.addActionListener(this); // Register the action listener for the subtraction button
    b3.addActionListener(this); //