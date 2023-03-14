### JavaBeans Properties

- A JavaBean property is a named attribute that can be accessed by the user of the object   .
- The attribute can be of any Java data type, including the classes that you define  .
- A JavaBean property may be read, write, read-only, or write-only   .
- To define a property in a bean class, supply public getter and setter methods.
- A special case for boolean properties allows the accessor method to be defined using is instead of get.
- Various specializations of basic properties are available and described in the following sections.

#### Indexed Properties
- An indexed property is an array instead of a single value.
- In this case, the bean class provides a method for getting and setting the entire array.
- For indexed properties, the bean class also provides methods for getting and setting a specific element of the array.

#### Bound Properties
- A bound property notifies listeners when its value changes.
- This has two implications:
  - The bean class includes addPropertyChangeListener () and removePropertyChangeListener () methods for managing the bean's listeners.
  - When a bound property is changed, the bean sends a PropertyChangeEvent to its registered listeners.
- The java.beans package includes a class, PropertyChangeSupport, that takes care of most of the work of bound properties.
- This handy class keeps track of property listeners and includes a convenience method that fires property change events to all registered listeners.