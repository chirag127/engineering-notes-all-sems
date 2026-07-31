#### Test Drivers and Test Stubs software testing strategy

Test drivers and test stubs are two types of test harnesses, which are collections of software and test data that are configured together in order to test a unit of a program by stimulating various conditions while constantly monitoring its outputs and behavior.

Test drivers are used in bottom-up testing approach, when the lower-level modules are ready to test, but the higher-level modules are still not ready yet. These dummy pieces of code are the test drivers, which simulate the calling programs and provide inputs to the lower-level modules .

Test stubs are used in top-down testing approach, when the higher-level modules are ready to test, but the lower-level modules are still not ready yet. These dummy pieces of code are the test stubs, which simulate the called programs and provide outputs to the higher-level modules .

A possible ASCII diagram for test drivers and test stubs software testing strategy is:

```
+-----------------+     +-----------------+     +-----------------+
| Higher-level    |     | Higher-level    |     | Higher-level    |
| module          |     | module          |     | module          |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
+-----------------+     +-----------------+     +-----------------+
| Test stub       |     | Test stub       |     | Test stub       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
+-----------------+     +-----------------+     +-----------------+
| Lower-level     |     | Lower-level     |     | Lower-level     |
| module          |     | module          |     | module          |
+-----------------+     +-----------------+     +-----------------+
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
+-----------------+     +-----------------+     +-----------------+
| Test driver     |     | Test driver     |     | Test driver     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The test drivers are at the bottom of the diagram, and they provide inputs to the lower-level modules. The test stubs are at the top of the diagram, and they provide outputs to the higher-level modules. The higher-level and lower-level modules are the actual units of the program that are being tested. The test drivers and test stubs are connected by vertical lines, which represent the data flow between them. The test drivers and test stubs are used to isolate the modules from each other and test them independently.