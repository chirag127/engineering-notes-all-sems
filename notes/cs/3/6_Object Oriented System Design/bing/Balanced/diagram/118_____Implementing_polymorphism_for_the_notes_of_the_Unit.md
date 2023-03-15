### Implementing polymorphism

- Polymorphism is the ability of an object to take on different forms depending on the context.
- Polymorphism can be implemented in two ways: static and dynamic.
- Static polymorphism is also known as compile-time polymorphism or overloading. It occurs when the same name is used for different methods or operators that have different parameters or return types.
- Dynamic polymorphism is also known as run-time polymorphism or overriding. It occurs when a subclass inherits a method from a superclass and redefines its behavior for the subclass.
- Static polymorphism can be achieved by using method overloading or operator overloading.
  - Method overloading is when a class has multiple methods with the same name but different parameters. The compiler determines which method to call based on the number and type of arguments passed to the method.
  - Operator overloading is when a class defines how an operator works for its objects. For example, the + operator can be overloaded to perform string concatenation or matrix addition depending on the operands.
- Dynamic polymorphism can be achieved by using method overriding or abstract classes and interfaces.
  - Method overriding is when a subclass inherits a method from a superclass and provides a different implementation for it. The method signature (name, parameters, and return type) must be the same in both classes. The subclass method is called at run-time based on the type of the object that invokes it.
  - Abstract classes and interfaces are classes that cannot be instantiated and have one or more abstract methods that must be implemented by their subclasses or implementers. Abstract classes and interfaces provide a common interface for polymorphic behavior. For example, an abstract class Animal can have an abstract method makeSound() that is implemented differently by its subclasses Dog, Cat, and Bird. An interface Shape can have an abstract method getArea() that is implemented differently by its implementers Circle, Square, and Triangle.