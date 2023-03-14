 Here is the content in markdown format for the topic #### Introduction to AWT in Core Java:

#### Introduction to AWT in Core Java

AWT stands for Abstract Window Toolkit. It is a platform-independent interface used to create GUI components in java. AWT components consist of windows, buttons, labels, text fields, etc.

Some key points about AWT:

- AWT components are heavyweight, i.e., they are OS dependent and use more memory.
- AWT has less features as compared to Swing and is not customizable.
- AWT does not support gradients, shadows, etc.
- AWT components are thread-safe, i.e., they are safe to access from multiple threads.
- The java.awt package consists of AWT classes and interfaces.

To create an AWT application:

1. Import the java.awt package
2. Create Frame which is a top-level window
3. Add components to the frame like buttons, labels, text fields, etc.
4. Set the size of the frame
5. Make the frame visible

For example:

```java
import java.awt.*;

public class MyAWTApp {
   public static void main(String[] args) {
      Frame f = new Frame("My AWT App");
      Button b = new Button("Click Me");
      f.add(b);
      f.setSize(300, 300);
      f.setVisible(true);
   }
}
```

Some key AWT components and their uses:

- Frame - Used to create application window
- Button - Used for user input
- Label - Used to display text
- TextField - Used for single line text input
- TextArea - Used for multi-line text input
- Checkbox - Used to select one option from multiple options
- Choice - Used to select one option from multiple options
- List - Used to select multiple options from a list
- Canvas - Used to draw shapes

Advantages:

- Provides basic GUI functionality
- Platform independent
- Thread safe

Disadvantages:

- Heavyweight components
- Limited features
- Not customizable

Applications:

- AWT can be used to create basic GUI applications like calculators, basic text editors, etc.
- AWT forms the base for the Swing API which provides more features.