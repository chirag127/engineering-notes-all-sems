 Here is the content in markdown format for the topic ### Overriding for the notes of Unit 7 - Inheritance in Object Oriented System Design:

### Overriding

Overriding is a feature of OOP where a child class redefines a method of parent class. i.e. the child class has a method with the same name and signature as a method in the parent class.

When overriding occurs, the child class method is called instead of the parent class method.

#### Important Points

- The method in child class must have the same name, same parameters (or signature) and same return type as the method in parent class.
- The overriding method can also return a subclass type. This is known as covariant return type.
- The overriding method can have a less restrictive access modifier. For example, a method declared protected in superclass can be declared public in subclass.
- The overriding method can throw the same checked or unchecked exceptions or exceptions that are subtypes of the checked exceptions declared in the overridden method.
- An overriding method can have more flexible parameter type such as a superclass for a parameter type. This is known as contravariant parameter type.

#### Why Override?

- To provide specific implementation of a method. For example, a superclass might define a method as abstract and Subclasses can provide the implementation details.
- To modify the behaviour of the method, for example, making a method more precise or adding extra functionalities.
- To change the accessibility of a method, for example, changing a private method of superclass to a protected or public method in subclass.

#### Applications

- Used to customize behaviour of methods.
- Provides flexibility to reuse parent class code and modify it as needed.
- Used in frameworks to provide hooks for subclasses to customize behaviour.

[Detailed ASCII diagrams, code examples and other points can be added here to provide better understanding and complete the notes]