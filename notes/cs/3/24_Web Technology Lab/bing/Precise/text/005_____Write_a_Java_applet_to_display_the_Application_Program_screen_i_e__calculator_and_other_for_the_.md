### Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

1. An applet is a small program that is designed to run within a web page.
2. To create an applet, you need to extend the `java.applet.Applet` class and override its methods to define the applet's behavior.
3. The `init()` method is called when the applet is first loaded and is used to initialize the applet.
4. The `start()` method is called when the applet becomes visible on the web page and is used to start any animations or other dynamic behavior.
5. The `paint()` method is called whenever the applet needs to be redrawn and is used to draw the applet's content.
6. To display a calculator, you can create a user interface using components such as buttons, text fields, and labels.
7. You can add event listeners to the buttons to handle user input and perform calculations.
8. Here is an example of a simple calculator applet:

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

    public void actionPerformed(ActionEvent evt) {
        String command = evt.getActionCommand();
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