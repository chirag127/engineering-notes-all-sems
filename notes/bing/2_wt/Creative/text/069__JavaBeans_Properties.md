### JavaBeans Properties

- A JavaBean property is a named attribute that can be accessed by the user of the object.
- The property can be of any Java data type, including the classes that you define.
- A property can be read-only, write-only, or read-write, depending on the presence of getter and setter methods.
- A getter method is a public method that returns the value of the property. It has the form `public <type> get<PropertyName>()`.
- A setter method is a public method that sets the value of the property. It has the form `public void set<PropertyName>(<type> value)`.
- A property can also be bound or constrained, meaning that it can notify other objects when its value changes, or it can allow other objects to veto its value change.
- A bound property has a pair of methods `public void addPropertyChangeListener(PropertyChangeListener listener)` and `public void removePropertyChangeListener(PropertyChangeListener listener)` that allow other objects to register or unregister as listeners for property change events.
- A constrained property has a pair of methods `public void addVetoableChangeListener(VetoableChangeListener listener)` and `public void removeVetoableChangeListener(VetoableChangeListener listener)` that allow other objects to register or unregister as listeners for vetoable change events.
- A vetoable change event is a special kind of property change event that can be rejected by any of the listeners, causing the property value to revert to its previous value.
- A property can also be indexed, meaning that it can have multiple values, accessed by an integer index. An indexed property has a pair of getter and setter methods that take an additional int parameter to specify the index. For example, `public <type> get<PropertyName>(int index)` and `public void set<PropertyName>(int index, <type> value)`.
- A JavaBean can have any number of properties, of any type and access mode. The properties of a JavaBean can be discovered by other tools or components using the JavaBeans Introspector class, which uses reflection to analyze the methods of the class and infer the properties.