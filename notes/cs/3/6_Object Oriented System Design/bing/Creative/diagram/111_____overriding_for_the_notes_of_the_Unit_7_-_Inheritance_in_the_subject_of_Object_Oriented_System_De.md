# Overriding

- Overriding is an object-oriented programming feature that enables a child class to provide a different implementation for a method that is already defined and/or implemented in its parent class or one of its parent classes .
- The overridden method in the child class should have the same name, signature, and parameters as the one in its parent class .
- Overriding allows a subclass to customize or modify the behavior of a superclass method according to its specific needs.
- Overriding is one of the ways to achieve polymorphism in object-oriented programming, which means the ability of an object to take different forms depending on the context.
- Overriding is different from overloading, which is the ability to define multiple methods with the same name but different parameters in the same class.
- Overriding is also different from hiding, which is the ability to define a method with the same name and signature as a superclass method, but in a different scope (such as static or private).
- Overriding can be illustrated by the following example in Java:

```java
// A superclass that defines a method called print()
class Animal {
  public void print() {
    System.out.println("I am an animal");
  }
}

// A subclass that inherits from Animal and overrides the print() method
class Dog extends Animal {
  public void print() {
    System.out.println("I am a dog");
  }
}

// A test class that creates an Animal object and a Dog object
class Test {
  public static void main(String[] args) {
    Animal a = new Animal(); // a is an Animal object
    a.print(); // prints "I am an animal"
    Dog d = new Dog(); // d is a Dog object
    d.print(); // prints "I am a dog"
    Animal b = new Dog(); // b is an Animal reference to a Dog object
    b.print(); // prints "I am a dog" because of overriding
  }
}
```