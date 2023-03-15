#### AWT controls

Here is an example of a simple Java program that uses AWT controls to create a GUI with a button and a label:

```java
import java.awt.*;
import java.awt.event.*;

public class AWTExample extends Frame implements ActionListener {
    Label label;
    Button button;

    public AWTExample() {
        setLayout(new FlowLayout());

        label = new Label("Click the button!");
        add(label);

        button = new Button("Click me");
        add(button);
        button.addActionListener(this);

        setTitle("AWT Example");
        setSize(250, 100);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        label.setText("Button clicked!");
    }

    public static void main(String[] args) {
        new AWTExample();
    }
}
```

This code creates a window with a label and a button. When the button is clicked, the text of the label changes to "Button clicked!".