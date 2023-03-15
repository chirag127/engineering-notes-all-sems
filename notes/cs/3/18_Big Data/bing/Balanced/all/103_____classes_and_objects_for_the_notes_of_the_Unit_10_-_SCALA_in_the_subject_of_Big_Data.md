# Classes and Objects

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members.
- Objects in Scala are single instances of their own definitions. They can be used to hold static methods or values, or to implement the singleton pattern.
- Scala is more object-oriented than Java because in Scala, we cannot have static members. Instead, Scala has singleton objects.
- Scala also supports multiple class constructors, inheritance, abstract classes, and traits, which are similar to interfaces but can also contain concrete members .
- To define a class in Scala, we use the keyword `class` followed by an identifier and an optional list of parameters. The parameters are also called primary constructor parameters, and they can be prefixed with `val` or `var` to make them public fields of the class .
- To define an object in Scala, we use the keyword `object` followed by an identifier. An object can extend another class or trait, and can have its own members.
- To create an instance of a class, we use the `new` keyword followed by the class name and the arguments for the primary constructor. Scala also supports the use of `apply` methods in companion objects to create instances without using `new` .
- To access the members of a class or object, we use the dot notation, such as `obj.method` or `obj.field` .

Here is an example of a class and an object in Scala:

```scala
// A class with a primary constructor that takes two parameters
class Person(val firstName: String, val lastName: String) {
  // A method that returns the full name
  def fullName: String = firstName + " " + lastName
}

// An object that acts as a companion to the class
object Person {
  // An apply method that creates a person from a string
  def apply(name: String): Person = {
    val parts = name.split(" ")
    new Person(parts(0), parts(1))
  }
}

// Creating a person using the new keyword
val p1 = new Person("John", "Doe")
// Creating a person using the apply method
val p2 = Person("Jane Doe")
// Accessing the members of the person class
println(p1.firstName) // John
println(p2.fullName) // Jane Doe
```