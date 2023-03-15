### Inheritance

Inheritance is an object-oriented concept that allows a class to reuse the features (fields and methods) of another class. The class that inherits the features is called a subclass (or a derived class or a child class). The class that provides the features is called a superclass (or a base class or a parent class).

Scala supports various types of inheritance, such as:

- Single inheritance: A subclass inherits from only one superclass.
- Multilevel inheritance: A subclass inherits from a superclass, which in turn inherits from another superclass, and so on.
- Hierarchical inheritance: A superclass has more than one subclass.
- Multiple inheritance: A subclass inherits from more than one superclass. This is not directly supported by Scala, but can be achieved by using traits.
- Hybrid inheritance: A combination of multiple and hierarchical inheritance. This is also not directly supported by Scala, but can be achieved by using traits.

To inherit from a superclass, a subclass uses the `extends` keyword. For example:

```scala
// A superclass
class Animal {
  def eat(): Unit = println("Eating")
}

// A subclass that inherits from Animal
class Dog extends Animal {
  def bark(): Unit = println("Barking")
}

// Another subclass that inherits from Animal
class Cat extends Animal {
  def meow(): Unit = println("Meowing")
}
```

In this example, `Dog` and `Cat` are subclasses of `Animal`, and they inherit the `eat` method from the superclass. They can also define their own methods, such as `bark` and `meow`.

A subclass can also override the methods of the superclass by using the `override` keyword. For example:

```scala
// A superclass
class Shape {
  def area(): Double = 0.0
}

// A subclass that overrides the area method
class Circle(val radius: Double) extends Shape {
  override def area(): Double = math.Pi * radius * radius
}

// Another subclass that overrides the area method
class Rectangle(val length: Double, val width: Double) extends Shape {
  override def area(): Double = length * width
}
```

In this example, `Circle` and `Rectangle` are subclasses of `Shape`, and they override the `area` method to calculate the area of different shapes.

A subclass can also call the methods of the superclass by using the `super` keyword. For example:

```scala
// A superclass
class Person(val name: String) {
  def greet(): Unit = println(s"Hello, $name")
}

// A subclass that calls the greet method of the superclass
class Student(name: String, val grade: Int) extends Person(name) {
  override def greet(): Unit = {
    super.greet()
    println(s"You are in grade $grade")
  }
}
```

In this example, `Student` is a subclass of `Person`, and it calls the `greet` method of the superclass by using `super.greet()`. It also adds its own message to the greeting.

A subclass can also inherit from a trait, which is an abstract type that defines a set of features. A trait can have both abstract and concrete methods, and can be mixed in with a class by using the `with` keyword. For example:

```scala
// A trait
trait Flyable {
  def fly(): Unit
}

// A class that inherits from a trait
class Bird extends Flyable {
  override def fly(): Unit = println("Flying with wings")
}

// Another class that inherits from a trait
class Plane extends Flyable {
  override def fly(): Unit = println("Flying with engines")
}

// A class that inherits from a class and a trait
class Helicopter extends Plane with Flyable {
  override def fly(): Unit = println("Flying with rotors")
}
```

In this example, `Bird` and `Plane` are classes that inherit from the `Flyable` trait, and they override the `fly` method to implement different ways of flying. `Helicopter` is a class that inherits from both `Plane` and `Flyable`, and it also overrides the `fly` method to implement its own way of flying.

A class can inherit from multiple traits by using the `with` keyword multiple times. For example:

```scala
// A trait
trait Swimmable {
  def swim(): Unit
}

// Another trait
trait Runnable {
  def run(): Unit
}

// A class that inherits from multiple traits
class Duck extends Bird with Swimmable with Runnable {
  override def swim(): Unit = println("