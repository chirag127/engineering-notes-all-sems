### Overriding

Overriding is a feature in Object Oriented System Design that allows a subclass to provide a specific implementation of a method that is already provided by its superclass. This is done by creating a method in the subclass with the same signature as the method in the superclass.

Here are some key points to remember about overriding:

1. The method in the subclass must have the same signature as the method in the superclass. This means that the method must have the same name, return type, and parameters.

2. The method in the subclass must be marked with the `@Override` annotation to indicate that it is intended to override a method in the superclass.

3. The access level of the overriding method cannot be more restrictive than the access level of the overridden method. For example, if the method in the superclass is `public`, the overriding method in the subclass must also be `public`.

4. The overriding method can throw fewer or narrower checked exceptions than the overridden method.

5. If a method is marked as `final` in the superclass, it cannot be overridden in the subclass.

6. Overriding is used to provide a specific implementation of a method in the subclass that is more appropriate for the objects of the subclass.

7. Overriding allows for dynamic method dispatch, which means that the method that is called is determined at runtime based on the type of the object that the method is called on.

8. Overriding is one of the ways in which inheritance can be used to achieve polymorphism in Object Oriented System Design.
