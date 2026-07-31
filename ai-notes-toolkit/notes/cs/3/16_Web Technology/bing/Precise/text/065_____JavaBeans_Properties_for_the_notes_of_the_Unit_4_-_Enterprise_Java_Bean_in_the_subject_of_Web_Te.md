### JavaBeans Properties

JavaBeans Properties are the characteristics of a JavaBean that can be accessed and manipulated by other objects. These properties are defined by the JavaBean's public getter and setter methods, which follow a naming convention. Here are some key points to remember about JavaBeans Properties:

1. JavaBeans Properties can be of any Java data type, including primitive types, objects, and arrays.
2. The naming convention for JavaBeans Properties is that the getter method for a property named `propertyName` should be `getPropertyName()` and the setter method should be `setPropertyName()`.
3. If the property is of type `boolean`, the getter method can also be named `isPropertyName()`.
4. JavaBeans Properties can be read-only, write-only, or read-write. A read-only property has only a getter method, a write-only property has only a setter method, and a read-write property has both.
5. JavaBeans Properties can be bound or constrained. A bound property notifies listeners when its value changes, while a constrained property allows listeners to veto a change to its value.
6. JavaBeans Properties can be indexed, meaning that they can be accessed using an index value. Indexed properties have getter and setter methods that take an additional `int` parameter to specify the index.

These are some of the key points to remember about JavaBeans Properties when studying for exams on the subject of Web Technology, specifically the Unit 4 - Enterprise Java Bean.