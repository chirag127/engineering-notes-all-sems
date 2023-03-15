# Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

### Write a Java applet to display the Application Program screen i.e. calculator and other

An applet is a small Java program that can be embedded in a web page. It runs inside the web browser and works at the client-side. An applet can be used to create a calculator or other application program screens.

Here are the steps to create a calculator applet:

1. **Create a new Java class** that extends the `Applet` class. This class will contain the code for the calculator applet.

```java
import java.applet.Applet;
import java.awt.*;

public class CalculatorApplet extends Applet {
    // code for the calculator applet
}
```

2. **Add the necessary components** to the applet, such as text fields for displaying the input and output, and buttons for the calculator operations. These components can be added using the `add()` method of the `Applet` class.

```java
public class CalculatorApplet extends Applet {
    TextField inputField;
    TextField outputField;
    Button addButton;
    Button subtractButton;
    // ...

    public void init() {
        inputField = new TextField();
        outputField = new TextField();
        addButton = new Button("+");
        subtractButton = new Button("-");
        // ...

        add(inputField);
        add(outputField);
        add(addButton);
        add(subtractButton);
        // ...
    }
}
```

3. **Add event listeners** to the buttons to perform the calculator operations when the buttons are clicked. This can be done by implementing the `ActionListener` interface and adding the listener to the buttons using the `addActionListener()` method.

```java
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class CalculatorApplet extends Applet implements ActionListener {
    // ...

    public void init() {
        // ...

        addButton.addActionListener(this);
        subtractButton.addActionListener(this);
        // ...
    }

    public void actionPerformed(ActionEvent e) {
        // code to perform the calculator operations
    }
}
```

4. **Write the code** to perform the calculator operations in the `actionPerformed()` method. This method is called when a button is clicked, and the `ActionEvent` object passed to the method contains information about which button was clicked.

```java
public void actionPerformed(ActionEvent e) {
    String input = inputField.getText();
    double result = 0;

    if (e.getSource() == addButton) {
        // code to perform addition
    } else if (e.getSource() == subtractButton) {
        // code to perform subtraction
    }
    // ...

    outputField.setText(Double.toString(result));
}
```

5. **Embed the applet** in a web page by adding the `<applet>` tag to the HTML code. The `code` attribute of the `<applet>` tag should specify the name of the applet class, and the `width` and `height` attributes should specify the size of the applet.

```html
<applet code="CalculatorApplet.class" width="300" height="200">
</applet>
```

After completing these steps, the calculator applet will be displayed on the web page and can be used to perform calculations. Similarly, other application program screens can be created using applets.