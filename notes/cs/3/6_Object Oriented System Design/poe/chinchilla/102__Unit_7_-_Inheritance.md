## Unit 7 - Inheritance

Inheritance is an important concept in object-oriented programming that allows the creation of new classes based on existing classes. It enables the code reuse and avoids redundancy. In this unit, we'll learn about inheritance in detail. Let's get started:

### 1. Introduction to Inheritance
- Inheritance is a mechanism where one class acquires the properties and methods of another class.
- The class that inherits the properties and methods is known as the subclass or derived class, and the class from which it inherits is known as the superclass or base class.
- The subclass can extend or modify the functionality of the superclass.

### 2. Types of Inheritance
There are four types of inheritance in Java:
- Single Inheritance: When a class inherits from a single superclass, it is known as single inheritance.
- Multilevel Inheritance: When a subclass inherits from a superclass, and that superclass is a subclass of another superclass, it is known as multilevel inheritance.
- Hierarchical Inheritance: When multiple classes inherit from a single superclass, it is known as hierarchical inheritance.
- Multiple Inheritance: When a class inherits from multiple superclasses, it is known as multiple inheritance. Java doesn't support multiple inheritance.

### 3. Access Modifiers and Inheritance
- Access modifiers control the visibility of variables and methods in a class.
- Inheritance affects the accessibility of variables and methods in the subclass.
- Public and protected members of the superclass can be accessed in the subclass.
- Private members of the superclass cannot be accessed in the subclass.

### 4. Method Overriding
- Method overriding is the process of declaring a method in the subclass with the same name, return type, and parameters as a method in the superclass.
- The method in the subclass overrides the method in the superclass.
- The subclass can also call the overridden method of the superclass using the `super` keyword.

### 5. Super Keyword
- The `super` keyword is used to refer to the superclass from the subclass.
- It can be used to call the constructor, variables, and methods of the superclass.
- The `super()` keyword is used to call the constructor of the superclass.

### 6. Final Keyword and Inheritance
- The `final` keyword can be used to make a class, method, or variable immutable.
- A final class cannot be inherited.
- A final method cannot be overridden in the subclass.
- A final variable cannot be changed.

In conclusion, inheritance is a powerful concept that allows us to reuse code and improve the flexibility of our programs. Understanding inheritance is essential for any Java developer.