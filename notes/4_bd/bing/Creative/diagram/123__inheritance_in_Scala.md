Inheritance is an important pillar of OOP (Object Oriented Programming). It is the mechanism in Scala by which one class is allowed to inherit the features (fields and methods) of another class. Scala supports various types of inheritance, such as single, multilevel, multiple, and hierarchical . Multiple and hybrid inheritance can only be achieved by using traits .

#### Inheritance in Scala

The following diagram illustrates the basic architecture of inheritance in Scala using ASCII characters:

```
    +-----------------+
    |      Class      |
    +-----------------+
    | Fields and      |
    | Methods         |
    +-----------------+
    |                 |
    +-----------------+
          /   \
         /     \
        /       \
+-----------------+    +-----------------+
|    Subclass     |    |    Subclass     |
+-----------------+    +-----------------+
| Fields and      |    | Fields and      |
| Methods         |    | Methods         |
+-----------------+    +-----------------+
|                 |    |                 |
+-----------------+    +-----------------+
```

The keyword used for inheritance is `extends`. The subclass can access or override the members of the superclass using the `super` keyword. The subclass can also add its own fields and methods in addition to the superclass fields and methods.

Example of single inheritance:

```scala
class Animal {
  def sound(): Unit = {
    println("Animal makes a sound")
  }
}

class Dog extends Animal {
  override def sound(): Unit = {
    println("Dog barks")
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val dog = new Dog()
    dog.sound() // Dog barks
    dog.super.sound() // Animal makes a sound
  }
}
```

Example of multilevel inheritance:

```scala
class Animal {
  def sound(): Unit = {
    println("Animal makes a sound")
  }
}

class Dog extends Animal {
  override def sound(): Unit = {
    println("Dog barks")
  }
}

class Puppy extends Dog {
  override def sound(): Unit = {
    println("Puppy whines")
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val puppy = new Puppy()
    puppy.sound() // Puppy whines
    puppy.super.sound() // Dog barks
    puppy.super.super.sound() // Animal makes a sound
  }
}
```

Example of multiple inheritance using traits:

```scala
trait A {
  def a(): Unit = {
    println("A")
  }
}

trait B {
  def b(): Unit = {
    println("B")
  }
}

class C extends A with B {
  def c(): Unit = {
    println("C")
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val c = new C()
    c.a() // A
    c.b() // B
    c.c() // C
  }
}
```

Example of hierarchical inheritance:

```scala
class Animal {
  def sound(): Unit = {
    println("Animal makes a sound")
  }
}

class Dog extends Animal {
  override def sound(): Unit = {
    println("Dog barks")
  }
}

class Cat extends Animal {
  override def sound(): Unit = {
    println("Cat meows")
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val dog = new Dog()
    val cat = new Cat()
    dog.sound() // Dog barks
    cat.sound() // Cat meows
    dog.super.sound() // Animal makes a sound
    cat.super.sound() // Animal makes a sound
  }
}
```

Example of hybrid inheritance using traits:

```scala
trait A {
  def a(): Unit = {
    println("A")
  }
}

trait B extends A {
  override def a(): Unit = {
    println("B")
  }
}

trait C extends A {
  override def a(): Unit = {
    println("C")
  }
}

class D extends B with C {
  override def a(): Unit = {
    println("D")
  }
}

class E extends C with B {
  override def a(): Unit = {
    println("E")
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val d = new D()
    val e = new E()
    d.a() // D
    e.a() // E