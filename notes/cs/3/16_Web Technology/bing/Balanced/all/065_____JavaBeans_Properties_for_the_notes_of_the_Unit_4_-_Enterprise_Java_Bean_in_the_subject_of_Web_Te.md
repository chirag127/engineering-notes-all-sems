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
- To implement a bound property, the JavaBean class must register and notify property change listeners.
- The `java.beans` package provides a class, `PropertyChangeSupport`, that simplifies the implementation of bound properties.
- A JavaBean property can also be constrained, which means that it can reject invalid values.
- To implement a constrained property, the JavaBean class must throw a `PropertyVetoException` if the value is not acceptable.
- The `java.beans` package also provides a class, `VetoableChangeSupport`, that simplifies the implementation of constrained properties.
- A JavaBean property can be customized by using a `BeanInfo` class that provides additional information about the property, such as its display name, description, editor, etc.
- A `BeanInfo` class can also specify the order and grouping of properties in a builder tool.