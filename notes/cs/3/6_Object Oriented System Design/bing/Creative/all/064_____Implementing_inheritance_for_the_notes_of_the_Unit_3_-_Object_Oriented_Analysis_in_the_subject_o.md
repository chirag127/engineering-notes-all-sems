# Implementing inheritance for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design

- Inheritance is the mechanism of basing an object or class upon another object or class, retaining similar implementation .
- Inheritance enables you to create new classes that reuse, extend, and modify the behavior defined in other classes.
- Inheritance is one of the three primary characteristics of object-oriented programming, together with encapsulation and polymorphism.
- Inheritance provides code re-usability, as you can inherit the properties and methods of one class into another class, instead of writing the same code again and again.
- Inheritance also supports the concept of hierarchical classification, where you can create a hierarchy of classes that share some common attributes and behaviors, but also have some specific ones.
- Inheritance can be implemented in different ways, depending on the programming language and the type of inheritance. Some common types of inheritance are:
  - Single inheritance: A class inherits from only one parent class.
  - Multiple inheritance: A class inherits from more than one parent class.
  - Multilevel inheritance: A class inherits from a parent class, which in turn inherits from another parent class, and so on.
  - Hierarchical inheritance: More than one class inherits from a single parent class.
  - Hybrid inheritance: A combination of two or more types of inheritance.
- Inheritance can be represented using a UML diagram, where a solid line with an empty arrowhead indicates a generalization relationship between a parent class and a child class.
- For example, the following UML diagram shows a single inheritance relationship between a class Animal and a class Dog, where Dog inherits the attributes and methods of Animal, and also has some specific ones.

![UML diagram of single inheritance](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Inheritance_example.svg/1200px-Inheritance_example.svg.png)

- To implement inheritance in a programming language, you need to follow the syntax and rules of that language. For example, in Java, you can use the keyword extends to indicate that a class inherits from another class. For example, the following Java code shows how to implement the single inheritance relationship between Animal and Dog.

```java
// A class to represent an animal
class Animal {
  // An attribute to store the name of the animal
  String name;

  // A constructor to initialize the name of the animal
  Animal(String name) {
    this.name = name;
  }

  // A method to make the animal sound
  void sound() {
    System.out.println("Animal makes a sound");
  }
}

// A class to represent a dog, which inherits from Animal
class Dog extends Animal {
  // An attribute to store the breed of the dog
  String breed;

  // A constructor to initialize the name and breed of the dog
  Dog(String name, String breed) {
    // Calling the constructor of the parent class
    super(name);
    this.breed = breed;
  }

  // A method to make the dog bark, which overrides the sound method of the parent class
  @Override
  void sound() {
    System.out.println("Dog barks");
  }
}
```