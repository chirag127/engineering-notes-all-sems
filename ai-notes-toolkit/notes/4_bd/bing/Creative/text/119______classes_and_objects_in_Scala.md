#### Classes and Objects in Scala

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members .
- Objects in Scala are single instances of their own definitions. They can be used to hold static methods or values, or to implement singleton patterns.
- To define a class in Scala, use the keyword `class` followed by an identifier and an optional list of constructor parameters  . For example:

```scala
// A class named Point with two parameters x and y
class Point(val x: Int, val y: Int)
```

- To create an object of a class, use the keyword `new` followed by the class name and the arguments for the constructor parameters  . For example:

```scala
// An object of class Point with x = 3 and y = 4
val p = new Point(3, 4)
```

- To define an object in Scala, use the keyword `object` followed by an identifier. An object can extend a class or a trait, or be standalone. For example:

```scala
// An object named Hello that extends the App trait
object Hello extends App {
  println("Hello, world!")
}
```

- An object can also have the same name as a class, in which case it is called a companion object. A companion object can access the private members of the class, and vice versa. For example:

```scala
// A class named Complex with two parameters real and imaginary
class Complex(val real: Double, val imaginary: Double)

// A companion object named Complex with a factory method
object Complex {
  // A method that creates a Complex object from polar coordinates
  def fromPolar(magnitude: Double, angle: Double) = {
    new Complex(magnitude * math.cos(angle), magnitude * math.sin(angle))
  }
}
```

- A companion object can also define an `apply` method, which can be used to create objects of the class without using the `new` keyword. For example:

```scala
// A class named Person with two parameters firstName and lastName
class Person(val firstName: String, val lastName: String)

// A companion object named Person with an apply method
object Person {
  // A method that creates a Person object from a full name
  def apply(fullName: String) = {
    val nameParts = fullName.split(" ")
    new Person(nameParts(0), nameParts(1))
  }
}

// Creating a Person object using the apply method
val p = Person("John Doe")
```