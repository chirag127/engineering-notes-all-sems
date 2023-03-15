#### Package and Interface in Core Java

- A package is a collection of related classes and interfaces that are grouped together for the purpose of modularizing the code and enhancing its reusability.
- A package can be declared by using the keyword `package` followed by the package name at the top of the Java source file. For example, `package com.example;`
- A package can also be created by using a directory structure that reflects the package name. For example, the package `com.example` can be created by creating a directory named `com` and a subdirectory named `example` inside it. The Java source files that belong to this package should be placed inside the `example` directory.
- A package can be imported by using the keyword `import` followed by the package name or a specific class or interface name. For example, `import com.example.*;` or `import com.example.MyClass;`
- A package can also be imported implicitly by using the fully qualified name of the class or interface. For example, `com.example.MyClass myObject = new com.example.MyClass();`
- An interface is a contract that specifies the behavior of a class that implements it. An interface can contain abstract methods, default methods, static methods, and constants, but no instance variables or constructors.
- An interface can be declared by using the keyword `interface` followed by the interface name. For example, `interface MyInterface { ... }`
- An interface can be implemented by a class by using the keyword `implements` followed by the interface name. For example, `class MyClass implements MyInterface { ... }`
- A class that implements an interface must provide the implementation for all the abstract methods declared in the interface, or be declared as abstract itself.
- A class can implement multiple interfaces by using a comma-separated list of interface names. For example, `class MyClass implements MyInterface1, MyInterface2 { ... }`
- An interface can extend another interface by using the keyword `extends` followed by the interface name. For example, `interface MyInterface2 extends MyInterface1 { ... }`
- An interface that extends another interface inherits all the methods and constants of the superinterface, and can also declare new methods and constants.
- An interface can also be used as a reference type to refer to an object of any class that implements it. For example, `MyInterface myObject = new MyClass();`
- An interface can also be used as a parameter type or a return type of a method. For example, `public MyInterface myMethod(MyInterface myParameter) { ... }`