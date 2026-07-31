# Inheritance in Scala

Inheritance is an object-oriented concept that allows a class to reuse the features (fields and methods) of another class. In Scala, inheritance can be achieved by using the `extends` keyword. For example:

```scala
class Animal {
  def eat(): Unit = println("Animal is eating")
}

class Dog extends Animal {
  def bark(): Unit = println("Dog is barking")
}
```

In this example, the class `Dog` inherits from the class `Animal`, which means that a `Dog` object can access the `eat` method defined in `Animal`, as well as the `bark` method defined in `Dog`.

Scala supports various types of inheritance, such as:

- **Single inheritance**: A class can only inherit from one superclass. This is the most common and simple form of inheritance. For example:

```scala
class Vehicle {
  def drive(): Unit = println("Vehicle is driving")
}

class Car extends Vehicle {
  def honk(): Unit = println("Car is honking")
}
```

In this example, the class `Car` inherits from the class `Vehicle`, which means that a `Car` object can access the `drive` method defined in `Vehicle`, as well as the `honk` method defined in `Car`.

- **Multilevel inheritance**: A class can inherit from another class that also inherits from another class. This creates a hierarchy of classes that share some common features. For example:

```scala
class Animal {
  def eat(): Unit = println("Animal is eating")
}

class Mammal extends Animal {
  def breathe(): Unit = println("Mammal is breathing")
}

class Dog extends Mammal {
  def bark(): Unit = println("Dog is barking")
}
```

In this example, the class `Dog` inherits from the class `Mammal`, which also inherits from the class `Animal`. This means that a `Dog` object can access the `eat` method defined in `Animal`, the `breathe` method defined in `Mammal`, and the `bark` method defined in `Dog`.

- **Hierarchical inheritance**: A class can have more than one subclass that inherit from it. This creates a tree-like structure of classes that share some common features. For example:

```scala
class Animal {
  def eat(): Unit = println("Animal is eating")
}

class Dog extends Animal {
  def bark(): Unit = println("Dog is barking")
}

class Cat extends Animal {
  def meow(): Unit = println("Cat is meowing")
}
```

In this example, the class `Animal` has two subclasses, `Dog` and `Cat`, that inherit from it. This means that both `Dog` and `Cat` objects can access the `eat` method defined in `Animal`, as well as their own specific methods, `bark` and `meow`.

- **Multiple inheritance**: A class can inherit from more than one superclass. This allows a class to combine the features of different classes. However, Scala does not support multiple inheritance directly, because it can cause ambiguity and complexity. Instead, Scala uses a concept called **traits** to achieve multiple inheritance. Traits are similar to interfaces in Java, but they can also have concrete methods and fields. A class can mix in one or more traits by using the `with` keyword. For example:

```scala
trait Flyable {
  def fly(): Unit = println("Flying")
}

trait Swimable {
  def swim(): Unit = println("Swimming")
}

class Duck extends Animal with Flyable with Swimable {
  def quack(): Unit = println("Quacking")
}
```

In this example, the class `Duck` inherits from the class `Animal`, and also mixes in the traits `Flyable` and `Swimable`. This means that a `Duck` object can access the `eat` method defined in `Animal`, the `fly` and `swim` methods defined in `Flyable` and `Swimable`, and the `quack` method defined in `Duck`.

- **Hybrid inheritance**: A combination of two or more types of inheritance. For example, a class can inherit from another class and also mix in one or more traits. This allows a class to have more flexibility and functionality. For example:

```scala
trait Printable {
  def print(): Unit = println("Printing")
}

class Vehicle {
  def drive(): Unit = println("Vehicle is driving")
}

class Car extends Vehicle with Printable {
  def honk(): Unit = println("

```
