#### Package and Interface in Core Java

A package is a group of classes, interfaces, and sub-packages that are related in some way. A package helps to organize the code, avoid name conflicts, control access, and reuse existing types. An interface is a group of abstract methods that define a contract or a behavior that a class can implement. An interface helps to achieve abstraction, polymorphism, and multiple inheritance in Java.

Some of the key points to remember about packages and interfaces in Java are:

- To create a package, we use the `package` keyword followed by the package name as the first line of code in a Java file. For example, `package com.example;`
- To use a package, we use the `import` keyword followed by the package name or the class name. For example, `import java.util.*;` or `import java.util.Scanner;`
- To create an interface, we use the `interface` keyword followed by the interface name and the body. For example, `interface Vehicle { ... }`
- To use an interface, we use the `implements` keyword followed by the interface name in the class declaration. For example, `class Bike implements Vehicle { ... }`
- A package can contain classes, interfaces, and sub-packages, but an interface can only contain abstract methods, constants, default methods, and static methods.
- A package can be imported by any other package, but an interface can only be implemented by a class or extended by another interface.
- A package can have different access levels for its members, such as public, protected, default, and private, but an interface can only have public or default access for its members.