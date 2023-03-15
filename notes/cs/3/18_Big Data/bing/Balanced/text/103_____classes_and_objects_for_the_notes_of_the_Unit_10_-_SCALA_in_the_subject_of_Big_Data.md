### Classes and Objects in Scala

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members .
- Objects in Scala are single instances of their own definitions. They can be used to hold static methods or values, or to implement the singleton pattern.
- To define a class in Scala, use the keyword `class` followed by an identifier (name) of the class. Optionally, you can also specify constructor parameters, a superclass, and/or traits.
- To create an object of a class, use the keyword `new` followed by the class name and constructor arguments (if any). Alternatively, you can use a companion object to define a factory method for creating instances of the class.
- To define an object in Scala, use the keyword `object` followed by an identifier (name) of the object. Optionally, you can also specify a superclass and/or traits.
- To access the members of a class or an object, use the dot notation, such as `obj.method` or `obj.value`.
- To override a method or a value in a subclass or a trait, use the keyword `override` before the definition.
- To define a private member of a class or an object, use the keyword `private` before the definition. This will restrict the access to the member within the same class or object.
- To define a protected member of a class or an object, use the keyword `protected` before the definition. This will restrict the access to the member within the same class or object and its subclasses.