#### Inheritance in Core Java

- Inheritance is one of the fundamental concepts of object-oriented programming in Java.
- Inheritance allows a class to inherit the properties and methods of another class, which is called the superclass or parent class.
- The class that inherits from the superclass is called the subclass or child class.
- Inheritance enables code reuse, polymorphism, and abstraction.
- In Java, inheritance is achieved by using the `extends` keyword in the class declaration.
- A subclass can access the public and protected members of the superclass, but not the private members.
- A subclass can also override the methods of the superclass, which means providing a new implementation for the same method signature.
- A subclass can also invoke the superclass constructor by using the `super` keyword in the first line of its constructor.
- A subclass can also use the `super` keyword to access the superclass methods that are hidden or overridden by the subclass methods.
- In Java, a class can only inherit from one superclass, which means Java does not support multiple inheritance. However, a class can implement multiple interfaces, which is a form of multiple inheritance.
- In Java, there are four types of inheritance: single, multilevel, hierarchical, and hybrid.

- Single inheritance is when a class inherits from only one superclass.
- Multilevel inheritance is when a class inherits from a superclass, which in turn inherits from another superclass, and so on.
- Hierarchical inheritance is when multiple subclasses inherit from the same superclass.
- Hybrid inheritance is a combination of two or more types of inheritance.

- An example of single inheritance in Java is:

```java
// Superclass
class Animal {
  public void eat() {
    System.out.println("Animal is eating");
  }
}

// Subclass
class Dog extends Animal {
  public void bark() {
    System.out.println("Dog is barking");
  }
}

// Main class
class Main {
  public static void main(String[] args) {
    // Create an object of the Dog class
    Dog dog = new Dog();

    // Call the methods of the superclass and the subclass
    dog.eat(); // Animal is eating
    dog.bark(); // Dog is barking
  }
}
```

- An example of multilevel inheritance in Java is:

```java
// Superclass
class Animal {
  public void eat() {
    System.out.println("Animal is eating");
  }
}

// Subclass 1
class Dog extends Animal {
  public void bark() {
    System.out.println("Dog is barking");
  }
}

// Subclass 2
class Puppy extends Dog {
  public void play() {
    System.out.println("Puppy is playing");
  }
}

// Main class
class Main {
  public static void main(String[] args) {
    // Create an object of the Puppy class
    Puppy puppy = new Puppy();

    // Call the methods of the superclass and the subclasses
    puppy.eat(); // Animal is eating
    puppy.bark(); // Dog is barking
    puppy.play(); // Puppy is playing
  }
}
```

- An example of hierarchical inheritance in Java is:

```java
// Superclass
class Animal {
  public void eat() {
    System.out.println("Animal is eating");
  }
}

// Subclass 1
class Dog extends Animal {
  public void bark() {
    System.out.println("Dog is barking");
  }
}

// Subclass 2
class Cat extends Animal {
  public void meow() {
    System.out.println("Cat is meowing");
  }
}

// Main class
class Main {
  public static void main(String[] args) {
    // Create an object of the Dog class
    Dog dog = new Dog();

    // Create an object of the Cat class
    Cat cat = new Cat();

    // Call the methods of the superclass and the subclasses
    dog.eat(); // Animal is eating
    dog.bark(); // Dog is barking
    cat.eat(); // Animal is eating
    cat.meow(); // Cat is meowing
  }
}
```

- An example of hybrid inheritance in Java is:

```java
// Superclass
class Animal {
  public void eat() {
    System.out.println("Animal is eating");
  }
}

// Subclass 1
class Dog extends Animal {
  public void bark() {
    System.out.println("Dog is barking");
  }
}

// Subclass 2
class Cat extends Animal {
  public void meow() {
    System.out.println("Cat is meowing");
  }
}

// Subclass 3
class Puppy extends Dog {
  public void play() {
    System.out.println("Puppy is playing");
  }
}

// Main