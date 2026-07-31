# Classes and Objects in Scala

- Scala is a pure object-oriented language, which means that every value is an object and every operation is a method call.
- Scala also supports functional programming, which means that functions are also values and can be passed as arguments or returned as results.
- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members.
- A class is defined with the keyword `class` followed by an identifier and an optional list of constructor parameters. For example:

```scala
class Person(firstName: String, lastName: String)
```

- This defines a class named `Person` with two constructor parameters, `firstName` and `lastName`. The class does not have an explicit body, but it can be added with curly braces after the parameters. For example:

```scala
class Person(firstName: String, lastName: String) {
  def fullName: String = firstName + " " + lastName
}
```

- This adds a method named `fullName` to the class, which returns the concatenation of the first and last names. The method does not have any parameters, but it can be added with parentheses after the method name. For example:

```scala
def greet(name: String): String = "Hello, " + name
```

- This defines a method named `greet` that takes a parameter named `name` and returns a greeting string. The method can be invoked on an instance of the class using the dot notation. For example:

```scala
val alice = new Person("Alice", "Smith")
val bob = new Person("Bob", "Jones")
alice.greet(bob.fullName) // returns "Hello, Bob Jones"
```

- This creates two instances of the `Person` class using the `new` keyword and assigns them to variables named `alice` and `bob`. Then it invokes the `greet` method on `alice` and passes the `fullName` of `bob` as an argument.

- Objects in Scala are singleton instances of a class. They are defined with the keyword `object` followed by an identifier. For example:

```scala
object Math {
  def pi: Double = 3.14159
  def square(x: Double): Double = x * x
  def sum(x: Double, y: Double): Double = x + y
}
```

- This defines an object named `Math` that contains three methods, `pi`, `square`, and `sum`. The object does not have any constructor parameters, but it can inherit from another class or trait using the `extends` keyword. For example:

```scala
object Math extends Serializable
```

- This makes the `Math` object inherit from the `Serializable` trait, which means that it can be serialized and deserialized using the Java serialization mechanism.

- Objects can be used to define constants, utility methods, or singleton patterns. They can also be used as companions to classes, which means that they share the same name and scope as a class and can access its private members. For example:

```scala
class Circle(radius: Double) {
  import Circle._
  def area: Double = pi * square(radius)
}

object Circle {
  private def square(x: Double): Double = x * x
  val pi: Double = 3.14159
}
```

- This defines a class named `Circle` with a constructor parameter named `radius` and a method named `area` that computes the area of the circle. The class imports the members of the companion object `Circle`, which defines a private method named `square` and a constant named `pi`. The class can access the private method and the constant from the object, but the object cannot access the private parameter of the class. For example:

```scala
val c = new Circle(2.0)
c.area // returns 12.56636
Circle.pi // returns 3.14159
Circle.square(c.radius) // returns 4.0
c.radius // error: radius is private
```

- This creates an instance of the `Circle` class and assigns it to a variable named `c`. Then it accesses the `area` method of the class and the `pi` and `square` methods of the object. However, it cannot access the `radius` parameter of the class, as it is private and only visible within the class.