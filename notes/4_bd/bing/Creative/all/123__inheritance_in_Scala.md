#### Inheritance in Scala

- Inheritance is an important pillar of OOP (Object Oriented Programming). It is the mechanism in Scala by which one class is allowed to inherit the features (fields and methods) of another class .
- Inheritance supports the concept of "reusability", i.e. when we want to create a new class and there is already a class that includes some of the code that we want, we can derive our new class from the existing class.
- The keyword used for inheritance is `extends`. The syntax is:

```scala
class child_class_name extends parent_class_name {
  // Methods and fields
}
```

- The class whose features are inherited is known as superclass (or a base class or a parent class). The class that inherits the other class is known as subclass (or a derived class, extended class, or child class). The subclass can add its own fields and methods in addition to the superclass fields and methods.
- The subclass can override the methods of the superclass by using the `override` keyword. The subclass can also access the members of the superclass by using the `super` keyword.
- Scala supports various types of inheritance, such as single, multilevel, multiple, and hierarchical. Multiple and hybrid inheritance can only be achieved by using traits.
- Traits are like abstract classes that can have both abstract and concrete members. They can be mixed in with classes using the `with` keyword. Traits can also extend other traits or classes.
- The order of traits in the class definition matters, as the trait methods are resolved from left to right. If two or more traits define the same method, then the method will be overridden by the last trait in the class definition.
- Here are some examples of different types of inheritance in Scala:

```scala
// Single inheritance
class A() {
  def name: String = "A"
}

class B() extends A() {
  override def name: String = "B"
}

// Multilevel inheritance
class C() extends B() {
  override def name: String = "C"
}

// Multiple inheritance using traits
trait D {
  def name: String = "D"
}

trait E {
  def name: String = "E"
}

class F extends D with E {
  override def name: String = "F"
}

// Hierarchical inheritance
class G extends A() {
  override def name: String = "G"
}

class H extends A() {
  override def name: String = "H"
}

// Hybrid inheritance using traits
trait I extends D {
  override def name: String = "I"
}

trait J extends E {
  override def name: String = "J"
}

class K extends I with J {
  override def name: String = "K"
}

class L extends J with I {
  override def name: String = "L"
}
```

- Some mnemonics and learning tricks for inheritance in Scala are:

  - Remember the acronym SMMH for the types of inheritance: Single, Multilevel, Multiple, and Hierarchical.
  - Remember the keyword `extends` for class inheritance and `with` for trait inheritance.
  - Remember the keyword `override` for overriding methods and `super` for accessing superclass members.
  - Remember the order of traits in the class definition: left to right. The last trait overrides the previous ones.