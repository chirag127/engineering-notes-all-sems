 Here is the content on #### inheritance in Scala in markdown format:

#### Inheritance in Scala

Inheritance in Scala is defined using the `extends` keyword. It allows a class to inherit the properties and methods of another class.

**Advantages:**

- Code reuse: The child class inherits the methods and properties of the parent class, so you don't have to rewrite the same code.
- Polymorphism: The child class can override methods of the parent class and provide different implementations. This allows using child class objects wherever parent class objects are expected.

**Examples:**

```scala
class Animal {
  def eat = println("eating...")
}

class Dog extends Animal {
  def bark = println("woof!")
}

val d = new Dog
d.eat // Output: eating...
d.bark // Output: woof!
```

Here, the `Dog` class inherits from the `Animal` class, so a `Dog` can do everything an `Animal` can, plus more (in this case, barking).

**Note:** In Scala, all classes inherit from `Any`, which is an implicit superclass. This is why we can call methods like `toString` on any object.

**Mnemonics:**

- The `is-a` relationship: You can think of inheritance as an `is-a` relationship. For example, a `Dog` _is-a_ `Animal`.
- The extends keyword looks like an arrow pointing from child to parent, showing the direction of inheritance.

**Learning tricks:**

- Practice implementing hierarchies of classes to solidify the understanding of inheritance. For example, create an `Animal` class, then create `Dog`, `Cat`, `Fish` subclasses that inherit from it.
- Pay attention to method overriding and polymorphism by experimenting with subclasses that override parent methods.
- Read through Scala API documentation to see real-world examples of inheritance hierarchies.