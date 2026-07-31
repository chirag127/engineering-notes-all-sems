### Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

1. An applet is a Java program that runs in a web browser.
2. Applets are used to create interactive features on web pages, such as calculators, games, and other graphical user interfaces.
3. To create an applet, you need to write a Java class that extends the `java.applet.Applet` class.
4. The `init()` method is called when the applet is first loaded and is used to initialize the applet.
5. The `paint()` method is called whenever the applet needs to be redrawn and is used to draw the applet's user interface.
6. To create a calculator applet, you can use the `java.awt` package to create a graphical user interface with buttons, text fields, and other components.
7. You can add event listeners to the buttons to perform calculations when the buttons are clicked.
8. You can also use the `java.awt` package to create other types of application program screens, such as text editors, image viewers, and more.

Here is an example of a simple calculator applet:

```java
import java.applet.Applet;
import java.awt.Button;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculatorApplet extends Applet implements ActionListener {
    TextField display;
    Button button1, button2, button3, button4, button5, button6, button7, button8, button9, button0;
    Button buttonAdd, buttonSubtract, buttonMultiply, buttonDivide, buttonEquals, buttonClear;

    public void init() {
        display = new TextField(20);
        add(display);

        button1 = new Button("1");
        button1.addActionListener(this);
        add(button1);

        button2 = new Button("2");
        button2.addActionListener(this);
        add(button2);

        button3 = new Button("3");
        button3.addActionListener(this);
        add(button3);

        button4 = new Button("4");
        button4.addActionListener(this);
        add(button4);

        button5 = new Button("5");
        button5.addActionListener(this);
        add(button5);

        button6 = new Button("6");
        button6.addActionListener(this);
        add(button6);

        button7 = new Button("7");
        button7.addActionListener(this);
        add(button7);

        button8 = new Button("8");
        button8.addActionListener(this);
        add(button8);

        button9 = new Button("9");
        button9.addActionListener(this);
        add(button9);

        button0 = new Button("0");
        button0.addActionListener(this);
        add(button0);

        buttonAdd = new Button("+");
        buttonAdd.addActionListener(this);
        add(buttonAdd);

        buttonSubtract = new Button("-");
        buttonSubtract.addActionListener(this);
        add(buttonSubtract);

        buttonMultiply = new Button("*");
        buttonMultiply.addActionListener(this);
        add(buttonMultiply);

        buttonDivide = new Button("/");
        buttonDivide.addActionListener(this);
        add(buttonDivide);

        buttonEquals = new Button("=");
        buttonEquals.addActionListener(this);
        add(buttonEquals);

        buttonClear = new Button("C");
        buttonClear.addActionListener(this);
        add(buttonClear);
    }

    public void actionPerformed(ActionEvent e) {
        // handle button clicks here
    }
}
```

This code creates a calculator applet with a display and buttons for the digits 0-9 and the basic arithmetic operations. You can add additional code to the `actionPerformed()` method to perform calculations when the buttons are clicked. You can also modify the code to create other types of application program screens.