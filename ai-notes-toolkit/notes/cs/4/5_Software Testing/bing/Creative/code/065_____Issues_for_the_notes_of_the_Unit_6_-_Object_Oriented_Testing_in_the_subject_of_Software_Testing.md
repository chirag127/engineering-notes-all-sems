# Issues for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

Object oriented testing (OOT) is a testing approach that is based on the principles of object oriented programming, such as encapsulation, inheritance, and polymorphism. OOT aims to test the functionality, reliability, and quality of object oriented software systems.

However, OOT also faces some challenges and issues that are different from or more complex than those in traditional testing methods. Some of these issues are:

- **Class testing**: Class testing is the testing of a single class or a group of related classes in isolation from the rest of the system. Class testing involves testing the methods, attributes, constructors, and destructors of a class, as well as the interactions between the class and its subclasses or superclasses. Class testing can be difficult due to the following reasons:
  - The class may have hidden or private data and methods that are not accessible to the tester.
  - The class may have inherited methods or attributes from its superclasses that may affect its behavior or state.
  - The class may have polymorphic methods that may behave differently depending on the type of the object that invokes them.
  - The class may have dependencies or associations with other classes that may influence its functionality or quality.
- **Integration testing**: Integration testing is the testing of the interactions and interfaces between different classes or components of the system. Integration testing involves testing the communication, coordination, and collaboration between the objects of the system. Integration testing can be challenging due to the following reasons:
  - The system may have a large number of classes or components that have complex relationships and dependencies among them.
  - The system may have dynamic binding or late binding, which means that the actual method or object that is invoked or used is determined at run time, not at compile time. This makes it hard to predict or control the behavior or state of the system.
  - The system may have multiple inheritance or multiple interfaces, which means that a class or a component may inherit or implement methods or attributes from more than one superclass or interface. This may cause conflicts or ambiguities in the system.
- **System testing**: System testing is the testing of the system as a whole, including its functionality, performance, usability, security, and reliability. System testing involves testing the system against its requirements, specifications, and expectations. System testing can be problematic due to the following reasons:
  - The system may have incomplete or inconsistent requirements or specifications, which may make it hard to define or measure the quality or success of the system.
  - The system may have emergent properties or behaviors, which means that the system may exhibit properties or behaviors that are not evident or predictable from the individual classes or components of the system.
  - The system may have adaptive or evolutionary features, which means that the system may change or evolve over time, either by design or by user feedback. This may make it hard to maintain or verify the system.