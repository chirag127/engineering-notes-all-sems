#### Test Drivers and Test Stubs software testing strategy

- Test Drivers and Test Stubs are two types of test harness, which is a collection of software and test data that is configured together in order to test a unit of a program by stimulating various conditions while constantly monitoring its outputs and behavior.
- Test Drivers and Test Stubs are used when some modules of the software are not available or developed yet, but are still needed for testing the functionality and integration of other modules.
- Test Drivers and Test Stubs simulate the behavior and interface of the missing modules, and provide inputs and outputs for the modules under test.
- Test Drivers and Test Stubs are used in different approaches of incremental testing, which is a testing strategy that involves testing the software in small parts or increments, and integrating them gradually until the whole system is tested.
- Test Stubs are used in top-down testing approach, which is a testing strategy that involves testing the software from the higher-level modules to the lower-level modules, following the control flow or hierarchy of the software .
- Test Stubs are also known as "called programs", which are the programs that are invoked or called by the modules under test.
- Test Stubs act as temporary replacements for the lower-level modules that are not available or developed yet, and provide predefined outputs or responses for the modules under test .
- Test Stubs can be classified into four basic types based on their functionality:
  - Trace message stubs: These stubs display a trace message that is used by the modules under test.
  - Parameter value stubs: These stubs display the parameter values that are used by the modules under test.
  - Return value stubs: These stubs return the values that are used by the modules under test.
  - Parameter-selected return value stubs: These stubs return values that are selected by the parameters that are used by the modules under test.
- Test Drivers are used in bottom-up testing approach, which is a testing strategy that involves testing the software from the lower-level modules to the higher-level modules, following the dependency or functionality of the software .
- Test Drivers are also known as "calling programs", which are the programs that invoke or call the modules under test.
- Test Drivers act as temporary replacements for the higher-level modules that are not available or developed yet, and provide inputs or stimuli for the modules under test .
- Test Drivers are more complex than Test Stubs, as they have to handle multiple inputs and outputs, and also coordinate the testing of several modules at once.
- Test Drivers can also be used when some lower-level modules are missing, by calling the available lower-level modules and the Test Stubs for the missing ones.