### Inheritance

Inheritance is an object-oriented concept that allows a class to reuse the features (fields and methods) of another class. The class that inherits the features is called a subclass (or a derived class or a child class). The class that provides the features is called a superclass (or a base class or a parent class).

Scala supports various types of inheritance, such as:

- Single inheritance: A subclass inherits from only one superclass.
- Multilevel inheritance: A subclass inherits from another subclass, which inherits from another subclass, and so on.
- Hierarchical inheritance: A superclass has more than one subclass.
- Multiple inheritance: A subclass inherits from more than one superclass.
- Hybrid inheritance: A combination of multiple and hierarchical inheritance.

Scala does not allow multiple inheritance for classes, but it can be achieved by using traits. Traits are abstract types that can contain fields and methods, and can be mixed in with classes using the `with` keyword. Traits can also extend other traits or classes, forming a linearization of the mixed-in types.

Some important points to remember about inheritance in Scala are:

- The `extends` keyword is used to indicate that a class inherits from another class or trait.
- The `override` keyword is used to indicate that a method or field is redefined in a subclass.
- The `super` keyword is used to access the members of the superclass from the subclass.
- The `final` keyword is used to prevent a class or a member from being inherited or overridden.
- The `sealed` keyword is used to restrict the subclasses of a class to the same source file.
- The `abstract` keyword is used to indicate that a class or a method is incomplete and needs to be implemented by a subclass.

Here is an example of single inheritance in Scala:

```scala
// A superclass that defines a person
class Person(val name: String, val age: Int) {
  def greet(): Unit = println(s"Hello, I am $name.")
}

// A subclass that inherits from Person and defines a student
class Student(name: String, age: Int, val course: String) extends Person(name, age) {
  override def greet(): Unit = println(s"Hello, I am $name, a student of $course.")
}

// An object that creates and uses instances of Person and Student
object InheritanceDemo {
  def main(args: Array[String]): Unit = {
    val p1 = new Person("Alice", 25)
    p1.greet() // Hello, I am Alice.
    val s1 = new Student("Bob", 20, "Scala")
    s1.greet() // Hello, I am Bob, a student of Scala.
  }
}
```