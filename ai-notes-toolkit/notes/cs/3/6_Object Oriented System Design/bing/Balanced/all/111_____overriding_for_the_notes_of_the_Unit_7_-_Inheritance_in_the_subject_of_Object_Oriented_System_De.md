# Overriding

- Overriding is an object-oriented programming feature that enables a child class to provide a different implementation for a method that is already defined and/or implemented in its parent class or one of its parent classes .
- The overridden method in the child class should have the same name, signature, and parameters as the one in its parent class .
- Overriding allows a subclass to customize or modify the behavior of a superclass method according to its specific needs.
- Overriding is one of the ways to achieve polymorphism in object-oriented programming, which means the ability of an object to take different forms depending on the context.
- Overriding is different from overloading, which is the ability to define multiple methods with the same name but different parameters in the same class.
- Overriding is also different from hiding, which is the ability to define a method with the same name and signature as a superclass method, but in a different scope (such as static or private).
- Overriding can be done by using the `@Override` annotation in Java, the `virtual` and `override` keywords in C#, or the `super` keyword in Python.
- Overriding can be useful for implementing the Liskov substitution principle, which states that a subclass object should be able to replace a superclass object without affecting the correctness of the program .
- Overriding can also be useful for implementing the open-closed principle, which states that a class should be open for extension but closed for modification.
- Overriding can also be useful for implementing the template method pattern, which defines the skeleton of an algorithm in a superclass method and lets subclasses override some steps of the algorithm.