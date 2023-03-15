### Inheritance

Inheritance is an object-oriented concept that allows a class to reuse the features (fields and methods) of another class. A class that inherits from another class is called a subclass, and a class that is inherited by another class is called a superclass. In Scala, inheritance is achieved by using the `extends` keyword.

Some important points about inheritance in Scala are:

- Scala supports single, multilevel, and hierarchical inheritance for classes. This means that a class can inherit from only one superclass, but a superclass can have multiple subclasses.
- Scala does not support multiple inheritance for classes, which means that a class cannot inherit from more than one superclass. However, Scala provides a feature called mixins, which allows a class to inherit from multiple traits. Traits are similar to interfaces in Java, but they can also have concrete members and constructors.
- Scala also supports hybrid inheritance, which is a combination of multiple and hierarchical inheritance. This can be achieved by using traits and classes together.
- Scala allows overriding the members of a superclass in a subclass by using the `override` keyword. This is necessary to avoid ambiguity and conflicts between the inherited members. However, Scala also allows using the `super` keyword to access the members of a superclass from a subclass.
- Scala allows defining abstract classes and traits, which are classes and traits that have some unimplemented members. These members must be implemented by the subclasses or the classes that mix in the traits. Abstract classes and traits cannot be instantiated directly, but they can be used as types and parameters.

Here is an example of inheritance in Scala:

```scala
// An abstract class Animal with an abstract method sound
abstract class Animal {
  def sound: String
}

// A class Dog that inherits from Animal and overrides the sound method
class Dog extends Animal {
  override def sound: String = "Woof"
}

// A class Cat that inherits from Animal and overrides the sound method
class Cat extends Animal {
  override def sound: String = "Meow"
}

// A trait Pet that has a concrete method greet
trait Pet {
  def greet: Unit = println("Hello")
}

// A class Puppy that inherits from Dog and mixes in Pet
class Puppy extends Dog with Pet

// A class Kitten that inherits from Cat and mixes in Pet
class Kitten extends Cat with Pet

// Creating instances of Puppy and Kitten
val pup = new Puppy
val kit = new Kitten

// Calling the inherited and mixed members
pup.sound // Woof
pup.greet // Hello
kit.sound // Meow
kit.greet // Hello
```