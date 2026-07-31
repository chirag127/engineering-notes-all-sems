#### Methods & Classes in Core Java

Java is an object-oriented programming language that supports the creation of classes, objects, and methods. In this section, we will discuss the methods and classes in Core Java.

##### Classes

- A class is a blueprint or a template for creating objects. It contains properties and methods that define the behavior of the objects.
- A class is defined using the keyword `class` followed by the class name.
- The properties of a class are defined using variables, and the behavior of a class is defined using methods.
- A class can be instantiated to create objects, which can then be used to access its properties and methods.

##### Methods

- A method is a block of code that performs a specific task. It can be called multiple times from different parts of the program.
- A method is defined using the keyword `public` followed by the return type, method name, and parameters (if any).
- The return type specifies the data type of the value returned by the method. It can be `void` if the method does not return any value.
- The method name should be descriptive and should indicate what the method does.
- The parameters specify the input values that the method accepts. They are optional and can be of any data type.
- A method can be overloaded by defining multiple methods with the same name but different parameters.
- A method can be overridden by a subclass by defining a method with the same name and parameters as the superclass.

##### Access Modifiers

- Access modifiers are used to control the visibility of classes, methods, and properties.
- There are four access modifiers in Java: `public`, `private`, `protected`, and default.
- `public` members can be accessed from any part of the program.
- `private` members can only be accessed from within the same class.
- `protected` members can be accessed from within the same class, the same package, and subclasses.
- Default members (no access modifier specified) can be accessed from within the same package.

##### Inheritance

- Inheritance is a mechanism in Java that allows a subclass to inherit the properties and methods of a superclass.
- A subclass is defined using the keyword `extends` followed by the superclass name.
- The subclass can access the public and protected members of the superclass.
- The subclass can override the methods of the superclass to provide a new implementation.
- The `super` keyword is used to call the constructor, methods, and properties of the superclass from the subclass.

##### Polymorphism

- Polymorphism is a concept in Java that allows an object to take on multiple forms.
- There are two types of polymorphism in Java: compile-time polymorphism and runtime polymorphism.
- Compile-time polymorphism is achieved through method overloading, where multiple methods with the same name but different parameters are defined in a class.
- Runtime polymorphism is achieved through method overriding, where a method in the subclass overrides a method in the superclass.

In summary, classes and methods are the building blocks of object-oriented programming in Java. Understanding how to define and use them is essential for creating robust and maintainable code.