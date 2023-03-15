### JavaBeans Properties

- A JavaBean property is a named attribute that can be accessed by the user of the object  .
- The attribute can be of any Java data type, including the classes that you define  .
- A JavaBean property may be read, write, read only, or write only  .
- A JavaBean property can be accessed by using getter and setter methods that follow a naming convention  .
- A getter method is a public instance method that takes no arguments and returns the value of the property  .
- A setter method is a public instance method that takes one argument of the same type as the property and returns void  .
- The name of the getter method must start with "get" followed by the capitalized name of the property, unless the property is a boolean, in which case it may start with "is" instead  .
- The name of the setter method must start with "set" followed by the capitalized name of the property  .
- For example, if the property name is "name", the getter method is "getName()" and the setter method is "setName(String name)"  .
- A JavaBean property can be bound or constrained .
- A bound property is one that notifies other objects when its value changes .
- A constrained property is one that allows other objects to veto its value changes .
- A JavaBean property can be persistent or transient .
- A persistent property is one that is saved and restored along with the bean .
- A transient property is one that is not saved or restored with the bean .
- A JavaBean property can be customized by using a BeanInfo class that provides additional information about the property, such as its display name, description, editor, etc .