### Factory Methods

- Factory methods are a design pattern that allows a class to delegate the creation of objects to subclasses .
- Factory methods are useful when a class cannot anticipate the class of objects it must create, or when a class wants its subclasses to specify the objects it creates .
- Factory methods can be either static or instance methods.
  - Static factory methods are methods that return an instance of a class, but are not constructors. They are usually defined in the same class as the returned object, or in a separate factory class.
  - Instance factory methods are methods that return an instance of a class, but are not constructors. They are usually defined in a superclass or an interface, and are implemented by subclasses.
- Factory methods have several advantages over constructors :
  - They can have meaningful names that describe the purpose of the created object .
  - They can return a subtype of the declared return type, allowing for more flexibility and polymorphism .
  - They can cache and reuse existing objects, improving performance and memory efficiency .
  - They can reduce the coupling between classes, as the client code does not need to know the exact class of the created object .
- Factory methods have some disadvantages as well :
  - They can make the code more complex and harder to read, as the client code needs to invoke a method instead of using the new operator .
  - They can introduce dependencies on the factory class or the interface, which may not be desirable in some cases .
  - They can make testing and debugging more difficult, as the factory method may hide the details of the object creation .
- Factory methods are widely used in web technology, for example, to create objects that represent web requests, responses, sessions, cookies, etc.