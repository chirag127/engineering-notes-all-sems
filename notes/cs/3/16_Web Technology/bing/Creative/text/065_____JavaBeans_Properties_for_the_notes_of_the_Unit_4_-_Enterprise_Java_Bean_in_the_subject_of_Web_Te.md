### JavaBeans Properties

- A JavaBean property is a named attribute that can be accessed by the user of the object  .
- The attribute can be of any Java data type, including the classes that you define  .
- A JavaBean property may be read, write, read only, or write only  .
- A JavaBean property can be bound or constrained.
  - A bound property is one that notifies other objects when its value changes.
  - A constrained property is one that allows other objects to veto a proposed change to its value.
- A JavaBean property can be accessed by using getter and setter methods that follow a naming convention .
  - A getter method is a public instance method that returns the value of the property .
  - A setter method is a public instance method that takes a single argument and assigns it to the property .
  - The name of the getter method must start with "get" or "is" (for boolean properties), followed by the capitalized name of the property .
  - The name of the setter method must start with "set", followed by the capitalized name of the property .
- A JavaBean property can be customized by using a BeanInfo class that provides additional information about the property .
  - A BeanInfo class is a public class that implements the BeanInfo interface .
  - A BeanInfo class can specify the display name, description, editor, and other attributes of the property .
  - A BeanInfo class can be associated with a JavaBean class by using the same name and package, or by using the Introspector.getBeanInfo method .