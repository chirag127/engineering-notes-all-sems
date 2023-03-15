#### Introduction to AWT in Core Java

AWT (Abstract Window Toolkit) is a set of APIs used by Java programmers to create graphical user interfaces (GUIs). It is part of the Java Foundation Classes (JFC) and provides a platform-independent way to develop rich, interactive user interfaces for desktop applications.

Here is an example of a simple AWT program that creates a window with a button:

```java
import java.awt.*;
import java.awt.event.*;

public class AWTExample extends Frame implements ActionListener {
    Button b;

    AWTExample() {
        b = new Button("Click me");
        b.setBounds(30, 100, 80, 30);
        add(b);
        setSize(300, 300);
        setLayout(null);
        setVisible(true);
        b.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        System.out.println("Button clicked!");
    }

    public static void main(String[] args) {
        new AWTExample();
    }
}
```

This code creates a window with a button that, when clicked, prints "Button clicked!" to the console. The `AWTExample` class extends the `Frame` class, which represents a window in AWT. The `Button` class is used to create a button, and the `ActionListener` interface is implemented to handle button clicks.