### Overriding

Overriding is a feature in Object Oriented System Design that allows a subclass to provide a specific implementation of a method that is already provided by its superclass. This is done to change the behavior of the method in the subclass. Here are some key points to remember about overriding:

1. The method in the subclass must have the same signature as the method in the superclass. This means that the method must have the same name, return type, and parameters.
2. The method in the subclass must be marked with the `@Override` annotation to indicate that it is intended to override a method in the superclass.
3. The access level of the overriding method cannot be more restrictive than the access level of the overridden method. For example, if the method in the superclass is `public`, the overriding method in the subclass cannot be `private` or `protected`.
4. The overriding method can throw fewer or narrower checked exceptions than the overridden method.
5. If the method in the superclass is marked as `final`, it cannot be overridden in the subclass.
6. Overriding is used to achieve runtime polymorphism, where the behavior of an object can change at runtime based on its type.

These are some of the key points to remember about overriding in the context of inheritance in Object Oriented System Design. It is an important concept to understand and can be very useful in designing flexible and reusable code.