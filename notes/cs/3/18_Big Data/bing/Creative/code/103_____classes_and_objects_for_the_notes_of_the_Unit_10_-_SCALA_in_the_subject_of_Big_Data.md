# Classes and Objects in Scala

- Scala is a pure object-oriented language, which means that every value is an object and every operation is a method call.
- Scala also supports functional programming, which means that functions are also values and can be passed as arguments or returned as results.
- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members.
- A minimal class definition is simply the keyword `class` and an identifier. Class names should be capitalized.
- For example, `class Point` defines a class named `Point`.
- To create an object of a class, we use the `new` keyword followed by the class name and any arguments for the constructor.
- For example, `val p = new Point(1, 2)` creates a new object of class `Point` with arguments `1` and `2` for the constructor.
- A class can have a primary constructor that is defined along with the class header. The primary constructor can have parameters that are either `val` or `var`, which means that they become fields of the class and can be accessed from outside.
- For example, `class Point(val x: Int, val y: Int)` defines a class named `Point` with a primary constructor that takes two parameters `x` and `y` of type `Int` and makes them fields of the class.
- A class can also have secondary constructors that are defined as methods with the name `this`. Secondary constructors must call the primary constructor or another secondary constructor as the first statement.
- For example, `class Point(val x: Int, val y: Int) { def this() = this(0, 0) }` defines a class named `Point` with a primary constructor and a secondary constructor that takes no arguments and calls the primary constructor with `0` and `0`.
- A singleton object is a class that can have only one instance, i.e., object. A singleton object is defined with the keyword `object` instead of `class`.
- For example, `object Hello { def main(args: Array[String]): Unit = println("Hello, world!") }` defines a singleton object named `Hello` with a `main` method that prints "Hello, world!" to the standard output.
- A singleton object can extend another superclass, implement interfaces, and be passed around as though it were an instance of a class.
- A singleton object can also have the same name as a class, in which case it is called a companion object. A companion object can access the private members of the class and vice versa.
- For example, `class Point(val x: Int, val y: Int) { def distanceTo(p: Point): Double = Point.distance(this, p) } object Point { def distance(p1: Point, p2: Point): Double = math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2)) }` defines a class named `Point` with a method `distanceTo` that uses a companion object named `Point` with a method `distance` that calculates the distance between two points. The companion object can access the private fields `x` and `y` of the class and the class can access the private method `distance` of the object.