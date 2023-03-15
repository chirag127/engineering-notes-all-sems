### Single Inheritance

- Single inheritance is a type of inheritance in object-oriented programming, where a class (derived class) inherits the attributes and methods of another class (base class).
- The base class is also known as the parent class or the superclass, and the derived class is also known as the child class or the subclass.
- The derived class can reuse, extend, and modify the behavior of the base class, without modifying the base class itself.
- The derived class can also define its own attributes and methods, in addition to those inherited from the base class.
- Single inheritance enables code reusability, modularity, and polymorphism.
- Single inheritance is transitive, which means that if class B inherits from class A, and class C inherits from class B, then class C also inherits from class A.
- Single inheritance can be implemented using the `extends` keyword in Java, the `:` operator in C++, and the `class` statement in Python.

#### Example of Single Inheritance

- Suppose we have a base class called `Animal`, which defines some common attributes and methods for all animals, such as `name`, `age`, `sound`, and `eat`.
- We can create a derived class called `Dog`, which inherits from the `Animal` class, and defines some specific attributes and methods for dogs, such as `breed`, `bark`, and `fetch`.
- The `Dog` class can access and use the attributes and methods of the `Animal` class, as well as its own attributes and methods.
- The `Dog` class can also override the `sound` method of the `Animal` class, to provide a more specific implementation for dogs.

```java
// Java code for single inheritance
// Base class
class Animal {
  // Attributes
  String name;
  int age;

  // Constructor
  Animal(String name, int age) {
    this.name = name;
    this.age = age;
  }

  // Methods
  void sound() {
    System.out.println("Animal makes a sound");
  }

  void eat() {
    System.out.println("Animal eats food");
  }
}

// Derived class
class Dog extends Animal {
  // Attributes
  String breed;

  // Constructor
  Dog(String name, int age, String breed) {
    // Calling the constructor of the base class
    super(name, age);
    this.breed = breed;
  }

  // Methods
  // Overriding the sound method of the base class
  void sound() {
    System.out.println("Dog barks");
  }

  void bark() {
    System.out.println("Dog barks loudly");
  }

  void fetch() {
    System.out.println("Dog fetches the ball");
  }
}

// Main class
class Main {
  public static void main(String[] args) {
    // Creating an object of the base class
    Animal a = new Animal("Tommy", 5);
    // Calling the methods of the base class
    a.sound();
    a.eat();
    // Creating an object of the derived class
    Dog d = new Dog("Rocky", 3, "Labrador");
    // Calling the methods of the derived class
    d.sound();
    d.eat();
    d.bark();
    d.fetch();
    // Accessing the attributes of the derived class
    System.out.println("Name: " + d.name);
    System.out.println("Age: " + d.age);
    System.out.println("Breed: " + d.breed);
  }
}
```

The output of the above code is:

```
Animal makes a sound
Animal eats food
Dog barks
Dog eats food
Dog barks loudly
Dog fetches the ball
Name: Rocky
Age: 3
Breed: Labrador
```