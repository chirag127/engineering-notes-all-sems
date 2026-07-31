### Overriding in Inheritance (Unit 7 - Object Oriented System Design)

- Overriding is a feature in object-oriented programming that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
- The method in the subclass must have the same name, return type, and parameters as the method in the superclass.
- The keyword `@Override` can be used above the method definition in the subclass to indicate that the method is intended to override a method in the superclass.
- Overriding is used to achieve runtime polymorphism, where the behavior of an object can vary depending on its type at runtime.
- When a method is called on an object, the method in the subclass is executed if it overrides the method in the superclass. Otherwise, the method in the superclass is executed.
- Overriding allows a subclass to inherit the methods and fields of its superclass while still being able to customize its behavior.
- It is important to follow the Liskov Substitution Principle when overriding methods, which states that objects of a superclass should be replaceable with objects of its subclasses without altering the correctness of the program.
- Overriding should not be confused with overloading, which is when multiple methods have the same name but different parameters within the same class.
