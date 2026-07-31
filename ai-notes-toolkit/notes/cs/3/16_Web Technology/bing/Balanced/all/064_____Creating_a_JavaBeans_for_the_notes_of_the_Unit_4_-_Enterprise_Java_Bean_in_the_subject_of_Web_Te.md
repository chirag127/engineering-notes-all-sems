# Creating a JavaBeans for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- JavaBeans are reusable software components that can be manipulated visually in a builder tool.
- JavaBeans follow a set of conventions for defining properties, methods, and events.
- JavaBeans can be used to create graphical user interfaces, web applications, and distributed systems .
- To create a JavaBeans component, you need to follow these steps :
  - Define a public class that implements the java.io.Serializable interface.
  - Provide a public no-argument constructor for the class.
  - Provide public getter and setter methods for the properties of the class, following the naming convention of getPropertyName and setPropertyName.
  - Provide public methods for the events that the class can fire, following the naming convention of addEventListener and removeEventListener.
  - Optionally, provide a BeanInfo class that implements the java.beans.BeanInfo interface, to customize the appearance and behavior of the component in a builder tool.
- To use a JavaBeans component, you need to follow these steps :
  - Import the component class and any other classes that it depends on.
  - Create an instance of the component class using the no-argument constructor or a builder tool.
  - Set the properties of the component using the setter methods or a builder tool.
  - Register event listeners for the component using the addEventListener methods or a builder tool.
  - Invoke the methods of the component as needed.
- An example of a JavaBeans component is a button that has a text property, a background color property, and a click event. The code for the button class could look something like this:

```java
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JButton;

public class ButtonBean extends JButton implements Serializable {

  // A property for the text of the button
  private String text;

  // A property for the background color of the button
  private Color backgroundColor;

  // A list of event listeners for the click event
  private List<ActionListener> actionListeners;

  // A public no-argument constructor
  public ButtonBean() {
    super();
    text = "Click me";
    backgroundColor = Color.WHITE;
    actionListeners = new ArrayList<>();
  }

  // A public getter method for the text property
  public String getText() {
    return text;
  }

  // A public setter method for the text property
  public void setText(String text) {
    this.text = text;
    super.setText(text); // Call the superclass method to update the button
  }

  // A public getter method for the background color property
  public Color getBackgroundColor() {
    return backgroundColor;
  }

  // A public setter method for the background color property
  public void setBackgroundColor(Color backgroundColor) {
    this.backgroundColor = backgroundColor;
    super.setBackground(backgroundColor); // Call the superclass method to update the button
  }

  // A public method for adding an event listener for the click event
  public void addActionListener(ActionListener listener) {
    actionListeners.add(listener);
  }

  // A public method for removing an event listener for the click event
  public void removeActionListener(ActionListener listener) {
    actionListeners.remove(listener);
  }

  // A protected method for firing the click event
  protected void fireActionPerformed(ActionEvent event) {
    for (ActionListener listener : actionListeners) {
      listener.actionPerformed(event); // Call the listener's method to handle the event
    }
  }

  // Override the superclass method to fire the click event when the button is pressed
  @Override
  public void doClick() {
    super.doClick();
    fireActionPerformed(new ActionEvent(this, ActionEvent.ACTION_PERFORMED, text));
  }
}
```

- To use the button component in a web application, you could write something like this:

```java
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ButtonServlet extends HttpServlet {

  // A button component instance
  private ButtonBean button;

  // Initialize the button component in the servlet constructor
  public ButtonServlet() {
    super();
    button = new ButtonBean();
    button.setText("Submit");
    button.setBackgroundColor(Color.GREEN);
    button.addActionListener(new ActionListener() {
      @Override

```
