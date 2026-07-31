# Issues for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

Object oriented testing (OOT) is a testing approach that is based on the principles of object oriented programming, such as encapsulation, inheritance, and polymorphism. OOT aims to test the functionality, reliability, and quality of object oriented software systems.

However, OOT also faces some challenges and issues that are different from or more complex than those in traditional testing methods. Some of these issues are:

- **Class testing**: Class testing is the testing of a single class or a group of related classes in isolation from the rest of the system. Class testing involves testing the methods, attributes, constructors, and destructors of a class, as well as the interactions between the class and its subclasses or superclasses. Class testing can be difficult due to the following reasons:
  - The class may have hidden or private data and methods that are not accessible to the tester.
  - The class may have inherited methods or attributes from its superclasses that may affect its behavior or state.
  - The class may have polymorphic methods that may behave differently depending on the type of the object that invokes them.
  - The class may have dependencies or associations with other classes that may influence its functionality or quality.
- **Integration testing**: Integration testing is the testing of the interactions and interfaces between different classes or components of the system. Integration testing involves testing the communication, coordination, and collaboration between the objects of the system. Integration testing can be challenging due to the following reasons:
  - The system may have a large number of classes or components that have complex relationships and dependencies with each other.
  - The system may have dynamic binding or late binding, which means that the actual method or object that is invoked or used may not be known until runtime.
  - The system may have multiple inheritance or multiple interfaces, which means that a class or an object may have more than one superclass or interface that may affect its behavior or state.
  - The system may have abstract classes or interfaces, which means that some of the methods or attributes of a class or an object may not be implemented or defined until a subclass or an implementation class is created.
- **System testing**: System testing is the testing of the system as a whole, including its functionality, performance, usability, security, and compatibility with other systems or environments. System testing involves testing the system against the user requirements, specifications, and expectations. System testing can be problematic due to the following reasons:
  - The system may have emergent properties or behaviors that are not predictable or observable from the individual classes or components of the system.
  - The system may have reuse or adaptation of existing classes or components that may introduce errors or inconsistencies in the system.
  - The system may have concurrency or parallelism, which means that the system may have multiple threads or processes that may execute simultaneously or asynchronously, and may cause race conditions, deadlocks, or synchronization issues.
  - The system may have distributed or networked components, which means that the system may have components that are located on different machines or platforms, and may communicate through network protocols or middleware, and may face network failures, delays, or security breaches.