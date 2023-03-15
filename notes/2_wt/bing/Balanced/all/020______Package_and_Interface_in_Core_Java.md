#### Package and Interface in Core Java

- A **package** is a group of classes, interfaces, sub-packages, and other types that are logically related and organized into a folder structure.  
- A **interface** is a group of abstract methods and constants that define a contract or a behavior that a class can implement.  
- The main benefits of using packages and interfaces in Java are:
  - They make related types easier to find and use. 
  - They avoid naming conflicts and ensure uniqueness of types. 
  - They promote code reuse and modularity.  
  - They support access control and encapsulation.  
  - They enable polymorphism and dynamic binding. 
- To create a package, we use the keyword `package` followed by the package name at the top of the Java source file.  
- To use a package, we use the keyword `import` followed by the package name or the specific type name.  
- To create an interface, we use the keyword `interface` followed by the interface name and optionally extends other interfaces.  
- To use an interface, we use the keyword `implements` followed by the interface name in the class declaration.  
- An example of a package declaration is:

```java
package com.example.myapp; // create a package named com.example.myapp
```

- An example of a package import is:

```java
import java.util.*; // import all types from the java.util package
import java.io.File; // import only the File type from the java.io package
```

- An example of an interface declaration is:

```java
interface Shape { // create an interface named Shape
  double PI = 3.14; // a constant
  double area(); // an abstract method
  double perimeter(); // another abstract method
}
```

- An example of an interface implementation is:

```java
class Circle implements Shape { // create a class named Circle that implements the Shape interface
  private double radius; // a private field
  public Circle(double radius) { // a public constructor
    this.radius = radius;
  }
  public double area() { // implement the area method
    return PI * radius * radius;
  }
  public double perimeter() { // implement the perimeter method
    return 2 * PI * radius;
  }
}
```

- A possible mnemonic to remember the difference between package and interface is: **P**ackage is a **P**lace where types are **P**ut together, **I**nterface is an **I**dea that types can **I**mplement.