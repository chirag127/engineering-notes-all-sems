#### Classes and Objects in Scala

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members .
- Objects in Scala are single instances of their own definitions. They can be used to hold static methods or values, or to implement singleton patterns.
- To define a class, use the keyword `class` followed by an identifier and an optional list of constructor parameters. For example:

```scala
class Point(x: Int, y: Int) {
  // class body
}
```

- To create an object of a class, use the `new` keyword followed by the class name and the constructor arguments. For example:

```scala
val p = new Point(1, 2) // p is an object of type Point
```

- To define an object, use the keyword `object` followed by an identifier. For example:

```scala
object Hello {
  // object body
}
```

- An object can extend a class or a trait, or both. For example:

```scala
object Hello extends App {
  // object body
}
```

- A class and an object can have the same name and be defined in the same file. This is called a companion class and a companion object. They can access each other's private members. For example:

```scala
class Point(x: Int, y: Int) {
  // class body
}

object Point {
  // object body
}
```

- A companion object is often used to define factory methods or constants for the companion class. For example:

```scala
object Point {
  val origin = new Point(0, 0) // a constant object
  def apply(x: Int, y: Int) = new Point(x, y) // a factory method
}
```

- A companion object can also implement the `apply` method, which allows creating objects of the companion class without using the `new` keyword. For example:

```scala
val p = Point(1, 2) // equivalent to val p = new Point(1, 2)
```