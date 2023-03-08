 Here is the content written in markdown format:

## Unit 8 - Polymorphism

Polymorphism is an Object Oriented Programming concept that refers to the ability of a method to do different things based on the object that invokes it. In polymorphism, objects of different types can respond to the same method call.

There are two types of polymorphism:

1. Compile time polymorphism: This is method overloading. It occurs when two or more methods in one class have the same method name but different parameters. The appropriate method is called based on the parameters passed.

Examples:
int sum(int a, int b) {return a+b;}
int sum(int a, int b, int c) {return a+b+c;}

Here, the appropriate sum method is called based on the number of parameters passed.

2. Runtime polymorphism: This is method overriding. It occurs when a child class overrides a method of the parent class. The overridden method is called dynamically at runtime depending on the object that invokes it.

Example:
Parent class:
class Animal {
  void makeSound() {
    System.out.println("Animal makes a sound");
  }
}

Child class:
class Dog extends Animal {
  void makeSound() {
    System.out.println("Dog barks");
  }
}

Here, even though we call makeSound() on the Animal reference, Dog's makeSound() is called at runtime due to method overriding.

Advantages:
- Code reusability - Parent class methods can be reused in child classes.
- Flexibility - Child classes can define their own behavior.
- Extensibility - New classes can be easily added into the hierarchy.

Disadvantages:
- Difficult to debug - The actual method being called is determined at runtime.
- Type casting issues - Care must be taken when casting to parent types.
- Tight coupling - The child class is tightly coupled with the parent class.

Applications: polymorphism is used in:
- Event handling
- Extension of classes
- Missing method handling
- Upcasting and downcasting