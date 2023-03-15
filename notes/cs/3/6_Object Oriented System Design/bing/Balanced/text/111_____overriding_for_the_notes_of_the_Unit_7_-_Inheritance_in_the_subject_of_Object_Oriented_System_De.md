### Overriding

- Overriding is an object-oriented programming feature that enables a child class to provide a different implementation for a method that is already defined and/or implemented in its parent class or one of its parent classes .
- The overridden method in the child class should have the same name, signature, and parameters as the one in its parent class .
- Overriding allows a subclass to customize or modify the behavior of a superclass method according to its specific needs.
- Overriding is one of the ways to achieve polymorphism in object-oriented programming, which means the ability of an object to take different forms depending on the context.
- Overriding is different from overloading, which is the ability to define multiple methods with the same name but different parameters in the same class.
- Overriding is also different from hiding, which is the ability to define a method with the same name and signature as a superclass method, but in a different scope (such as static or private).
- Overriding can be done by using the `@Override` annotation in Java, which indicates that the method is intended to override a superclass method and helps to detect errors at compile time.
- Overriding can be illustrated by the following example in Java:

```java
// A superclass Animal with a method makeSound()
class Animal {
  public void makeSound() {
    System.out.println("Animal makes sound");
  }
}

// A subclass Dog that inherits from Animal and overrides the makeSound() method
class Dog extends Animal {
  @Override // This annotation indicates that the method is overriding a superclass method
  public void makeSound() {
    System.out.println("Dog barks");
  }
}

// A subclass Cat that inherits from Animal and overrides the makeSound() method
class Cat extends Animal {
  @Override
  public void makeSound() {
    System.out.println("Cat meows");
  }
}

// A main class that creates objects of Animal, Dog, and Cat and invokes their makeSound() methods
class Main {
  public static void main(String[] args) {
    Animal a = new Animal(); // An object of Animal class
    a.makeSound(); // Prints "Animal makes sound"

    Animal b = new Dog(); // An object of Dog class, but referenced by Animal type
    b.makeSound(); // Prints "Dog barks" because of overriding

    Animal c = new Cat(); // An object of Cat class, but referenced by Animal type
    c.makeSound(); // Prints "Cat meows" because of overriding
  }
}
```