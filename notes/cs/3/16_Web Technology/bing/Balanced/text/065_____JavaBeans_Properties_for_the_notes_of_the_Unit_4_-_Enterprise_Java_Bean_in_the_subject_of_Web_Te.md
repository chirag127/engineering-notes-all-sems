### JavaBeans Properties

- A JavaBean property is a named attribute that can be accessed by the user of the object  .
- The attribute can be of any Java data type, including the classes that you define  .
- A JavaBean property may be read, write, read only, or write only  .
- A JavaBean property can be accessed by using getter and setter methods that follow a naming convention  .
- A getter method is a public instance method that takes no arguments and returns the value of the property. It has the name `get` followed by the capitalized property name  .
- A setter method is a public instance method that takes one argument of the same type as the property and returns void. It has the name `set` followed by the capitalized property name  .
- A read only property has only a getter method, while a write only property has only a setter method .
- A boolean property can have a getter method with the name `is` followed by the capitalized property name instead of `get` .
- A JavaBean property can be bound or constrained .
- A bound property is a property that notifies other objects when its value changes. A bound property can have one or more property change listeners registered with it .
- A constrained property is a property that allows other objects to veto its value change. A constrained property can have one or more vetoable change listeners registered with it .
- The java.beans package provides classes and interfaces to support bound and constrained properties, such as PropertyChangeSupport, VetoableChangeSupport, PropertyChangeListener, and VetoableChangeListener .
- A JavaBean property can also be customized by using a BeanInfo class that provides additional information about the property, such as its display name, description, editor, and hidden status .