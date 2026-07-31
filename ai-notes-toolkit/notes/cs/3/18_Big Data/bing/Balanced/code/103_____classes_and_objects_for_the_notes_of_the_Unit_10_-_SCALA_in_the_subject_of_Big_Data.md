# Classes and Objects in Scala

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members .
- Objects in Scala are single instances of their own definitions. They can be used to hold static methods or values, or to implement singleton patterns.
- To define a class in Scala, use the keyword `class` followed by an identifier (name) of the class. Optionally, you can also specify constructor parameters, a superclass, and/or traits.
- To create an object of a class, use the keyword `new` followed by the class name and constructor arguments (if any). Alternatively, you can use a companion object to define a factory method for creating instances of the class.
- To define an object in Scala, use the keyword `object` followed by an identifier (name) of the object. Optionally, you can also specify a superclass and/or traits.
- To access the members of a class or an object, use the dot notation, such as `obj.method` or `obj.value`. You can also use infix notation for methods that take one argument, such as `obj method arg`.
- To define a private member of a class or an object, use the keyword `private` before the member definition. This will restrict the access to the member within the same class or object.
- To define a getter and a setter for a member of a class or an object, use the keywords `def` and `_=`, respectively. For example, `def name = firstName + " " + lastName` defines a getter for the name, and `def name_= (value: String) = { ... }` defines a setter for the name.
- To define a case class in Scala, use the keyword `case` before the class definition. A case class is a special kind of class that automatically provides some useful features, such as equality, hashing, pattern matching, and a companion object with an apply method.
- To define a nested class or object in Scala, use the keyword `class` or `object` inside another class or object definition. A nested class or object can access the members of its enclosing class or object, but not vice versa.