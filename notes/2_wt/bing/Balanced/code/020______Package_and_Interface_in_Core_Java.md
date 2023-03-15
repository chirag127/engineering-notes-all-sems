#### Package and Interface in Core Java

A package is a group of classes and interfaces that are related to each other. A package helps to organize the code and avoid naming conflicts. An interface is a group of abstract methods that define a contract for a class that implements it. An interface helps to achieve abstraction and polymorphism in Java.

To create a package, we use the keyword `package` followed by the package name at the top of the Java file. For example:

```java
package com.example.math;

public class Calculator {
    // class code
}
```

To use a class or an interface from a package, we need to import the package using the keyword `import` followed by the package name and the class or interface name. For example:

```java
import com.example.math.Calculator;

public class Test {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        // use calc object
    }
}
```

To create an interface, we use the keyword `interface` followed by the interface name. An interface can have abstract methods, default methods, static methods, and constants. For example:

```java
public interface Shape {
    double PI = 3.14; // constant
    double area(); // abstract method
    default void print() { // default method
        System.out.println("This is a shape.");
    }
    static double perimeter(double a, double b) { // static method
        return 2 * (a + b);
    }
}
```

To implement an interface, we use the keyword `implements` followed by the interface name. A class that implements an interface must provide the implementation for all the abstract methods of the interface. For example:

```java
public class Rectangle implements Shape {
    private double length;
    private double width;

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    @Override
    public double area() {
        return length * width;
    }

    @Override
    public void print() {
        System.out.println("This is a rectangle.");
    }
}
```

To use an interface, we can create an object of the class that implements it and assign it to a reference variable of the interface type. For example:

```java
Shape s = new Rectangle(10, 5);
System.out.println(s.area()); // 50.0
s.print(); // This is a rectangle.
System.out.println(Shape.perimeter(10, 5)); // 30.0
```