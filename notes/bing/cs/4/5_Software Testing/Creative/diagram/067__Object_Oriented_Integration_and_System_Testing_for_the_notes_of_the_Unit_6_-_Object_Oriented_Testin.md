The following is a detailed ascii diagram for Object Oriented Integration and System Testing for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing.

Object Oriented Integration and System Testing is a process of testing the software system that is composed of many object-oriented modules or classes. It ensures that the system meets the functional and non-functional requirements, and that the modules interact correctly with each other and with the external environment.

The diagram shows the levels of testing that are involved in Object Oriented Integration and System Testing, namely:

- Unit Testing: This is the testing of individual modules or classes in isolation, using stubs and drivers to simulate the dependencies. It verifies the internal logic and functionality of the modules, and checks for errors such as syntax, logic, and data flow.
- Subsystem Testing: This is the testing of a group of related modules or classes that form a subsystem, using stubs and drivers to simulate the external dependencies. It verifies the functionality and performance of the subsystem, and checks for errors such as interface, integration, and communication.
- System Testing: This is the testing of the entire system as a whole, using the actual or simulated environment and data. It verifies the functionality, performance, reliability, security, and usability of the system, and checks for errors such as system, configuration, and compatibility.
- Acceptance Testing: This is the testing of the system by the end-users or customers, using the actual or simulated environment and data. It verifies the satisfaction of the user requirements and expectations, and checks for errors such as user, operational, and business.

The diagram also shows the types of testing techniques that can be applied at each level, such as:

- White-box Testing: This is the testing of the internal structure and logic of the modules or classes, using the knowledge of the code and design. It can be used for unit testing and subsystem testing, and it includes techniques such as statement coverage, branch coverage, path coverage, and data flow testing.
- Black-box Testing: This is the testing of the external functionality and behavior of the modules or classes, using the knowledge of the specifications and requirements. It can be used for subsystem testing, system testing, and acceptance testing, and it includes techniques such as equivalence partitioning, boundary value analysis, decision table testing, and state transition testing.
- Grey-box Testing: This is the testing of the modules or classes using a combination of white-box and black-box techniques, using the knowledge of both the code and the specifications. It can be used for any level of testing, and it includes techniques such as code-based testing, fault-based testing, and scenario-based testing.

The diagram is drawn using the following symbols:

- [ ]: A module or class
- [ ]-[ ]: A dependency or association between modules or classes
- [ ]-[ ]-[ ]: A stub or driver that simulates a module or class
- [ ]-[ ]-[ ]-[ ]: A group of modules or classes that form a subsystem
- [ ]-[ ]-[ ]-[ ]-[ ]: The entire system
- [ ]-[ ]-[ ]-[ ]-[ ]-[ ]: The actual or simulated environment and data
- [ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]: The end-users or customers

The diagram is as follows:

```
[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]   Acceptance Testing
|                         |   Black-box Testing
|                         |
[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]   System Testing
| | | | | | | | | | | | | |   Black-box Testing
| | | | | | | | | | | | | |
[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]   Subsystem Testing
| | | | | | | | | | | | | |   Black-box Testing
| | | | | | | | | | | | | |   Grey-box Testing
| | | | | | | | | | | | | |
[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]   Unit Testing
| | | | | | | | | | | | | |   White-box Testing
| | | | | | | | | | | | | |   Grey-box Testing
| | | | | | | | | | | | | |
[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]   Modules or Classes
```