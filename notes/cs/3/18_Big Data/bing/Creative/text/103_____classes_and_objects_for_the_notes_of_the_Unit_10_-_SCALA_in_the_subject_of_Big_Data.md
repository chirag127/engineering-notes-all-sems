### Classes and Objects in Scala

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members  .
- Objects in Scala are single instances of their own definitions. They can be used to hold static methods or values, or to define singleton types.
- A minimal class definition is simply the keyword `class` and an identifier (name) of the class. For example:

```scala
class Person
```

- A class can have a primary constructor that takes parameters. The parameters are defined in the class header, after the class name . For example:

```scala
class Person(firstName: String, lastName: String)
```

- A class can also have a body that contains definitions of members. The body is enclosed in curly braces . For example:

```scala
class Person(firstName: String, lastName: String) {
  // a value member
  val fullName = firstName + " " + lastName

  // a method member
  def greet(): Unit = {
    println(s"Hello, $fullName!")
  }
}
```

- To create an object of a class, we use the `new` keyword followed by the class name and the arguments for the constructor (if any) . For example:

```scala
val alice = new Person("Alice", "Smith")
```

- To access the members of an object, we use the dot notation . For example:

```scala
println(alice.fullName) // prints Alice Smith
alice.greet() // prints Hello, Alice Smith!
```

- To define an object, we use the keyword `object` and an identifier (name) of the object. For example:

```scala
object Math {
  // a value member
  val PI = 3.14

  // a method member
  def square(x: Int): Int = {
    x * x
  }
}
```

- To access the members of an object, we use the same dot notation as for classes. For example:

```scala
println(Math.PI) // prints 3.14
println(Math.square(5)) // prints 25
```

- An object can extend another class or trait, and implement its abstract members. For example:

```scala
trait Greeter {
  def greet(): Unit
}

object Bob extends Greeter {
  def greet(): Unit = {
    println("Hi, I'm Bob.")
  }
}

Bob.greet() // prints Hi, I'm Bob.
```

- A class and an object can have the same name, in which case they are called companions. The class is called the companion class, and the object is called the companion object. They must be defined in the same source file, and they can access each other's private members. For example:

```scala
class Circle(radius: Double) {
  // a private value member
  private val area = Math.PI * radius * radius

  // a method member that uses the companion object's member
  def printArea(): Unit = {
    println(s"The area of this circle is ${Circle.format(area)}.")
  }
}

object Circle {
  // a private method member
  private def format(d: Double): String = {
    f"$d%.2f"
  }

  // a method member that uses the companion class's constructor
  def apply(radius: Double): Circle = {
    new Circle(radius)
  }
}

val c = Circle(2.5) // same as new Circle(2.5)
c.printArea() // prints The area of this circle is 19.63.
```