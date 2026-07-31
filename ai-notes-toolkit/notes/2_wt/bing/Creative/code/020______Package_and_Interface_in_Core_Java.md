#### Package and Interface in Core Java

A package is a group of related classes, interfaces, and sub-packages that are used to organize the code and avoid naming conflicts. An interface is a group of abstract methods that define a contract or a behavior that a class can implement.

To create a package, we use the keyword `package` followed by the name of the package at the top of the Java file. For example:

```java
package com.example.math; // create a package named com.example.math

public class Calculator {
    // class definition
}
```

To use a class or an interface from a package, we need to import the package using the keyword `import` followed by the name of the package and the class or interface. For example:

```java
import com.example.math.Calculator; // import the Calculator class from the com.example.math package

public class Test {
    public static void main(String[] args) {
        Calculator calc = new Calculator(); // create an object of the Calculator class
        // use the methods of the Calculator class
    }
}
```

To create an interface, we use the keyword `interface` followed by the name of the interface. An interface can have abstract methods, default methods, static methods, and constants. For example:

```java
public interface Shape {
    // constant
    double PI = 3.14;

    // abstract method
    double area();

    // default method
    default void print() {
        System.out.println("This is a shape.");
    }

    // static method
    static void draw() {
        System.out.println("Drawing a shape.");
    }
}
```

To implement an interface, we use the keyword `implements` followed by the name of the interface. A class that implements an interface must provide the implementation of all the abstract methods of the interface. For example:

```java
public class Circle implements Shape {
    // instance variable
    private double radius;

    // constructor
    public Circle(double radius) {
        this.radius = radius;
    }

    // implement the abstract method of the Shape interface
    public double area() {
        return PI * radius * radius;
    }

    // override the default method of the Shape interface
    public void print() {
        System.out.println("This is a circle.");
    }
}
```

To use an interface, we can create an object of the class that implements the interface and assign it to a reference variable of the interface type. For example:

```java
public class Test {
    public static void main(String[] args) {
        Shape s = new Circle(5); // create an object of the Circle class and assign it to a Shape variable
        System.out.println(s.area()); // call the area method of the Circle class
        s.print(); // call the print method of the Circle class
        Shape.draw(); // call the static method of the Shape interface
    }
}
```