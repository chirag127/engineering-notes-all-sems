# Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

- A Java applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly .
- A Java applet program for a calculator can use a grid layout to arrange buttons for the digits and for the addition, subtraction, multiplication, and division operations.
- A Java applet program for a calculator can also use a text field to display the first and second numbers and the result.
- A Java applet program for a calculator can add an action listener to each button to perform the corresponding arithmetic operation.
- A Java applet program for a calculator can use the `java.applet.Applet` class and the `java.awt` package to create the user interface and handle the events   .
- A Java applet program for a calculator can be compiled and run using the `appletviewer` tool or a web browser that supports Java .

- Here is an example of a Java applet program for a calculator:

```java
// Import the necessary packages
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

// Define the applet class
public class Calculator extends Applet implements ActionListener {
  // Declare the components
  TextField tf1, tf2, tf3;
  Button b1, b2, b3, b4;
  Label l1, l2, l3, l4;

  // Initialize the components
  public void init() {
    // Create the components
    tf1 = new TextField();
    tf2 = new TextField();
    tf3 = new TextField();
    b1 = new Button("+");
    b2 = new Button("-");
    b3 = new Button("*");
    b4 = new Button("/");
    l1 = new Label("First Number");
    l2 = new Label("Second Number");
    l3 = new Label("Result");
    l4 = new Label("Calculator");

    // Set the layout
    setLayout(new GridLayout(5, 2));

    // Add the components to the applet
    add(l4);
    add(new Label()); // Empty label for spacing
    add(l1);
    add(tf1);
    add(l2);
    add(tf2);
    add(l3);
    add(tf3);
    add(b1);
    add(b2);
    add(b3);
    add(b4);

    // Add action listeners to the buttons
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
    b4.addActionListener(this);

    // Set the result text field as non-editable
    tf3.setEditable(false);
  }

  // Handle the button clicks
  public void actionPerformed(ActionEvent e) {
    // Get the numbers from the text fields
    int num1 = Integer.parseInt(tf1.getText());
    int num2 = Integer.parseInt(tf2.getText());

    // Get the source of the event
    Object source = e.getSource();

    // Perform the corresponding operation
    if (source == b1) {
      // Addition
      tf3.setText(String.valueOf(num1 + num2));
    } else if (source == b2) {
      // Subtraction
      tf3.setText(String.valueOf(num1 - num2));
    } else if (source == b3) {
      // Multiplication
      tf3.setText(String.valueOf(num1 * num2));
    } else if (source == b4) {
      // Division
      tf3.setText(String.valueOf(num1 / num2));
    }
  }
}
```