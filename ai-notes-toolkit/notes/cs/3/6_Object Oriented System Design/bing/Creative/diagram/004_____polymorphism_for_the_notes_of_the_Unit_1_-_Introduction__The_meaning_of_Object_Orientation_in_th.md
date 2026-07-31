Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of polymorphism for the notes of the Unit 1 - Introduction: The meaning of Object Orientation in the subject of Object Oriented System Design.

### Polymorphism

- Polymorphism is the ability of an object to take on different forms or behaviors depending on the context.
- Polymorphism is one of the key concepts of object-oriented programming, along with abstraction, encapsulation, and inheritance.
- Polymorphism allows for code reuse, flexibility, and extensibility, as well as reducing complexity and duplication.
- There are two main types of polymorphism: static and dynamic.

#### Static polymorphism

- Static polymorphism, also known as compile-time polymorphism, is when the form or behavior of an object is determined at compile time, based on the type of the object or the arguments of a method.
- Static polymorphism is achieved by using method overloading and operator overloading.
- Method overloading is when a class defines multiple methods with the same name but different parameters. The compiler chooses the appropriate method to call based on the number and type of the arguments.
- Operator overloading is when a class defines how an operator (such as +, -, *, /, etc.) works for its objects. The compiler chooses the appropriate operator to apply based on the type of the operands.
- Example of static polymorphism in Java:

```java
class Calculator {
  // Method overloading
  public int add(int a, int b) {
    return a + b;
  }

  public double add(double a, double b) {
    return a + b;
  }

  // Operator overloading
  public String toString() {
    return "This is a calculator";
  }
}

Calculator c = new Calculator();
System.out.println(c.add(2, 3)); // Prints 5
System.out.println(c.add(2.5, 3.5)); // Prints 6.0
System.out.println(c); // Prints This is a calculator
```

#### Dynamic polymorphism

- Dynamic polymorphism, also known as run-time polymorphism, is when the form or behavior of an object is determined at run time, based on the actual object that is referenced by a variable or a parameter.
- Dynamic polymorphism is achieved by using method overriding and inheritance.
- Method overriding is when a subclass defines a method with the same name and parameters as a method in its superclass. The subclass method overrides the superclass method and provides a different implementation. The compiler chooses the appropriate method to call based on the actual object that is referenced at run time.
- Inheritance is when a subclass inherits the attributes and methods of its superclass. The subclass can also add new attributes and methods or modify the inherited ones. The subclass is a more specific or specialized version of the superclass. The subclass can be used wherever the superclass is expected, as it is a subtype of the superclass. This is known as the substitution principle or the Liskov substitution principle.
- Example of dynamic polymorphism in Java:

```java
class Animal {
  public void makeSound() {
    System.out.println("Animal sound");
  }
}

class Dog extends Animal {
  // Method overriding
  public void makeSound() {
    System.out.println("Woof");
  }
}

class Cat extends Animal {
  // Method overriding
  public void makeSound() {
    System.out.println("Meow");
  }
}

Animal a = new Animal();
Animal b = new Dog();
Animal c = new Cat();
a.makeSound(); // Prints Animal sound
b.makeSound(); // Prints Woof
c.makeSound(); // Prints Meow
```