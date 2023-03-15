### Overriding
- Overriding is a feature in object-oriented programming that allows a subclass to provide a specific implementation of a method that is already provided by its superclass.
- The method in the subclass must have the same name, return type, and parameters as the method in the superclass.
- The keyword `@Override` can be used above the method in the subclass to indicate that the method is intended to override a method in the superclass.
- Overriding is used to achieve runtime polymorphism, where the behavior of an object can change depending on its type at runtime.
- When a method is called on an object, the method in the subclass is called if it exists, otherwise the method in the superclass is called.
- Overriding allows a subclass to inherit the methods of its superclass and modify or extend their behavior as needed.
- Overriding is different from overloading, where multiple methods with the same name but different parameters can exist in the same class.
- Overriding is also different from hiding, where a static method in a subclass has the same name as a static method in its superclass. In this case, the method in the subclass hides the method in the superclass.