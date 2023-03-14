#### Inheritance in Core Java

- Inheritance is one of the fundamental concepts of object-oriented programming in Java.
- Inheritance allows a class to inherit the properties and methods of another class, which is called the superclass or parent class.
- The class that inherits from the superclass is called the subclass or child class.
- Inheritance enables code reuse, polymorphism, and abstraction.
- In Java, inheritance is achieved by using the `extends` keyword in the class declaration.
- A subclass can access the public and protected members of the superclass, but not the private members.
- A subclass can also override the methods of the superclass, which means providing a new implementation for the same method signature.
- A subclass can also invoke the superclass constructor by using the `super` keyword in the first line of its constructor.
- A subclass can also use the `super` keyword to access the superclass members that are hidden by the subclass members with the same name.
- Java supports single inheritance, which means a class can only extend one superclass. However, a class can implement multiple interfaces, which are abstract types that define a set of methods that the implementing class must provide.
- Java also supports multilevel inheritance, which means a subclass can inherit from another subclass, forming a hierarchy of classes.
- Java does not support multiple inheritance, which means a class cannot extend more than one superclass. This is to avoid the diamond problem, which is a situation where a class inherits from two superclasses that have a common superclass, leading to ambiguity and inconsistency.
- A simple example of inheritance in Java is:

```java
// Superclass
class Animal {
  // Instance variable
  String name;

  // Constructor
  Animal(String name) {
    this.name = name;
  }

  // Method
  void eat() {
    System.out.println(name + " is eating.");
  }
}

// Subclass
class Dog extends Animal {
  // Constructor
  Dog(String name) {
    // Invoking superclass constructor
    super(name);
  }

  // Method
  void bark() {
    System.out.println(name + " is barking.");
  }

  // Overriding superclass method
  @Override
  void eat() {
    System.out.println(name + " is eating dog food.");
  }
}

// Main class
class Main {
  public static void main(String[] args) {
    // Creating an object of superclass
    Animal a = new Animal("Tommy");
    a.eat(); // Output: Tommy is eating.

    // Creating an object of subclass
    Dog d = new Dog("Rocky");
    d.eat(); // Output: Rocky is eating dog food.
    d.bark(); // Output: Rocky is barking.

    // Upcasting: assigning a subclass object to a superclass reference
    Animal a2 = d;
    a2.eat(); // Output: Rocky is eating dog food.
    // a2.bark(); // Compile-time error: Animal class does not have bark() method

    // Downcasting: assigning a superclass object to a subclass reference
    // Dog d2 = a; // Compile-time error: incompatible types
    Dog d2 = (Dog) a; // Explicit casting is required
    d2.eat(); // Output: Tommy is eating dog food.
    d2.bark(); // Output: Tommy is barking.
    // Note: Downcasting can cause runtime errors if the object is not of the expected type
  }
}
```

- A possible mnemonic to remember the concept of inheritance is:

  - **I**nheritance **N**eeds **E**xtends **R**euse **I**mplement **T**ype **A**bstract **N**ame **C**onstructor **E**ncapsulation
  - Each letter corresponds to a keyword or concept related to inheritance in Java.