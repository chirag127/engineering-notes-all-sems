#### Test Drivers and Test Stubs software testing strategy

- Test Drivers and Test Stubs are two types of test harness, which is a collection of software and test data that is configured together in order to test a unit of a program by stimulating various conditions while constantly monitoring its outputs and behavior.
- Test Drivers and Test Stubs are used in integration testing, which is a type of testing that verifies the functionality, performance, and reliability of a group of interacting software modules.
- Test Drivers and Test Stubs are also known as dummy programs or mock objects, as they simulate the behavior of the missing or incomplete modules in the testing .
- Test Drivers are the programs that call or invoke the modules that are being tested. They are used in bottom-up testing approach, when the lower-level modules are ready to test, but the higher-level modules are still not ready yet. Test Drivers provide the input data and receive the output data from the modules under test .
- Test Stubs are the programs that are called or invoked by the modules that are being tested. They are used in top-down testing approach, when the higher-level modules are ready to test, but the lower-level modules are still not ready yet. Test Stubs provide the output data and receive the input data from the modules under test .
- The main purpose of using Test Drivers and Test Stubs is to isolate the modules under test from the dependencies or interactions with other modules, and to provide a controlled environment for testing  .
- The main advantages of using Test Drivers and Test Stubs are:
  - They allow early detection and correction of defects in the modules under test .
  - They reduce the complexity and risk of integration testing by breaking down the system into smaller and manageable units .
  - They enable parallel development and testing of different modules by different teams or individuals .
  - They increase the test coverage and reliability of the modules under test .
- The main disadvantages of using Test Drivers and Test Stubs are:
  - They require extra effort and time to develop, maintain, and update .
  - They may not accurately represent the behavior or functionality of the actual modules that they are simulating .
  - They may introduce new errors or inconsistencies in the testing process .
- An example of using Test Drivers and Test Stubs in software testing is shown in the following diagram:

```
+-----------------+     +-----------------+     +-----------------+
|  Module A       |     |  Module B       |     |  Module C       |
|  (Test Driver)  |     |  (Test Stub)    |     |  (Test Stub)    |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Input data     |     |  Output data    |     |  Output data    |
|  -------------> |     |  <------------- |     |  <------------- |
|                 |     |                 |     |                 |
|  Output data    |     |  Input data     |     |  Input data     |
|  <------------- |     |  -------------> |     |  -------------> |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

- A possible mnemonic or learning trick to remember the difference between Test Drivers and Test Stubs is:

  - Test Drivers **D**rive the modules under test from the **B**ottom-up.
  - Test Stubs **S**tub the modules under test from the **T**op-down.