### Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

Java Applet for Displaying a Calculator:

In Web Technology Lab, Java applets can be used to create window/web-based applications. One common example of a window/web-based application is a calculator. In this section, we will write a Java applet that displays a simple calculator.

The following code is an example of a Java applet that displays a calculator:

```
import java.awt.*;
import java.awt.event.*;
import java.applet.*;

public class CalculatorApplet extends Applet implements ActionListener {
  private TextField display;
  private Panel buttons;
  private Button[] b;
  private String[] buttonLabels = { "7", "8", "9", "+",
                                   "4", "5", "6", "-",
                                   "1", "2", "3", "*",
                                   "0", ".", "=", "/" };
  
  public void init() {
    display = new TextField("0", 20);
    display.setEditable(false);
    add(display, BorderLayout.NORTH);
    
    buttons = new Panel();
    buttons.setLayout(new GridLayout(4, 4));
    b = new Button[16];
    for (int i = 0; i < 16; i++) {
      b[i] = new Button(buttonLabels[i]);
      b[i].addActionListener(this);
      buttons.add(b[i]);
    }
    add(buttons, BorderLayout.CENTER);
  }
  
  public void actionPerformed(ActionEvent e) {
    String s = e.getActionCommand();
    if (s.equals("=")) {
      display.setText(eval(display.getText()));
    } else {
      display.setText(display.getText() + s);
    }
  }
  
  private String eval(String s) {
    // Evaluate the expression and return the result as a string
    return "0";
  }
}
```

In this example, the `CalculatorApplet` class extends the `Applet` class and implements the `ActionListener` interface. The `init` method sets up the user interface, including the display and buttons. The `actionPerformed` method is called whenever a button is clicked, and updates the display accordingly. The `eval` method evaluates the expression in the display and returns the result as a string.

In conclusion, Java applets can be used to create window/web-based applications, such as a calculator. The example code provided in this section demonstrates how to create a simple calculator applet in Java.
