### JavaBeans Properties

- JavaBeans properties are attributes of a Java class that can be accessed by other classes or tools using a standard convention.
- A property can be of any Java data type, such as int, String, boolean, or an object of another class.
- A property can be read-only, write-only, or read-write, depending on the availability of getter and setter methods.
- A getter method is a public instance method that returns the value of a property. It follows the naming convention of `getPropertyName` or `isPropertyName` for boolean properties.
- A setter method is a public instance method that takes a single parameter and assigns it to a property. It follows the naming convention of `setPropertyName`.
- For example, a Java class that represents a person may have the following properties and methods:

```java
public class Person {
  // properties
  private String name;
  private int age;
  private boolean married;

  // getter and setter methods
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }

  public boolean isMarried() {
    return married;
  }

  public void setMarried(boolean married) {
    this.married = married;
  }
}
```

- In this example, the `name`, `age`, and `married` properties are read-write, as they have both getter and setter methods.
- A JavaBeans property can also be bound or constrained, meaning that it can notify other classes or components when its value changes, or it can allow other classes or components to veto its value change.
- To implement bound or constrained properties, a Java class must follow these steps:
  - Implement the `java.beans.PropertyChangeSupport` class to manage a list of listeners that are interested in the property changes.
  - Implement the `java.beans.PropertyChangeListener` interface to define a method that handles the property change events.
  - Implement the `java.beans.VetoableChangeSupport` class to manage a list of listeners that can veto the property changes.
  - Implement the `java.beans.VetoableChangeListener` interface to define a method that can veto the property change events.
  - Add or remove listeners using the `addPropertyChangeListener`, `removePropertyChangeListener`, `addVetoableChangeListener`, and `removeVetoableChangeListener` methods of the support classes.
  - Fire property change events using the `firePropertyChange` method of the support classes.
  - Catch and handle the `java.beans.PropertyVetoException` that may be thrown by the vetoable listeners.
- For example, a Java class that represents a bank account may have the following bound and constrained properties and methods:

```java
import java.beans.*;

public class BankAccount {
  // properties
  private String owner;
  private double balance;

  // support classes for bound and constrained properties
  private PropertyChangeSupport pcs;
  private VetoableChangeSupport vcs;

  // constructor
  public BankAccount(String owner, double balance) {
    this.owner = owner;
    this.balance = balance;
    this.pcs = new PropertyChangeSupport(this);
    this.vcs = new VetoableChangeSupport(this);
  }

  // getter and setter methods
  public String getOwner() {
    return owner;
  }

  public void setOwner(String owner) {
    this.owner = owner;
  }

  public double getBalance() {
    return balance;
  }

  public void setBalance(double balance) throws PropertyVetoException {
    // get the old value of the balance property
    double oldBalance = this.balance;
    // fire a vetoable change event and check if any listener vetoes the change
    vcs.fireVetoableChange("balance", oldBalance, balance);
    // if no veto, set the new value of the balance property
    this.balance = balance;
    // fire a property change event and notify the listeners
    pcs.firePropertyChange("balance", oldBalance, balance);
  }

  // methods to add or remove listeners
  public void addPropertyChangeListener(PropertyChangeListener listener) {
    pcs.addPropertyChangeListener(listener);
  }

  public void removePropertyChangeListener(PropertyChangeListener listener) {
    pcs.removePropertyChangeListener(listener);
  }

  public void addVetoableChangeListener(VetoableChangeListener listener) {
    vcs.addVetoableChangeListener(listener);
  }

  public void removeVetoableChangeListener(VetoableChangeListener listener) {
    vcs.removeVetoableChangeListener(listener);
  }
}
```

- In this example, the `balance` property is bound and constrained, as it