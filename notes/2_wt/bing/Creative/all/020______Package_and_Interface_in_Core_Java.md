#### Package and Interface in Core Java

- A **package** is a group of classes, interfaces, sub-packages, and other types that are logically related and organized into a folder structure. A package helps to avoid naming conflicts, to find and use related types, and to reuse existing code .
- An **interface** is a group of abstract methods and constants that define a contract or a behavior that a class or an enum can implement. An interface helps to achieve abstraction, multiple inheritance, and polymorphism in Java .
- A package is created using the keyword `package` followed by the package name at the top of the Java file. For example:

```java
package com.example.math; // package declaration
public class Calculator { // class declaration
  // class body
}
```

- An interface is created using the keyword `interface` followed by the interface name. For example:

```java
public interface Drawable { // interface declaration
  public static final int RED = 1; // constant declaration
  public abstract void draw(); // method declaration
}
```

- A package can contain multiple classes and interfaces, as well as sub-packages. A package can be imported using the keyword `import` followed by the package name or a specific type name. For example:

```java
import com.example.math.*; // import all types from the math package
import com.example.math.Calculator; // import only the Calculator class from the math package
```

- An interface can contain multiple methods and constants, but cannot contain any implementation details. An interface can be implemented by a class or an enum using the keyword `implements` followed by the interface name. For example:

```java
public class Circle implements Drawable { // class declaration
  // class body
  public void draw() { // method implementation
    // method body
  }
}
```

- A package can be divided into two types: built-in packages and user-defined packages. Built-in packages are already defined in the Java API and provide various functionalities, such as input/output, networking, graphics, etc. For example, `java.util`, `java.io`, `java.lang`, `java.awt`, `java.applet`, `java.net`, etc. User-defined packages are created by the programmers according to their needs.
- An interface can be divided into two types: functional interfaces and marker interfaces. Functional interfaces are interfaces that have only one abstract method and can be used with lambda expressions. For example, `java.util.function.Predicate`, `java.util.function.Function`, `java.util.Comparator`, etc. Marker interfaces are interfaces that have no methods or constants and are used to mark a class as having some property or capability. For example, `java.io.Serializable`, `java.lang.Cloneable`, `java.util.RandomAccess`, etc.

- A package can be accessed by using the fully qualified name of the type or by using the `import` statement. A package can also have different levels of visibility, such as public, protected, default, and private, depending on the access modifiers used for the types and members. A package can also be declared as a module in Java 9 or later, which provides more control over the dependencies and encapsulation of the package.
- An interface can be accessed by using the interface name or by using the `import` statement. An interface can also have different levels of visibility, such as public, protected, default, and private, depending on the access modifiers used for the interface and its members. An interface can also have default methods and static methods, which provide some implementation details that can be inherited or overridden by the implementing classes.

- A package can be used to group related types, to avoid naming conflicts, to reuse existing code, and to modularize the application. A package can also be used to create a hierarchy of types, such as `java.lang.Object`, `java.lang.String`, `java.lang.Number`, `java.lang.Integer`, etc .
- An interface can be used to achieve abstraction, multiple inheritance, and polymorphism in Java. An interface can also be used to define a contract or a behavior that a class or an enum must follow, such as `java.lang.Comparable`, `java.lang.Runnable`, `java.util.Iterator`, etc .

- A mnemonic to remember the difference between a package and an interface in Java is:

  - **P**ackage: **P**rovides **P**rotection and **P**artition