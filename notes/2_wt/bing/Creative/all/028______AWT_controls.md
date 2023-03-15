#### AWT controls

AWT controls are components that allow a user to interact with your application in various ways. AWT stands for Abstract Window Toolkit, which is a set of APIs for creating graphical user interfaces (GUIs) in Java. AWT controls are also called AWT components or AWT widgets .

Some of the features of AWT controls are:

- They are platform-dependent, meaning they use the resources and look-and-feel of the underlying operating system (OS) .
- They are heavyweight, meaning they have their own native window and peer object.
- They are contained in the `java.awt` package .
- They can be added to containers such as `Frame`, `Panel`, or `Applet` .
- They can generate events such as `ActionEvent`, `ItemEvent`, or `TextEvent` when the user interacts with them .

Some of the commonly used AWT controls are :

- `Label`: A component for displaying text in a container.
- `Button`: A component for triggering an action when clicked.
- `Checkbox`: A component for selecting or deselecting an option.
- `Choice`: A component for selecting one option from a drop-down list.
- `List`: A component for displaying and selecting multiple items from a scrollable list.
- `Scrollbar`: A component for adjusting a value within a range by dragging a thumb.
- `TextField`: A component for entering and editing a single line of text.
- `TextArea`: A component for entering and editing multiple lines of text.

Each AWT control has its own constructor, methods, and properties that can be used to create and manipulate it. For example, to create a label with the text "Hello World", you can use the following code:

```java
Label label = new Label("Hello World");
```

To add the label to a frame, you can use the `add()` method of the frame:

```java
Frame frame = new Frame("AWT Example");
frame.add(label);
```

To set the font of the label, you can use the `setFont()` method of the label:

```java
Font font = new Font("Arial", Font.BOLD, 20);
label.setFont(font);
```

To learn more about AWT controls, you can refer to the following sources:

: https://www.educba.com/awt-controls-in-java/
: https://dotnettutorials.net/lesson/awt-controls-in-java/
: https://www.brainkart.com/article/AWT-Control-Fundamentals_10656/
: https://www.javatpoint.com/java-awt
: https://docs.oracle.com/javase/7/docs/api/java/awt/package-summary.html
: https://www.tutorialspoint.com/awt/awt_controls.htm