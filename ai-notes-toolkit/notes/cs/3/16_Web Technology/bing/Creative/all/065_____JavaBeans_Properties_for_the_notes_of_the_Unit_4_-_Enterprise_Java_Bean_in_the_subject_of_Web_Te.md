# JavaBeans Properties

- A JavaBean property is a named attribute that can be accessed by the user of the object  .
- The attribute can be of any Java data type, including the classes that you define  .
- A JavaBean property may be read, write, read only, or write only  .
- A JavaBean property can be accessed by using getter and setter methods that follow a naming convention .
- For example, a property named `color` would have the following getter and setter methods:

```java
public String getColor() {
  return color;
}

public void setColor(String color) {
  this.color = color;
}
```

- A JavaBean property can also be bound, which means that it can notify other objects when its value changes.
- To implement a bound property, the JavaBean class must register and notify property change listeners, which are objects that implement the `PropertyChangeListener` interface.
- The `java.beans` package also includes a class, `PropertyChangeSupport`, that takes care of most of the work of bound properties.
- This handy class keeps track of property listeners and includes a convenience method that fires property change events to all registered listeners.
- For example, to use `PropertyChangeSupport` for the `color` property, the JavaBean class would have the following code:

```java
private String color;
private PropertyChangeSupport pcs = new PropertyChangeSupport(this);

public String getColor() {
  return color;
}

public void setColor(String color) {
  String oldColor = this.color;
  this.color = color;
  pcs.firePropertyChange("color", oldColor, color);
}

public void addPropertyChangeListener(PropertyChangeListener listener) {
  pcs.addPropertyChangeListener(listener);
}

public void removePropertyChangeListener(PropertyChangeListener listener) {
  pcs.removePropertyChangeListener(listener);
}
```

- A JavaBean property can also be indexed, which means that it can have multiple values of the same type, such as an array or a list.
- To implement an indexed property, the JavaBean class must provide getter and setter methods that take an integer index as a parameter, as well as methods that access the entire array or list.
- For example, an indexed property named `colors` would have the following methods:

```java
public String getColor(int index) {
  return colors[index];
}

public void setColor(int index, String color) {
  colors[index] = color;
}

public String[] getColors() {
  return colors;
}

public void setColors(String[] colors) {
  this.colors = colors;
}
```

- A JavaBean property can also be constrained, which means that it can have a limited range of valid values, and that any attempt to change its value outside that range will trigger a vetoable change event.
- To implement a constrained property, the JavaBean class must register and notify vetoable change listeners, which are objects that implement the `VetoableChangeListener` interface.
- The `java.beans` package also includes a class, `VetoableChangeSupport`, that takes care of most of the work of constrained properties.
- This class is similar to `PropertyChangeSupport`, but it also allows the listeners to reject the proposed change by throwing a `PropertyVetoException`.
- For example, to use `VetoableChangeSupport` for a constrained property named `temperature`, the JavaBean class would have the following code:

```java
private int temperature;
private VetoableChangeSupport vcs = new VetoableChangeSupport(this);

public int getTemperature() {
  return temperature;
}

public void setTemperature(int temperature) throws PropertyVetoException {
  int oldTemperature = this.temperature;
  vcs.fireVetoableChange("temperature", oldTemperature, temperature);
  this.temperature = temperature;
}

public void addVetoableChangeListener(VetoableChangeListener listener) {
  vcs.addVetoableChangeListener(listener);
}

public void removeVetoableChangeListener(VetoableChangeListener listener) {
  vcs.removeVetoableChangeListener(listener);
}
```

- These are some of the main types and features of JavaBean properties. They are useful for creating reusable and customizable components that can be manipulated by builder tools and other JavaBean classes .