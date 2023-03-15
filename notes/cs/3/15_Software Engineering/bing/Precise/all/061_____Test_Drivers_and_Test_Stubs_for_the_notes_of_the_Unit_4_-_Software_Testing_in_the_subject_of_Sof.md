# Test Drivers and Test Stubs

Test drivers and test stubs are two types of test harness components used in software testing. They are used to facilitate the testing of software modules in isolation, by simulating the behavior of the modules that are not yet integrated or not available for testing.

## Test Drivers

A test driver is a program that sets up and calls the module or component under test. It provides the necessary inputs to the module, invokes the module's functionality, and captures the outputs produced by the module. The test driver then compares the actual outputs with the expected outputs to determine if the module is functioning correctly.

Test drivers are commonly used in bottom-up integration testing, where the lower-level modules are tested first, and the higher-level modules are tested later. In this approach, the test driver simulates the behavior of the higher-level modules that call the module under test.

## Test Stubs

A test stub is a program that simulates the behavior of a module that is not yet integrated or not available for testing. It receives the inputs from the module under test, and returns pre-determined outputs to the module.

Test stubs are commonly used in top-down integration testing, where the higher-level modules are tested first, and the lower-level modules are tested later. In this approach, the test stub simulates the behavior of the lower-level modules that are called by the module under test.

In summary, test drivers and test stubs are used to facilitate the testing of software modules in isolation, by simulating the behavior of the modules that are not yet integrated or not available for testing. Test drivers are used to set up and call the module under test, while test stubs are used to simulate the behavior of the modules that are called by the module under test.