#### Inheritance in Scala

- Inheritance is an important pillar of OOP (Object Oriented Programming).
- It is the mechanism in Scala by which one class is allowed to inherit the features (fields and methods) of another class.
- Scala supports various types of inheritance including single, multilevel, multiple, and hybrid.
- You can use single, multilevel and hierarchal inheritance in your class.
- Multiple and hybrid inheritance can only be achieved by using traits.

##### Single Inheritance

- Single inheritance is the most simple form of inheritance.
- As shown in the example below, one class (subclass or child class) inherits from another class (superclass or parent class).

```scala
// Superclass
class Animal {
  def eat(): Unit = {
    println("Animal is eating")
  }
}

// Subclass
class Dog extends Animal {
  def bark(): Unit = {
    println("Dog is barking")
  }
}

// Main object
object Main {
  def main(args: Array[String]): Unit = {
    // Creating an instance of Dog class
    val dog = new Dog()
    // Calling methods of both classes
    dog.eat()
    dog.bark()
  }
}
```

- The output of the above program is:

```
Animal is eating
Dog is barking
```

- The subclass can access the public and protected members of the superclass, but not the private ones.
- The subclass can also override the methods of the superclass by using the `override` keyword.

##### Multilevel Inheritance

- Multilevel inheritance is the extension of single inheritance, where one class inherits from another class, which in turn inherits from another class.
- As shown in the example below, the class `Puppy` inherits from the class `Dog`, which inherits from the class `Animal`.

```scala
// Superclass
class Animal {
  def eat(): Unit = {
    println("Animal is eating")
  }
}

// Subclass 1
class Dog extends Animal {
  def bark(): Unit = {
    println("Dog is barking")
  }
}

// Subclass 2
class Puppy extends Dog {
  def play(): Unit = {
    println("Puppy is playing")
  }
}

// Main object
object Main {
  def main(args: Array[String]): Unit = {
    // Creating an instance of Puppy class
    val puppy = new Puppy()
    // Calling methods of all classes
    puppy.eat()
    puppy.bark()
    puppy.play()
  }
}
```

- The output of the above program is:

```
Animal is eating
Dog is barking
Puppy is playing
```

- The subclass can access the public and protected members of its direct and indirect superclasses, but not the private ones.
- The subclass can also override the methods of its direct and indirect superclasses by using the `override` keyword.

##### Multiple Inheritance

- Multiple inheritance is the scenario where one class inherits from more than one class.
- Scala does not support multiple inheritance for classes, but it does for traits.
- Traits are similar to interfaces in Java, but they can also have concrete methods and fields.
- As shown in the example below, the class `Bird` inherits from two traits `Flyable` and `Singable`.

```scala
// Trait 1
trait Flyable {
  def fly(): Unit = {
    println("Flying in the sky")
  }
}

// Trait 2
trait Singable {
  def sing(): Unit = {
    println("Singing a song")
  }
}

// Class
class Bird extends Flyable with Singable {
  def chirp(): Unit = {
    println("Chirping happily")
  }
}

// Main object
object Main {
  def main(args: Array[String]): Unit = {
    // Creating an instance of Bird class
    val bird = new Bird()
    // Calling methods of all traits and class
    bird.fly()
    bird.sing()
    bird.chirp()
  }
}
```

- The output of the above program is:

```
Flying in the sky
Singing a song
Chirping happily
```

- The class can access the public and protected members of all the traits it inherits from, but not the private ones.
- The class can also override the methods of the traits it inherits from by