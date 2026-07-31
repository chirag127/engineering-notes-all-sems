### Inheritance

Inheritance is an object-oriented concept that allows a class to reuse the features (fields and methods) of another class. The class that inherits the features is called a subclass (or a derived class or a child class). The class that provides the features is called a superclass (or a base class or a parent class).

Scala supports various types of inheritance, such as:

- Single inheritance: A subclass inherits from only one superclass.
- Multilevel inheritance: A subclass inherits from a superclass, which in turn inherits from another superclass, and so on.
- Hierarchical inheritance: A superclass has more than one subclass.
- Multiple inheritance: A subclass inherits from more than one superclass.
- Hybrid inheritance: A combination of multiple and hierarchical inheritance.

Scala does not allow multiple inheritance for classes, but it can be achieved by using traits. Traits are abstract types that can contain fields and methods, and can be mixed in with classes using the `with` keyword. Traits can also extend other traits or classes, forming a linearization of the mixed-in types.

Some examples of inheritance in Scala are:

```scala
// Single inheritance
class Animal {
  def eat(): Unit = println("Eating")
}

class Dog extends Animal {
  def bark(): Unit = println("Barking")
}

val d = new Dog()
d.eat() // Eating
d.bark() // Barking
```

```scala
// Multilevel inheritance
class Vehicle {
  def start(): Unit = println("Starting")
}

class Car extends Vehicle {
  def drive(): Unit = println("Driving")
}

class Tesla extends Car {
  def autopilot(): Unit = println("Autopilot")
}

val t = new Tesla()
t.start() // Starting
t.drive() // Driving
t.autopilot() // Autopilot
```

```scala
// Hierarchical inheritance
class Shape {
  def area(): Double = 0.0
}

class Circle(val radius: Double) extends Shape {
  override def area(): Double = math.Pi * radius * radius
}

class Rectangle(val length: Double, val width: Double) extends Shape {
  override def area(): Double = length * width
}

val c = new Circle(2.0)
val r = new Rectangle(3.0, 4.0)
println(c.area()) // 12.566370614359172
println(r.area()) // 12.0
```

```scala
// Multiple inheritance using traits
trait Flyable {
  def fly(): Unit = println("Flying")
}

trait Swimable {
  def swim(): Unit = println("Swimming")
}

class Duck extends Flyable with Swimable {
  def quack(): Unit = println("Quacking")
}

val d = new Duck()
d.fly() // Flying
d.swim() // Swimming
d.quack() // Quacking
```

```scala
// Hybrid inheritance using traits
trait A {
  def a(): Unit = println("A")
}

trait B extends A {
  def b(): Unit = println("B")
}

trait C extends A {
  def c(): Unit = println("C")
}

trait D extends B with C {
  def d(): Unit = println("D")
}

class E extends D {
  def e(): Unit = println("E")
}

val e = new E()
e.a() // A
e.b() // B
e.c() // C
e.d() // D
e.e() // E
```

References:

: https://www.javatpoint.com/scala-inheritance
: https://www.geeksforgeeks.org/inheritance-in-scala/
: https://www.baeldung.com/scala/inheritance
: https://docs.scala-lang.org/tour/mixin-class-composition.html