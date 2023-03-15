#### Event handling in Core Java
Event handling in Core Java involves three main components: the event source, the event object, and the event listener. The event source is the object on which the event occurs. The event object contains information about the event, such as its type and the state of the source object. The event listener is an object that receives the event and provides a response.

Here is an example of how to handle a button click event in Core Java:

```java
import java.awt.*;
import java.awt.event.*;

public class ButtonClickExample extends Frame implements ActionListener {
    ButtonClickExample() {
        Button b = new Button("Click me!");
        b.setBounds(50, 100, 80, 30);
        add(b);
        b.addActionListener(this);
        setSize(300, 300);
        setLayout(null);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        System.out.println("Button clicked!");
    }

    public static void main(String[] args) {
        new ButtonClickExample();
    }
}
```

In this example, the `ButtonClickExample` class extends `Frame` and implements the `ActionListener` interface. The `ActionListener` interface requires the implementation of the `actionPerformed` method, which is called when an action event occurs. In this case, the action event is a button click. The `actionPerformed` method prints a message to the console when the button is clicked.

The `ButtonClickExample` constructor creates a `Button` object and sets its properties. The `addActionListener` method is called on the button object and `this` is passed as an argument, indicating that the `ButtonClickExample` object is the event listener for the button click event. The `setSize`, `setLayout`, and `setVisible` methods are called to set the size, layout, and visibility of the frame.

The `main` method creates an instance of the `ButtonClickExample` class, which displays the frame and the button. When the button is clicked, the `actionPerformed` method is called and the message is printed to the console.