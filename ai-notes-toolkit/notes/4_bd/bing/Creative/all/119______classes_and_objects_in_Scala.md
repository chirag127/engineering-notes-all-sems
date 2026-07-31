# Classes and Objects in Scala

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members .
- Objects in Scala are single instances of their own definitions. They can be used to hold static methods or values, or to implement singleton patterns.
- To define a class in Scala, use the keyword `class` followed by an identifier and an optional list of constructor parameters. For example:

```scala
// A class named Point with two parameters x and y
class Point(val x: Int, val y: Int)
```

- To create an object of a class, use the keyword `new` followed by the class name and the arguments for the constructor. For example:

```scala
// An object of class Point with x = 10 and y = 20
val p = new Point(10, 20)
```

- To define an object in Scala, use the keyword `object` followed by an identifier. For example:

```scala
// An object named Hello with a method greet
object Hello {
  def greet(name: String): Unit = {
    println(s"Hello, $name!")
  }
}
```

- To access the members of a class or an object, use the dot notation. For example:

```scala
// Accessing the x and y values of the object p
println(p.x)
println(p.y)

// Calling the greet method of the object Hello
Hello.greet("Scala")
```

- Classes and objects can also inherit from other classes or traits using the keyword `extends`. For example:

```scala
// A class named Circle that extends the class Point and has an additional parameter radius
class Circle(x: Int, y: Int, val radius: Int) extends Point(x, y)

// An object named Math that extends the trait scala.math.Pi and has a method area
object Math extends scala.math.Pi {
  def area(c: Circle): Double = {
    Pi * c.radius * c.radius
  }
}
```

- To create a subclass object of a superclass, use the keyword `new` followed by the subclass name and the arguments for the constructor. For example:

```scala
// A subclass object of class Circle with x = 0, y = 0 and radius = 5
val c = new Circle(0, 0, 5)
```

- To access the inherited members of a subclass or an object, use the dot notation. For example:

```scala
// Accessing the x, y and radius values of the object c
println(c.x)
println(c.y)
println(c.radius)

// Calling the area method of the object Math with the object c as an argument
println(Math.area(c))
```