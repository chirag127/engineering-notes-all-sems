#### Test Drivers and Test Stubs software testing strategy

Test drivers and test stubs are two types of test harness, which is a collection of software and test that is configured together in order to test a unit of a program by stimulating variety of conditions while constantly monitoring its outputs and behaviour.

Test drivers are the ones, which are the “calling” programs. Drivers are used in bottom up testing approach, when one has the sub modules ready to test, but the main module is still not ready yet. These dummy pieces of code are the drivers .

Test stubs are used in top down testing approach, when one has the major module ready to test, but the sub modules are still not ready yet. These dummy pieces of code are the stubs .

A possible ASCII diagram for the test drivers and test stubs software testing strategy is:

```
    +-------------------+        +-------------------+
    | Main Module       |        | Sub Module 1      |
    |                   |        |                   |
    |                   |        |                   |
    |                   |        |                   |
    +-------------------+        +-------------------+
            |                           ^
            |                           |
            |                           |
            |                           |
            |                           |
            v                           |
    +-------------------+        +-------------------+
    | Test Driver       |        | Test Stub         |
    |                   |        |                   |
    |                   |        |                   |
    |                   |        |                   |
    +-------------------+        +-------------------+
            |                           ^
            |                           |
            |                           |
            |                           |
            |                           |
            v                           |
    +-------------------+        +-------------------+
    | Test Case         |        | Test Case         |
    |                   |        |                   |
    |                   |        |                   |
    |                   |        |                   |
    +-------------------+        +-------------------+
```

The test driver simulates the main module and calls the sub module 1, which is the unit under test. The test stub simulates the sub module 2, which is not yet available, and provides the expected output to the main module. The test cases are the inputs and expected outputs for each unit. The test harness monitors the actual outputs and compares them with the expected outputs to verify the correctness of the units  .