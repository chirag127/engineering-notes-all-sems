Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 8 - Polymorphism:

```markdown
# Unit 8 - Polymorphism

## What is polymorphism?

- Polymorphism is the ability of an object to take on different forms depending on the context.
- Polymorphism is one of the key concepts of object-oriented programming (OOP).
- Polymorphism allows us to write generic and reusable code that can work with different types of objects.

## Types of polymorphism

- There are two main types of polymorphism in OOP: compile-time polymorphism and run-time polymorphism.
- Compile-time polymorphism is also known as static polymorphism or overloading. It occurs when the compiler decides which method or operator to invoke based on the number, type, or order of the arguments at compile time.
- Run-time polymorphism is also known as dynamic polymorphism or overriding. It occurs when the compiler decides which method to invoke based on the actual type of the object at run time.
- Both types of polymorphism are achieved by using inheritance and abstract classes or interfaces.

## Examples of polymorphism

- An example of compile-time polymorphism is method overloading. Method overloading is when a class defines multiple methods with the same name but different parameters. For example, a class `Calculator` can have multiple methods named `add` that can take different types or numbers of arguments, such as `add(int a, int b)`, `add(double a, double b)`, or `add(int a, int b, int c)`.
- An example of run-time polymorphism is method overriding. Method overriding is when a subclass defines a method with the same name and parameters as a method in its superclass, but provides a different implementation. For example, a class `Animal` can have a method named `makeSound` that prints "Animal sound". A subclass `Dog` can override this method and print "Woof". A subclass `Cat` can override this method and print "Meow".
- Another example of run-time polymorphism is interface implementation. An interface is a contract that specifies the methods that a class must implement. A class that implements an interface can be treated as an instance of that interface. For example, an interface `Shape` can have a method named `getArea` that returns the area of the shape. A class `Circle` can implement this interface and provide its own formula for calculating the area. A class `Square` can also implement this interface and provide its own formula for calculating the area. A variable of type `Shape` can hold a reference to either a `Circle` or a `Square` object and invoke the `getArea` method polymorphically.
```