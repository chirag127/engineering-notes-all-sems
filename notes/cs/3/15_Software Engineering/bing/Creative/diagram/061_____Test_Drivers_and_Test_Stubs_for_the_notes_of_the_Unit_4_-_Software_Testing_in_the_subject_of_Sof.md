### Test Drivers and Test Stubs

- Test drivers and test stubs are two types of **test harness**, which is a collection of software and test data that is configured together in order to test a unit of a program by stimulating various conditions while constantly monitoring its outputs and behavior.
- Test drivers and test stubs are used in **integration testing**, which is a level of software testing where individual units are combined and tested as a group to verify their functionality and interactions.
- Test drivers and test stubs are used to simulate the **missing or incomplete modules** in the software system, which are not yet developed or integrated.
- Test drivers and test stubs are used to **isolate** the module under test from the rest of the system, so that any errors or defects can be easily identified and traced.

#### Test Drivers

- A test driver is a piece of code that **emulates a calling function**. It is also known as a **dummy main function** that calls other modules to form a complete application .
- Test drivers are created in integration testing following a **bottom-up approach**, where the lower-level modules are tested and integrated first, and then the higher-level modules are tested and integrated later.
- Test drivers are used to **pass test cases** to the module under test and **receive test results** from it. They also **control the execution** of the test cases and **report the outcomes**.
- Test drivers are usually **written by the testers** or the developers of the module under test.

#### Test Stubs

- A test stub is a piece of code that **emulates a called function**. It is also known as a **dummy subprogram** that returns a predefined value or performs a simple action when called .
- Test stubs are created in integration testing following a **top-down approach**, where the higher-level modules are tested and integrated first, and then the lower-level modules are tested and integrated later.
- Test stubs are used to **replace the missing or incomplete modules** that are called by the module under test. They also **provide dummy data** or **simulate the behavior** of the missing modules.
- Test stubs are usually **written by the testers** or the developers of the calling module.