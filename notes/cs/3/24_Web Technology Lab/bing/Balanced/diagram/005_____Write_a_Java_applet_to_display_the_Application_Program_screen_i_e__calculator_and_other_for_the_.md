# Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

- A Java applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly  .
- A Java applet can be used to create a calculator program that can perform basic arithmetic operations such as addition, subtraction, multiplication and division.
- A Java applet can use the `java.awt` and `java.applet` packages to create the graphical user interface (GUI) and the logic of the calculator program.
- A Java applet can use the `Applet` class to define the applet, the `init()` method to initialize the applet, the `paint()` method to draw the applet, and the `actionPerformed()` method to handle the user events  .
- A Java applet can use the `TextField` class to create the input and output fields, the `Button` class to create the buttons, the `GridLayout` class to arrange the components in a grid, and the `ActionListener` interface to register the event listeners  .
- A Java applet can use the `Double.parseDouble()` method to convert the input strings to double values, the `String.valueOf()` method to convert the double values to output strings, and the `switch` statement to perform the arithmetic operations based on the selected operator  .
- A Java applet can use the `repaint()` method to update the applet display after each operation  .

- A possible example of a Java applet program for a calculator is as follows:

```java
// import the necessary packages
import java.awt.*;
import java.applet.*;
import java.awt.event.*;

// define the applet class
public class Calculator extends Applet implements ActionListener {
  // declare the components
  TextField input1, input2, output;
  Button add, subtract, multiply, divide, clear;
  double num1, num2, result;
  char op;

  // initialize the applet
  public void init() {
    // create the components
    input1 = new TextField(10);
    input2 = new TextField(10);
    output = new TextField(10);
    add = new Button("+");
    subtract = new Button("-");
    multiply = new Button("*");
    divide = new Button("/");
    clear = new Button("C");

    // add the components to the applet
    add(input1);
    add(input2);
    add(output);
    add(add);
    add(subtract);
    add(multiply);
    add(divide);
    add(clear);

    // set the layout of the applet
    setLayout(new GridLayout(4, 2));

    // register the event listeners
    add.addActionListener(this);
    subtract.addActionListener(this);
    multiply.addActionListener(this);
    divide.addActionListener(this);
    clear.addActionListener(this);
  }

  // draw the applet
  public void paint(Graphics g) {
    // set the font and color of the applet
    g.setFont(new Font("Arial", Font.BOLD, 20));
    g.setColor(Color.blue);

    // draw the title of the applet
    g.drawString("Calculator Applet", 50, 20);
  }

  // handle the user events
  public void actionPerformed(ActionEvent e) {
    // get the source of the event
    Object source = e.getSource();

    // if the source is the clear button, clear the input and output fields
    if (source == clear) {
      input1.setText("");
      input2.setText("");
      output.setText("");
    }
    // else, get the input values and the selected operator
    else {
      num1 = Double.parseDouble(input1.getText());
      num2 = Double.parseDouble(input2.getText());

      if (source == add) {
        op = '+';
      } else if (source == subtract) {
        op = '-';
      } else if (source == multiply) {
        op = '*';
      } else if (source == divide) {
        op = '/';
      }

      // perform the arithmetic operation based on the operator
      switch (op) {
        case '+':
          result = num1 + num2;
          break;
        case '-':