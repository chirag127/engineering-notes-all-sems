 Here is the content in markdown format for the topic ### Inheritance for the notes of Unit 10 - Scala in the subject of Big Data:

### Inheritance

Inheritance is a mechanism in which a class can extend another class and inherit its properties and methods. It enables code reuse and promotes abstraction.

#### Points to Remember:

1. The class that inherits the properties and methods is called the *sub-class* or *child class*. The class whose properties and methods are inherited is called the *super-class* or *parent class*.
2. The sub-class inherits all the non-private properties and methods of the super-class.
3. The sub-class can also define its own properties and methods in addition to the inherited ones. This allows the sub-class to modify the behaviour of the super-class.
4. The super-class can be a class of any accessibility (public, private, protected), but the sub-class must be defined in the same package as the super-class if the super-class is private or protected. If the super-class is public, the sub-class can be defined in any package.
5. The sub-class constructor must call the super-class constructor explicitly if the super-class has a constructor that takes parameters. This is done using the keyword `super`.

**Example:**
```scala
class Animal {
  val name: String = "Animal"
  def eat: Unit = println("Eating...")
}

class Cat extends Animal {
  val name: String = "Cat"
}

object InheritanceDemo extends App {
  val cat = new Cat
  println(cat.name) // Prints "Cat"
  cat.eat // Prints "Eating..."
}
```

**Advantages:**
- Reusability of code. The sub-class reuses the code of the super-class, thus reducing duplication of code.
- Promotes abstraction. The sub-class represents a more specific category of the super-class and thus relates to the real world concept of inheritance.

**Disadvantages:**
- The super-class is tightly coupled with the sub-class. Any change to the super-class structure might break the sub-class.
- The sub-class inherits all the properties and methods of the super-class, even the ones it might not require. This can lead to wastage of resources.

**Applications:**
- Object oriented modeling to represent hierarchical relationships between categories (e.g. Animal and Cat example above).
- Reusing code of the super-class in the sub-class to avoid duplication and promote DRY (Don't Repeat Yourself) principle.

[Detailed diagrams and code examples can be added here if required to aid understanding]