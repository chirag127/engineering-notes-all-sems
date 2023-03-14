## Unit 6 - Object Oriented Testing

- Object oriented testing is a software testing process that is conducted to test the software using object oriented paradigms like encapsulation, inheritance, polymorphism, etc.
- Object oriented testing is different from conventional testing methods because of the following reasons:
  - A class does not have a clearly defined input-output behavior, unlike a function or a procedure.
  - A class can only be tested dynamically through its instances or objects, not statically.
  - A class can inherit features from other classes, which introduces complexity and dependencies in testing.
  - A class can communicate with other classes through messages, which affects the control flow and the state of the objects.
- Object oriented testing encompasses three levels, namely, unit testing, subsystem testing, and system testing:
  - Unit testing focuses on testing the methods of a class individually, as well as the interactions among the methods and the state of the object.
  - Subsystem testing focuses on testing the collaborations among a group of classes that form a subsystem, as well as the interfaces and contracts of the subsystem.
  - System testing focuses on testing the functionality and performance of the entire system, as well as the integration with other systems and the user requirements.
- Some of the techniques of object oriented testing are:
  - Fault based testing: This technique allows for designing test cases based on the user specification or the design specification of the class, and identifying the possible faults or errors that may occur in the class.
  - Class testing based on method testing: This technique is the simplest approach to test classes. Each method of the class is tested separately using conventional testing techniques, such as boundary value analysis, equivalence partitioning, etc. Then, the interactions among the methods are tested using state-based testing or scenario-based testing.
  - Random testing: This technique involves generating random test cases for the methods of the class, and checking the results against the expected behavior or the specification of the class. This technique can be useful for testing large and complex classes, or classes that have unpredictable behavior.
  - Partition testing: This technique involves dividing the class into partitions based on some criteria, such as the functionality, the state, the inheritance hierarchy, etc. Then, test cases are designed for each partition, and the results are compared with the expected behavior or the specification of the class. This technique can reduce the number of test cases and increase the coverage of testing.
  - Inter-class testing: This technique involves testing the interactions and communications among the classes that form a subsystem or a system. This can be done using techniques such as message sequence charts, collaboration diagrams, use case diagrams, etc. This technique can test the dynamic behavior and the functionality of the system.