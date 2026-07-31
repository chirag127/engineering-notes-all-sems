### Creating a JavaBeans for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- JavaBeans is a technology developed by Sun Microsystems and released in 1996, as part of JDK 1.1.
- JavaBeans are classes that encapsulate one or more objects into a single standardized object (the bean).
- JavaBeans are reusable software components that can be easily developed and assembled to create sophisticated applications.
- JavaBeans have the following features :
  - Properties: attributes that define the state or appearance of a bean.
  - Methods: operations that a bean can perform or that can be invoked by other beans or applications.
  - Events: notifications that a bean can send or receive when something of interest happens.
  - Persistence: the ability to save and restore the state of a bean to and from a persistent storage.
- To create a JavaBeans class, the following conventions must be followed :
  - The class must have a public default constructor (no-argument constructor).
  - The class must implement the Serializable interface to enable persistence.
  - The class must follow the Java naming conventions for properties, methods and events.
  - The class must provide public getter and setter methods for accessing its properties.
  - The class must support event listeners and event sources for handling events.
- An example of a JavaBeans class is:

```java
import java.io.Serializable;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;

public class StudentBean implements Serializable {

  // A property to store the name of the student
  private String name;

  // A property to store the age of the student
  private int age;

  // A property change support object to handle property change events
  private PropertyChangeSupport pcs;

  // A public default constructor
  public StudentBean() {
    name = "";
    age = 0;
    pcs = new PropertyChangeSupport(this);
  }

  // A public getter method for the name property
  public String getName() {
    return name;
  }

  // A public setter method for the name property
  public void setName(String name) {
    // Get the old value of the name property
    String oldName = this.name;
    // Set the new value of the name property
    this.name = name;
    // Fire a property change event to notify the listeners
    pcs.firePropertyChange("name", oldName, name);
  }

  // A public getter method for the age property
  public int getAge() {
    return age;
  }

  // A public setter method for the age property
  public void setAge(int age) {
    // Get the old value of the age property
    int oldAge = this.age;
    // Set the new value of the age property
    this.age = age;
    // Fire a property change event to notify the listeners
    pcs.firePropertyChange("age", oldAge, age);
  }

  // A public method to add a property change listener
  public void addPropertyChangeListener(PropertyChangeListener listener) {
    pcs.addPropertyChangeListener(listener);
  }

  // A public method to remove a property change listener
  public void removePropertyChangeListener(PropertyChangeListener listener) {
    pcs.removePropertyChangeListener(listener);
  }
}
```