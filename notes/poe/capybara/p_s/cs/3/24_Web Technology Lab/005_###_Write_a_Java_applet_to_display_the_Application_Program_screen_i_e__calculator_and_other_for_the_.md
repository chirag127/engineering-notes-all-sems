## Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab.

Java applets are small programs that run within a web browser. They are used to enhance the functionality of a website by providing interactive features, such as games, calculators, and other useful tools. In this section, we will learn how to write a Java applet to display the application program screen, specifically a calculator.

### Steps to write a Java applet for a calculator:

1. First, create a new Java project in your IDE (Integrated Development Environment).
2. Create a new class and name it `CalculatorApplet`.
3. Extend the `Applet` class to inherit its properties and methods.
4. Override the `init()` method to create the calculator interface using the `GridLayout` class.
5. Create buttons for each number and operator using the `Button` class.
6. Add action listeners to each button to perform their respective functions using the `ActionListener` interface.
7. Override the `paint()` method to display the calculator interface on the applet.

Here is an example code snippet for the `CalculatorApplet` class:

```
import java.awt.*;
import java.awt.event.*;
import java.applet.*;

public class CalculatorApplet extends Applet implements ActionListener {
    TextField display = new TextField("", 20);
    Button button0 = new Button("0");
    Button button1 = new Button("1");
    Button button2 = new Button("2");
    Button button3 = new Button("3");
    Button button4 = new Button("4");
    Button button5 = new Button("5");
    Button button6 = new Button("6");
    Button button7 = new Button("7");
    Button button8 = new Button("8");
    Button button9 = new Button("9");
    Button buttonPlus = new Button("+");
    Button buttonMinus = new Button("-");
    Button buttonMultiply = new Button("*");
    Button buttonDivide = new Button("/");
    Button buttonClear = new Button("C");
    Button buttonEquals = new Button("=");

    public void init() {
        setLayout(new BorderLayout());
        add("North", display);

        Panel panel = new Panel();
        panel.setLayout(new GridLayout(4,4));
        panel.add(button1);
        panel.add(button2);
        panel.add(button3);
        panel.add(buttonPlus);
        panel.add(button4);
        panel.add(button5);
        panel.add(button6);
        panel.add(buttonMinus);
        panel.add(button7);
        panel.add(button8);
        panel.add(button9);
        panel.add(buttonMultiply);
        panel.add(buttonClear);
        panel.add(button0);
        panel.add(buttonEquals);
        panel.add(buttonDivide);

        add("Center", panel);

        button1.addActionListener(this);
        button2.addActionListener(this);
        button3.addActionListener(this);
        button4.addActionListener(this);
        button5.addActionListener(this);
        button6.addActionListener(this);
        button7.addActionListener(this);
        button8.addActionListener(this);
        button9.addActionListener(this);
        button0.addActionListener(this);
        buttonPlus.addActionListener(this);
        buttonMinus.addActionListener(this);
        buttonMultiply.addActionListener(this);
        buttonDivide.addActionListener(this);
        buttonClear.addActionListener(this);
        buttonEquals.addActionListener(this);
    }

    public void actionPerformed(ActionEvent event) {
        String action = event.getActionCommand();

        if (action.equals("+")) {
            // perform addition
        } else if (action.equals("-")) {
            // perform subtraction
        } else if (action.equals("*")) {
            // perform multiplication
        } else if (action.equals("/")) {
            // perform division
        } else if (action.equals("C")) {
            // clear the display
        } else if (action.equals("=")) {
            // perform calculation and display result
        } else {
            // append digit to display
        }
    }

    public void paint(Graphics g) {
        // display the calculator interface
    }
}
```

### Advantages of using Java applets:

1. They can be used to create interactive tools and applications that run within a web browser.
2. They are platform-independent, meaning they can be run on any operating system that supports Java.
3. They can be easily integrated into web pages using HTML tags.
4. They can be used to create rich multimedia content, such as games and animations.

### Disadvantages of using Java applets:

1. They require the Java Runtime Environment (JRE) to be installed on the user's machine.
2. They can be slow to load and may impact the performance of the web page.
3. They are not supported on many mobile devices, such as smartphones and tablets.
4. They are not as secure as other web technologies, such as JavaScript.

### Conclusion:

In this section, we learned how to write a Java applet to display the application program screen, specifically a calculator. We also discussed the