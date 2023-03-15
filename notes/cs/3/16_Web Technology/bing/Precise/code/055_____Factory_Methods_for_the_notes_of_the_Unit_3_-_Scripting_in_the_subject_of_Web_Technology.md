### Factory Methods

- Factory methods are a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
- Factory methods are used when a class cannot anticipate the type of objects it needs to create or when a class wants to delegate the responsibility of object creation to its subclasses.
- Factory methods are typically implemented by defining an abstract method in the superclass that returns an object of the desired type. Subclasses then override this method to return an instance of the desired concrete class.
- Factory methods can be used to encapsulate the object creation process and provide a level of abstraction between the client code and the object creation code.
- Factory methods can also be used to implement the concept of "dependency injection" where the dependencies of a class are provided to it by an external entity, rather than the class creating its own dependencies.
- Factory methods can help to promote loose coupling between classes by reducing the dependencies between them.
- Factory methods can also be used to implement the "singleton" design pattern, where only a single instance of a class is allowed to exist at any given time.