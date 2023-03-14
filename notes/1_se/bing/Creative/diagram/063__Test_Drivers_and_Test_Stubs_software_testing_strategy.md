Test Drivers and Test Stubs are software testing techniques that are used to simulate the behavior of missing or incomplete modules in a system. They are often used in incremental testing approaches, such as top-down testing and bottom-up testing, to facilitate the integration of different modules and test their functionality.

A Test Driver is a program that calls and executes the module under test. It is used when the higher-level modules are not available or developed yet, and the lower-level modules need to be tested. A Test Driver provides the input data and parameters for the module under test, and displays or verifies the output results.

A Test Stub is a program that simulates the behavior of a module that is called by the module under test. It is used when the lower-level modules are not available or developed yet, and the higher-level modules need to be tested. A Test Stub accepts the input data and parameters from the module under test, and returns the expected output results.

The following diagram illustrates the basic architecture of a Test Driver and a Test Stub in a software testing scenario:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Test Driver    |        |  Module under   |        |  Test Stub      |
|                 |        |  test           |        |                 |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Input data     |------->|  Input data     |------->|  Input data     |
|  and parameters |        |  and parameters |        |  and parameters |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Output results |<-------|  Output results |<-------|  Output results |
|  and verification|       |                 |        |                 |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```