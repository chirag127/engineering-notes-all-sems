### Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

1. An applet is a Java program that runs in a web browser.
2. Applets are used to provide interactive features to web applications that cannot be provided by HTML alone.
3. To create a Java applet, you need to define a class that extends the `java.applet.Applet` class.
4. The `init()` method is called when the applet is first loaded and is used to initialize the applet.
5. The `paint()` method is called whenever the applet needs to be redrawn and is used to display the applet's user interface.
6. To create a calculator applet, you can use the `java.awt` package to create a user interface with buttons, text fields, and other components.
7. You can add event listeners to the buttons to perform calculations when the user clicks on them.
8. You can use the `java.lang.Math` class to perform mathematical operations.
9. Here is an example of a simple calculator applet:

```java
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

public class CalculatorApplet extends Applet implements ActionListener {
    TextField display;
    double result = 0;
    String operator = "=";
    boolean calculating = true;

    public void init() {
        setLayout(new BorderLayout());

        display = new TextField("0");
        display.setEditable(false);
        add(display, "North");

        Panel panel = new Panel();
        panel.setLayout(new GridLayout(4, 4));
        String buttonLabels = "789/456*123-0.=+";
        for (int i = 0; i < buttonLabels.length(); i++) {
            Button button = new Button(buttonLabels.substring(i, i + 1));
            panel.add(button);
            button.addActionListener(this);
        }
        add(panel, "Center");
    }

    public void actionPerformed(ActionEvent event) {
        String command = event.getActionCommand();
        if ('0' <= command.charAt(0) && command.charAt(0) <= '9' || command.equals(".")) {
            if (calculating)
                display.setText(command);
            else
                display.setText(display.getText() + command);
            calculating = false;
        } else {
            if (calculating) {
                if (command.equals("-")) {
                    display.setText(command);
                    calculating = false;
                } else
                    operator = command;
            } else {
                double x = Double.parseDouble(display.getText());
                calculate(x);
                operator = command;
                calculating = true;
            }
        }
    }

    private void calculate(double n) {
        if (operator.equals("+"))
            result += n;
        else if (operator.equals("-"))
            result -= n;
        else if (operator.equals("*"))
            result *= n;
        else if (operator.equals("/"))
            result /= n;
        else if (operator.equals("="))
            result = n;
        display.setText("" + result);
    }
}
```

10. This applet creates a calculator with a display at the top and buttons for the digits, operators, and the decimal point.
11. When the user clicks on a button, the `actionPerformed()` method is called and performs the appropriate calculation.
12. You can use this example as a starting point and modify it to create more advanced calculator applets or other types of applets.