## Unit 6 - Object Oriented Testing

- Object oriented testing is a software testing process that is conducted to test the software using object oriented paradigms like, encapsulation, inheritance, polymorphism, etc.   
- Object oriented testing is different from conventional testing strategies as the concepts of object oriented programming are way different from that of conventional ones.  
- The whole object oriented testing revolves around the fundamental entity known as “class”. 
- The software typically undergoes many levels of testing, from unit testing to system or acceptance testing. 
- Some of the techniques of object oriented testing are as follows: 
  - Fault Based Testing: This type of testing allows for designing test cases based on the customer specification or requirements. The test cases are derived from the faults that may occur in the software. The goal is to find as many faults as possible with a minimum number of test cases.
  - Class Testing Based on Method Testing: This approach is the simplest approach to test classes. Each method of the class is tested individually using white box testing techniques. The test cases are derived from the method specifications and the class invariants. The goal is to ensure the correctness and robustness of each method.
  - Class Testing Based on State Testing: This approach is more complex than the previous one. It tests the class as a whole, considering the possible states and transitions of the class. The test cases are derived from the state diagram or the state table of the class. The goal is to ensure the consistency and completeness of the class behavior.
  - Scenario Based Testing: This type of testing focuses on the interactions among the classes and the objects. The test cases are derived from the scenarios or use cases that describe the functionality of the software. The goal is to ensure the integration and communication of the classes and the objects.
  - Cluster Testing: This type of testing is similar to scenario based testing, but it involves a larger group of classes and objects that form a subsystem or a component of the software. The test cases are derived from the specifications and the architecture of the subsystem or the component. The goal is to ensure the functionality and performance of the subsystem or the component.
  - System Testing: This type of testing is the final level of testing, where the entire software is tested as a whole. The test cases are derived from the system requirements and the user expectations. The goal is to ensure the quality and reliability of the software.

- Some of the advantages of object oriented testing are as follows: 
  - It supports the reuse of test cases and test data, as the classes and the objects can be tested independently and in different contexts.
  - It facilitates the maintenance and evolution of the software, as the changes in the classes and the objects can be easily reflected in the test cases and the test data.
  - It improves the test coverage and the test effectiveness, as the testing techniques are tailored to the object oriented concepts and structures.

- Some of the challenges of object oriented testing are as follows: 
  - It requires more effort and expertise to design and execute the test cases, as the object oriented software is more complex and dynamic than the conventional software.
  - It may introduce new types of faults and errors, such as inheritance anomalies, polymorphism errors, encapsulation violations, etc.
  - It may encounter difficulties in measuring and evaluating the test results, as the object oriented software is more abstract and less observable than the conventional software.

- A mnemonic to remember the techniques of object oriented testing is: **FCCS-CS**. It stands for Fault, Class (Method), Class (State), Scenario, Cluster, System.