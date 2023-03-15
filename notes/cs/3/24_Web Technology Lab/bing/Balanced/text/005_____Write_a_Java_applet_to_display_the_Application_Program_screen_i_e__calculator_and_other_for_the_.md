### Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

- A Java applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly .
- A Java applet can be used to create a calculator program that can perform basic arithmetic operations such as addition, subtraction, multiplication and division  .
- To create a Java applet for a calculator program, the following steps are required:

  - Import the necessary packages such as `java.applet`, `java.awt` and `java.awt.event`  .
  - Define a class that extends the `Applet` class and implements the `ActionListener` interface  .
  - Declare the components such as text fields, buttons and labels as instance variables of the class  .
  - Initialize the components in the `init()` method of the applet and add them to the applet layout  .
  - Register the action listeners for the buttons in the `init()` method  .
  - Define the `actionPerformed()` method to handle the button clicks and perform the arithmetic operations  .
  - Override the `paint()` method to display the applet title and other information  .
  - Compile and run the applet using an applet viewer or a web browser  .

- A sample code for a Java applet calculator program is given below:

```java
// Import the necessary packages
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

// Define a class that extends the Applet class and implements the ActionListener interface
public class CalculatorApplet extends Applet implements ActionListener {

  // Declare the components as instance variables
  TextField tf1, tf2, tf3; // Text fields for input and output
  Button b1, b2, b3, b4; // Buttons for arithmetic operations
  Label l1, l2, l3; // Labels for instructions

  // Initialize the components in the init() method
  public void init() {
    // Set the applet layout to grid layout with 4 rows and 2 columns
    setLayout(new GridLayout(4, 2));

    // Create the components
    tf1 = new TextField(10); // Text field for the first operand
    tf2 = new TextField(10); // Text field for the second operand
    tf3 = new TextField(10); // Text field for the result
    tf3.setEditable(false); // Make the result text field read-only
    b1 = new Button("+"); // Button for addition
    b2 = new Button("-"); // Button for subtraction
    b3 = new Button("*"); // Button for multiplication
    b4 = new Button("/"); // Button for division
    l1 = new Label("Enter the first number:"); // Label for the first operand
    l2 = new Label("Enter the second number:"); // Label for the second operand
    l3 = new Label("Result:"); // Label for the result

    // Add the components to the applet layout
    add(l1); // Add the first label to the first row and first column
    add(tf1); // Add the first text field to the first row and second column
    add(l2); // Add the second label to the second row and first column
    add(tf2); // Add the second text field to the second row and second column
    add(l3); // Add the third label to the third row and first column
    add(tf3); // Add the third text field to the third row and second column
    add(b1); // Add the first button to the fourth row and first column
    add(b2); // Add the second button to the fourth row and second column
    add(b3); // Add the third button to the fifth row and first column
    add(b4); // Add the fourth