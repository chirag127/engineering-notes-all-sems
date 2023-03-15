### JavaBeans Properties

- A JavaBean property is a named attribute that can be accessed by the user of the object  .
- The attribute can be of any Java data type, including the classes that you define  .
- A JavaBean property may be read, write, read only, or write only  .
- A JavaBean property can be accessed by using getter and setter methods that follow a naming convention  .
- A getter method is a public instance method that takes no arguments and returns the value of the property  .
- A setter method is a public instance method that takes one argument of the same type as the property and returns void  .
- The name of the getter method must start with "get" followed by the capitalized name of the property, unless the property is a boolean, in which case it may start with "is" instead  .
- The name of the setter method must start with "set" followed by the capitalized name of the property  .
- For example, a JavaBean property named "color" of type String would have the following getter and setter methods:

```java
public String getColor() {
  return color;
}

public void setColor(String color) {
  this.color = color;
}
```

- A JavaBean property can be bound or constrained .
- A bound property is one that notifies other objects when its value changes .
- A constrained property is one that allows other objects to veto its value change .
- To implement a bound or constrained property, a JavaBean must register and notify property change listeners and vetoable change listeners .
- The java.beans package provides classes and interfaces to support bound and constrained properties, such as PropertyChangeSupport, VetoableChangeSupport, PropertyChangeListener, and VetoableChangeListener .
- For example, a JavaBean property named "temperature" of type int that is bound and constrained would have the following code:

```java
import java.beans.*;

public class Thermometer {

  private int temperature;
  private PropertyChangeSupport pcs;
  private VetoableChangeSupport vcs;

  public Thermometer() {
    temperature = 0;
    pcs = new PropertyChangeSupport(this);
    vcs = new VetoableChangeSupport(this);
  }

  public int getTemperature() {
    return temperature;
  }

  public void setTemperature(int temperature) throws PropertyVetoException {
    int oldTemperature = this.temperature;
    vcs.fireVetoableChange("temperature", oldTemperature, temperature);
    this.temperature = temperature;
    pcs.firePropertyChange("temperature", oldTemperature, temperature);
  }

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

- A JavaBean property can also be customized by using a BeanInfo class that provides additional information about the property, such as its display name, description, editor, or hidden status .
- A BeanInfo class is a public class that implements the BeanInfo interface and follows a naming convention of appending "BeanInfo" to the name of the JavaBean class .
- A BeanInfo class can also provide information about the JavaBean's methods, events, icons, and customizers .
- For example, a BeanInfo class for the Thermometer class would look like this:

```java
import java.beans.*;

public class ThermometerBeanInfo implements BeanInfo {

  public PropertyDescriptor[] getPropertyDescriptors() {
    try {
      PropertyDescriptor temperature = new PropertyDescriptor("temperature", Thermometer.class);
      temperature.setDisplayName("Temperature");
      temperature.setShort