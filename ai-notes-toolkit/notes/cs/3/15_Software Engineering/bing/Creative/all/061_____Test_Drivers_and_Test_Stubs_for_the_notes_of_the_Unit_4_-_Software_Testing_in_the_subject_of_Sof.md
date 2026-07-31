# Test Drivers and Test Stubs

- Test drivers and test stubs are two types of test harnesses, which are collections of software and test data that are configured together in order to test a unit of a program by stimulating various conditions while constantly monitoring its outputs and behavior.
- Test drivers and test stubs are used in integration testing, which is a type of testing that aims to verify the functionality, performance, and reliability of different modules or components of a software system when they are combined together.
- Test drivers and test stubs are especially useful when some modules or components are not yet developed or available, or when they are too complex or costly to use in the testing environment.
- Test drivers and test stubs can simulate the features and functionalities of the missing or unavailable modules or components, and provide inputs and outputs to the modules or components under test.
- Test drivers and test stubs can also help to isolate the modules or components under test from the rest of the system, and reduce the dependencies and interactions among them.
- Test drivers and test stubs can improve the efficiency, effectiveness, and coverage of integration testing, and facilitate the detection and correction of errors and defects in the software system.

## Test Drivers
- A test driver is a piece of code that emulates a calling function or a main function that invokes the module or component under test .
- A test driver is created in integration testing following a bottom-up approach, which is a strategy that starts with testing the lowest-level or the most basic modules or components, and then gradually integrates and tests the higher-level or the more complex ones .
- A test driver provides inputs or test cases to the module or component under test, and receives and verifies the outputs or results from it .
- A test driver can also monitor and record the behavior and performance of the module or component under test, and report any errors or defects that are found .
- A test driver can be replaced by the actual calling function or the main function once the integration testing is completed and the software system is ready for operation .

## Test Stubs
- A test stub is a piece of code that emulates a called function or a subordinate function that is invoked by the module or component under test .
- A test stub is created in integration testing following a top-down approach, which is a strategy that starts with testing the highest-level or the most complex modules or components, and then gradually integrates and tests the lower-level or the more basic ones .
- A test stub receives inputs or requests from the module or component under test, and provides outputs or responses to it .
- A test stub can also simulate the behavior and performance of the called function or the subordinate function, and generate expected or unexpected outputs or results .
- A test stub can be replaced by the actual called function or the subordinate function once the integration testing is completed and the software system is ready for operation .

: https://softwaretester.net/articles/stubs-and-drivers-in-software-testing/
: https://www.professionalqa.com/stubs-and-drivers
: https://www.linkedin.com/pulse/what-difference-between-stubs-drivers-software-shormistha-chatterjee
: https://www.geeksforgeeks.org/difference-between-stubs-and-drivers/