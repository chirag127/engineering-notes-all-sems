#### Classes and Objects in Scala

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members.
- Objects in Scala are singleton instances of some anonymous class. They can be used to hold static members that are not associated with instances of some class, or to act as special named instances of some class or trait.
- To define a class, use the keyword `class` followed by an identifier and an optional constructor with parameters. Class names should be capitalized.
- To create an instance of a class, use the keyword `new` followed by the class name and arguments, or omit the `new` keyword if the class has a companion object with an `apply` method .
- To define an object, use the keyword `object` followed by an identifier and an optional body with members. Object names should follow the same convention as class names.
- To access the members of a class or an object, use the dot notation, such as `point.x` or `A.twice(2)` .
- To override a member of a superclass, use the keyword `override` before the member definition. This helps to avoid accidental overriding and ensures compatibility with the superclass.
- To define a companion object, use the same name as the class and place it in the same source file. A companion object can access the private members of the class and vice versa. It can also define an `apply` method to act as a factory for the class instances, and an `unapply` method to enable pattern matching on the class.
- To define an implicit parameter for a method, use the keyword `implicit` before the parameter. The compiler will then try to find a value of the appropriate type in the scope or in the companion object of the type. This can be useful to avoid passing the same parameter repeatedly or to provide some default behavior.

: https://docs.scala-lang.org/tour/classes.html
: https://stackoverflow.com/questions/1755345/difference-between-object-and-class-in-scala