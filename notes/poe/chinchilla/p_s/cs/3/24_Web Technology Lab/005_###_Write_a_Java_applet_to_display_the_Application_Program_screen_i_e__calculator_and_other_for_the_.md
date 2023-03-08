### Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab.

Java applets are small programs that are executed within a web browser. They are a great way to add interactivity to websites and can be used to create applications such as calculators. In this unit, we will learn how to develop Java programs for window/web-based applications, and one of the examples we will cover is how to create a Java applet to display an application program screen, specifically a calculator.

To create a Java applet, we will need to follow these steps:

1. Create a new Java class that extends the Applet class.
2. Declare any variables that we will need for our calculator, such as the numbers and operations that will be used.
3. Override the init() method to initialize our calculator and add any necessary components.
4. Override the paint() method to draw the calculator screen.
5. Add any necessary event listeners to handle user input.

Here's an example of what our Java applet code might look like:

```java
import java.awt.*;
import java.awt.event.*;
import java.applet.*;

public class Calculator extends Applet implements ActionListener {
    private TextField display;
    private Button[] buttons;
    private String[] buttonLabels = {"7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "=", "+"};
    private double num1, num2, result;
    private char operator;

    public void init() {
        display = new TextField("0");
        display.setEditable(false);
        add(display);

        buttons = new Button[buttonLabels.length];
        for (int i = 0; i < buttonLabels.length; i++) {
            buttons[i] = new Button(buttonLabels[i]);
            buttons[i].addActionListener(this);
            add(buttons[i]);
        }
    }

    public void actionPerformed(ActionEvent e) {
        String label = e.getActionCommand();
        switch (label) {
            case "+":
            case "-":
            case "*":
            case "/":
                num1 = Double.parseDouble(display.getText());
                operator = label.charAt(0);
                display.setText("");
                break;
            case ".":
                if (display.getText().indexOf(".") == -1) {
                    display.setText(display.getText() + label);
                }
                break;
            case "=":
                num2 = Double.parseDouble(display.getText());
                switch (operator) {
                    case '+':
                        result = num1 + num2;
                        break;
                    case '-':
                        result = num1 - num2;
                        break;
                    case '*':
                        result = num1 * num2;
                        break;
                    case '/':
                        result = num1 / num2;
                        break;
                }
                display.setText("" + result);
                break;
            default:
                display.setText(display.getText() + label);
                break;
        }
    }

    public void paint(Graphics g) {
        int x = 10;
        int y = 50;
        int width = 30;
        int height = 30;
        for (int i = 0; i < buttonLabels.length; i++) {
            if (i == 3 || i == 7 || i == 11 || i == 14) {
                x += 40;
                y = 50;
            }
            buttons[i].setBounds(x, y, width, height);
            y += 40;
        }
    }
}
```

This code creates a calculator applet with buttons for the numbers, decimal point, and operators (+, -, *, /). When the user clicks a button, the actionPerformed() method is called and the appropriate action is performed. The paint() method is used to draw the calculator screen, and the init() method is used to set up the calculator and add the necessary components.

In conclusion, creating a Java applet to display an application program screen such as a calculator requires knowledge of Java programming and familiarity with the Applet class. By following the steps outlined above and using the example code provided, you should be able to create your own calculator applet and gain a better understanding of how Java applets work.