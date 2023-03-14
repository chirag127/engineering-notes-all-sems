### Issues for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

Object oriented testing (OOT) is a testing approach that is based on the object oriented paradigm, which treats software as a collection of interacting objects. OOT aims to test the functionality, behavior, and quality of the software from the perspective of the objects and their interactions.

OOT faces some challenges and issues that are different from the traditional testing methods, such as:

- **Testing classes**: A class is a blueprint for creating objects, and it does not have a clear input-output behavior specification. Therefore, testing a class requires testing its methods, attributes, constructors, and destructors, as well as the interactions among them. Testing a class also requires testing its instances, or objects, which can have different states and behaviors depending on the context. A class can also have abstract methods, which are not implemented in the class but in its subclasses, making it difficult to test the class in isolation. 

- **Testing inheritance**: Inheritance is a mechanism that allows a class to inherit the features and behaviors of another class, called the superclass or parent class. Inheritance introduces some issues for testing, such as:

  - How to test the inherited methods and attributes in the subclass or child class?
  - How to test the overridden methods and attributes in the subclass or child class?
  - How to test the new methods and attributes added in the subclass or child class?
  - How to test the interactions between the superclass and the subclass?
  - How to test the effects of changes in the superclass on the subclass?  

- **Testing polymorphism**: Polymorphism is a feature that allows an object to behave differently depending on its type or context. Polymorphism can be achieved by using abstract classes, interfaces, or method overloading and overriding. Polymorphism introduces some issues for testing, such as:

  - How to test the dynamic binding of methods at runtime?
  - How to test the different behaviors of an object under different types or contexts?
  - How to test the compatibility and interoperability of different types of objects?  

- **Testing composition and encapsulation**: Composition is a mechanism that allows a class to contain other classes as its attributes, creating a complex object. Encapsulation is a principle that hides the internal details of a class from the outside world, exposing only the public interface. Composition and encapsulation introduce some issues for testing, such as:

  - How to test the interactions and dependencies among the composed classes?
  - How to test the effects of changes in the composed classes on the containing class?
  - How to test the internal state and behavior of a class without violating the encapsulation principle?  

- **Testing levels**: OOT involves different levels of testing, such as:

  - Unit testing: Testing the individual classes and methods in isolation.
  - Integration testing: Testing the interactions and dependencies among the classes and objects.
  - System testing: Testing the functionality and quality of the whole software system.
  - Acceptance testing: Testing the software system against the user requirements and expectations. 

- **Testing tools and techniques**: OOT requires different tools and techniques for testing, such as:

  - Test case design: Designing test cases that cover the different scenarios and states of the objects and their interactions.
  - Test case execution: Executing the test cases using automated or manual tools that can simulate the object behavior and environment.
  - Test case evaluation: Evaluating the test results using metrics and criteria that measure the object functionality, behavior, and quality. 

Some mnemonics and learning tricks for the issues of OOT are:

- **CIPET**: A mnemonic to remember the main concepts of OOT that introduce testing issues: Class, Inheritance, Polymorphism, Encapsulation, and Testing levels. 

- **FICED**: A mnemonic to remember the main issues of testing classes: Functionality, Interaction, Construction, Exception, and Destruction. 

- **IOTOP**: A mnemonic to remember the main issues of testing inheritance: Inherited, Overridden, Testing, Overloading, and Polymorphism. 

- **CETIC**: A mnemonic to remember the main issues of testing composition and encapsulation: Composition, Encapsulation, Testing, Interaction, and Change. 

- **DIEC**: A mnemonic to remember the main levels of OOT