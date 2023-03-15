#### Classes and Objects in Scala

- A class is a blueprint for creating objects. It defines the state and behavior of the objects of that class.
- An object is an instance of a class. It has a unique identity and can access the members (fields and methods) of its class.
- Scala supports both object-oriented and functional programming paradigms. It allows defining classes and objects as well as functions and values.
- To define a class in Scala, use the `class` keyword followed by the name of the class and an optional parameter list. For example:

```scala
class Person(name: String, age: Int) {
  // class body
}
```

- To create an object of a class, use the `new` keyword followed by the name of the class and an optional argument list. For example:

```scala
val p = new Person("Alice", 20) // p is an object of Person class
```

- Scala also supports the concept of singleton objects, which are objects that are declared and initialized at the same time. To define a singleton object, use the `object` keyword followed by the name of the object. For example:

```scala
object Math {
  // object body
}
```

- A singleton object can be accessed by its name directly, without using the `new` keyword. For example:

```scala
Math.PI // access the PI value defined in Math object
```

- A singleton object can also be used to define static members (fields and methods) that belong to the class with the same name. This is called a companion object. For example:

```scala
class Circle(radius: Double) {
  // class body
}

object Circle {
  // object body
  def area(r: Double): Double = Math.PI * r * r // static method to calculate area of a circle
}
```

- A companion object can access the private members of its companion class and vice versa. For example:

```scala
class Circle(radius: Double) {
  private val r = radius // private field
  def getRadius: Double = r // public method to access private field
}

object Circle {
  def printRadius(c: Circle): Unit = println(c.r) // object method can access private field of class
}
```