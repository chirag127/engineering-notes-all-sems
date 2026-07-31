### Overriding

- Overriding is an object-oriented programming feature that enables a child class to provide a different implementation for a method that is already defined and/or implemented in its parent class or one of its parent classes .
- The overridden method in the child class should have the same name, signature, and parameters as the one in its parent class .
- Overriding allows a subclass to customize or modify the behavior of a superclass method according to its specific needs.
- Overriding is one of the ways to achieve polymorphism in object-oriented programming, which means the ability of an object to take different forms depending on the context.
- Overriding is different from overloading, which is the ability to define multiple methods with the same name but different parameters in the same class.
- Overriding is also different from hiding, which is the ability to define a method with the same name and signature as a superclass method, but in a different scope (such as a static method or a private method).
- Overriding can be done by using the `@Override` annotation in Java, which indicates that the method is intended to override a superclass method and helps to detect errors at compile time.
- Overriding can also be done by using the `virtual` and `override` keywords in C#, which indicate that the method can be overridden by a subclass and that the method is overriding a superclass method respectively.
- Overriding can be illustrated by the following example in Java:

```java
// A superclass that defines a method called display()
class Animal {
  public void display() {
    System.out.println("I am an animal.");
  }
}

// A subclass that overrides the display() method
class Dog extends Animal {
  @Override // optional annotation
  public void display() {
    System.out.println("I am a dog.");
  }
}

// A test class that creates an object of the subclass and calls the display() method
class Test {
  public static void main(String[] args) {
    Animal a = new Dog(); // polymorphism
    a.display(); // prints "I am a dog."
  }
}
```