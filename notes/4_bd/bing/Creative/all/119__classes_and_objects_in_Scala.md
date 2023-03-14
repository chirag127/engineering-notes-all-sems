#### Classes and Objects in Scala

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members.
- Objects in Scala are singleton instances of some anonymous class. They can be used to hold static members that are not associated with instances of some class, or to act as special named instances of some class or trait.
- To define a class, use the keyword `class` followed by an identifier and an optional constructor with parameters. Class names should be capitalized.
- To create an object, use the keyword `object` followed by an identifier. Object names should follow the same convention as class names.
- To create an instance of a class, use the `new` keyword followed by the class name and arguments for the constructor. Alternatively, you can omit the `new` keyword if the class has a companion object with an `apply` method .
- To access the members of a class or an object, use the dot notation, such as `point.x` or `A.twice(2)` .
- To override a member of a superclass, use the `override` keyword before the member definition.
- To make a member private, use the `private` keyword before the member definition. To make a member visible only within a certain scope, use the `private[scope]` syntax, where `scope` can be a package, class, or object.
- To define a getter and a setter for a variable, use the `def` keyword with parentheses for the getter and with a parameter for the setter. The name of the getter and setter should be the same as the variable, and the setter should have an underscore after the name.
- To define a companion object for a class, use the same name for the object as the class. A companion object can access the private members of the class, and vice versa. A companion object can also define an `apply` method to act as a factory for the class instances, and an `unapply` method to enable pattern matching for the class.

: https://docs.scala-lang.org/tour/classes.html
: https://stackoverflow.com/questions/1755345/difference-between-object-and-class-in-scala