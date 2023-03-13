Test Drivers and Test Stubs are two types of test harnesses that are used to facilitate the integration testing of software modules. Test Drivers are programs that call the module to be tested and provide the input data, while Test Stubs are programs that are called by the module to be tested and provide the output data. Test Drivers are used in Bottom-up integration testing, where the lower level modules are tested first and then used to test the higher level modules. Test Stubs are used in Top-down integration testing, where the higher level modules are tested first and then the lower level modules are simulated by the Stubs.

The following diagram illustrates the basic architecture of a Test Driver and a Test Stub in software testing strategy:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Test Driver   |    |  Module Under  |    |  Test Stub     |
|                |    |  Test (MUT)    |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Input Data    |    |  Input Data    |    |  Output Data   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Output Data   |    |  Output Data   |    |  Input Data    |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Test Results  |    |  Test Results  |    |  Test Results  |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```