### Test Drivers and Test Stubs

- Test drivers and test stubs are two types of **test harness**, which is a collection of software and test data that is configured together in order to test a unit of a program by stimulating various conditions while constantly monitoring its outputs and behavior.
- Test drivers and test stubs are used in **integration testing**, which is a level of software testing where individual units are combined and tested as a group to verify their functionality and interactions.
- Test drivers and test stubs are created when some modules or components are not yet developed or available for testing, and they act as temporary substitutes for the missing modules or components.
- Test drivers and test stubs differ in their roles and approaches:

  - A **test driver** is a piece of code that **emulates a calling function**. It is used to **invoke** the module or component under test and **pass test cases** to it. It also **receives** the output from the module or component under test and **verifies** it against the expected results  .
  - A **test stub** is a piece of code that **emulates a called function**. It is used to **simulate** the module or component that is **called by** the module or component under test. It **returns** predefined or dummy data to the module or component under test, and may also **record** the input or output for later verification  .
  - A test driver is created in **bottom-up integration testing**, where the lower-level modules or components are tested first and then integrated with the higher-level modules or components. A test driver acts as a **dummy main function** that calls the lower-level modules or components and integrates them into a complete application  .
  - A test stub is created in **top-down integration testing**, where the higher-level modules or components are tested first and then integrated with the lower-level modules or components. A test stub acts as a **dummy sub-module** or **sub-component** that is called by the higher-level modules or components and provides them with the necessary data or functionality  .

- Test drivers and test stubs have the following advantages and disadvantages:

  - Advantages:
    - They **reduce** the dependency on the availability and development of other modules or components, and thus **speed up** the testing process .
    - They **isolate** the module or component under test from the errors or faults in other modules or components, and thus **improve** the reliability and accuracy of the testing results .
    - They **facilitate** the testing of different scenarios and conditions by providing predefined or dummy data or functionality .
  - Disadvantages:
    - They **increase** the complexity and cost of the testing process, as they require additional effort and resources to create, maintain, and update .
    - They **limit** the scope and coverage of the testing process, as they may not be able to simulate the real behavior and interactions of the missing modules or components .
    - They **introduce** the risk of inconsistency and incompatibility between the test drivers or test stubs and the actual modules or components, which may lead to errors or failures in the integration testing .

- The following diagram illustrates the use of test drivers and test stubs in integration testing:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Test Driver    |     |  Module A       |     |  Test Stub      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Invoke Module  |---->|  Call Module B  |---->|  Simulate       |
|  A and pass     |     |                 |     |  Module B       |
|  test cases     |     |                 |     |                 |
|                 |     |                 |     |                 |
|  Receive output |<----|  Return output  |<----|  Return dummy   |
|  from Module A  |     |  to Test

```
