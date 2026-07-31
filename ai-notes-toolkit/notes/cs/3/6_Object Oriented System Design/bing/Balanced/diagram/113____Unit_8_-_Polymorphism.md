## Unit 8 - Polymorphism

Polymorphism is one of the key concepts of object-oriented programming. It means that an object can have different forms or behaviors depending on the context. Polymorphism allows us to write generic and reusable code that can work with different types of objects.

There are two main types of polymorphism in Java: compile-time polymorphism and run-time polymorphism.

- Compile-time polymorphism is also known as static polymorphism or method overloading. It occurs when we have multiple methods with the same name but different parameters in the same class or its subclasses. The compiler determines which method to call based on the number and type of arguments passed to the method. For example:

```java
class Calculator {
  // method overloading
  public int add(int a, int b) {
    return a + b;
  }

  public double add(double a, double b) {
    return a + b;
  }

  public int add(int a, int b, int c) {
    return a + b + c;
  }
}

Calculator calc = new Calculator();
calc.add(10, 20); // calls the first method
calc.add(10.5, 20.5); // calls the second method
calc.add(10, 20, 30); // calls the third method
```

- Run-time polymorphism is also known as dynamic polymorphism or method overriding. It occurs when we have a method with the same name and parameters in a superclass and its subclass. The subclass can override the behavior of the superclass method and provide its own implementation. The compiler does not know which method to call at compile time, it is determined at run time based on the type of the object that invokes the method. For example:

```java
class Animal {
  // method overriding
  public void makeSound() {
    System.out.println("Animal makes sound");
  }
}

class Dog extends Animal {
  // method overriding
  public void makeSound() {
    System.out.println("Dog barks");
  }
}

class Cat extends Animal {
  // method overriding
  public void makeSound() {
    System.out.println("Cat meows");
  }
}

Animal a1 = new Animal();
Animal a2 = new Dog();
Animal a3 = new Cat();
a1.makeSound(); // prints "Animal makes sound"
a2.makeSound(); // prints "Dog barks"
a3.makeSound(); // prints "Cat meows"
```

Polymorphism can also be achieved by using interfaces and abstract classes. An interface is a contract that specifies the methods that a class must implement. An abstract class is a class that cannot be instantiated and may have some abstract methods that subclasses must implement. Both interfaces and abstract classes can be used as reference types for polymorphic objects. For example:

```java
interface Shape {
  // abstract method
  public double getArea();
}

class Circle implements Shape {
  private double radius;

  public Circle(double radius) {
    this.radius = radius;
  }

  // implementing the interface method
  public double getArea() {
    return Math.PI * radius * radius;
  }
}

class Rectangle implements Shape {
  private double length;
  private double width;

  public Rectangle(double length, double width) {
    this.length = length;
    this.width = width;
  }

  // implementing the interface method
  public double getArea() {
    return length * width;
  }
}

Shape s1 = new Circle(10);
Shape s2 = new Rectangle(20, 30);
System.out.println(s1.getArea()); // prints 314.1592653589793
System.out.println(s2.getArea()); // prints 600.0
```