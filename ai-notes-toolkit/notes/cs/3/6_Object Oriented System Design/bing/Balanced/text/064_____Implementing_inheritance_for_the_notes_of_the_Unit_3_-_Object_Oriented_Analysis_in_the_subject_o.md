### Implementing inheritance for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design

- Inheritance is the mechanism of basing an object or class upon another object or class, retaining similar implementation .
- Inheritance enables you to create new classes that reuse, extend, and modify the behavior defined in other classes.
- Inheritance is one of the three primary characteristics of object-oriented programming, together with encapsulation and polymorphism.
- Inheritance provides code re-usability, as you can inherit the properties and methods of one class into another class, instead of writing the same code again and again.
- Inheritance also supports the concept of hierarchical classification, as you can form a hierarchy of classes that share some common attributes and behaviors.
- To implement inheritance, you need to define a base class (also called a super class or a parent class) and a derived class (also called a sub class or a child class).
- The base class is the class that provides the common attributes and methods for the derived classes to inherit.
- The derived class is the class that inherits the attributes and methods from the base class, and can also add its own attributes and methods.
- The syntax for defining a derived class varies depending on the programming language, but usually involves using a keyword such as `extends`, `inherits`, or `:` to indicate the relationship with the base class.
- For example, in Java, you can define a base class called `Animal` and a derived class called `Dog` as follows:

```java
// Define the base class
class Animal {
  // Declare some attributes
  String name;
  int age;

  // Define a constructor
  public Animal(String name, int age) {
    this.name = name;
    this.age = age;
  }

  // Define some methods
  public void eat() {
    System.out.println(name + " is eating.");
  }

  public void sleep() {
    System.out.println(name + " is sleeping.");
  }
}

// Define the derived class
class Dog extends Animal {
  // Declare some additional attributes
  String breed;
  boolean hasTail;

  // Define a constructor
  public Dog(String name, int age, String breed, boolean hasTail) {
    // Call the constructor of the base class
    super(name, age);
    this.breed = breed;
    this.hasTail = hasTail;
  }

  // Define some additional methods
  public void bark() {
    System.out.println(name + " is barking.");
  }

  public void wagTail() {
    if (hasTail) {
      System.out.println(name + " is wagging its tail.");
    }
  }
}
```

- In this example, the `Dog` class inherits the attributes and methods of the `Animal` class, and also adds its own attributes and methods.
- To create an object of the `Dog` class, you can use the `new` keyword and pass the appropriate arguments to the constructor:

```java
// Create a dog object
Dog d = new Dog("Spot", 3, "Labrador", true);

// Call the inherited methods
d.eat();
d.sleep();

// Call the additional methods
d.bark();
d.wagTail();
```

- The output of this code would be:

```
Spot is eating.
Spot is sleeping.
Spot is barking.
Spot is wagging its tail.
```

- Inheritance can also be applied to multiple levels, meaning that a derived class can itself be a base class for another derived class.
- For example, you can define another class called `Poodle` that inherits from the `Dog` class, and add some more attributes and methods:

```java
// Define another derived class
class Poodle extends Dog {
  // Declare some additional attributes
  String color;
  boolean isCurly;

  // Define a constructor
  public Poodle(String name, int age, String breed, boolean hasTail, String color, boolean isCurly) {
    // Call the constructor of the parent class
    super(name, age, breed, hasTail);
    this.color = color;
    this.isCurly = isCurly;
  }

  // Define some additional methods
  public void groom() {
    System.out.println(name + " is being groomed.");
  }

  public void showCurly() {
    if (isCurly) {
      System.out.println(name + " has curly fur.");
    }
  }
}
```

-