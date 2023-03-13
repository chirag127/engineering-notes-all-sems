### JavaBeans Properties

- A JavaBean property is a named attribute that can be accessed by the user of the object  .
- The attribute can be of any Java data type, including the classes that you define  .
- A JavaBean property may be read, write, read only, or write only  .
- A JavaBean property follows a naming convention for its getter and setter methods .
  - For a boolean property, the getter method is prefixed with `is` and the setter method is prefixed with `set`. For example, `isReady()` and `setReady(boolean value)`.
  - For a non-boolean property, the getter method is prefixed with `get` and the setter method is prefixed with `set`. For example, `getName()` and `setName(String value)`.
- A JavaBean property can be bound or constrained .
  - A bound property notifies other objects when its value changes .
  - A constrained property allows other objects to veto its value change .
- A JavaBean property can be indexed or non-indexed .
  - A non-indexed property has a single value for the whole object .
  - An indexed property has an array of values for the object .
- A JavaBean property can be customized by using a `BeanInfo` class .
  - A `BeanInfo` class provides information about the bean's properties, methods, and events .
  - A `BeanInfo` class can be used to hide, rename, or reorder the bean's properties, methods, and events .
  - A `BeanInfo` class can also provide icons, descriptions, and custom editors for the bean's properties, methods, and events .