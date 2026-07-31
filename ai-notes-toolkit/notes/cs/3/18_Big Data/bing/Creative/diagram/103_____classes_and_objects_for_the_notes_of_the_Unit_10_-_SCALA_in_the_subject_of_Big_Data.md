### Classes and Objects

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members.
- Objects in Scala are single instances of their own definitions. They can be used to hold static methods or values, or to implement the singleton pattern.
- A minimal class definition is simply the keyword `class` and an identifier. Class names should be capitalized.
- A class can have a primary constructor that takes parameters directly after the class name. These parameters become public fields of the class and can be accessed with the dot notation.
- A class can also have auxiliary constructors that are defined as methods named `this`. They must call the primary constructor or another auxiliary constructor as their first action.
- An object can be defined with the keyword `object` and an identifier. An object can extend another superclass, implement interfaces, and be passed around as though it were an instance of a class.
- An object can also be used as a companion object to a class, which means that it has the same name and is defined in the same source file as the class. A companion object can access the private members of the class and vice versa.
- A companion object can also define an `apply` method that can be used to create instances of the class without using the `new` keyword.

Here is an example of a class and an object in Scala:

```scala
// A class with a primary constructor that takes two parameters
class Person(val firstName: String, val lastName: String) {
  // An auxiliary constructor that takes one parameter
  def this(name: String) {
    // Calling the primary constructor
    this(name, "")
  }

  // A method that returns the full name
  def fullName: String = s"$firstName $lastName"
}

// An object that acts as a companion object to the class
object Person {
  // An apply method that creates a Person instance
  def apply(name: String): Person = new Person(name)

  // A static method that prints a greeting
  def greet(person: Person): Unit = {
    println(s"Hello, ${person.fullName}!")
  }
}

// Creating a Person instance using the apply method
val alice = Person("Alice")

// Creating a Person instance using the primary constructor
val bob = new Person("Bob", "Smith")

// Calling the greet method on the companion object
Person.greet(alice)
Person.greet(bob)
```