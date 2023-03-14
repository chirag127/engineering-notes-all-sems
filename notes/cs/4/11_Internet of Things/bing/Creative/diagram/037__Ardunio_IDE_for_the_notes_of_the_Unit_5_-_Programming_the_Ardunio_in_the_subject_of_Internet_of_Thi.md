The Arduino IDE is an open-source software that allows you to write and upload code to Arduino boards. It consists of a text editor, a compiler, a serial monitor, and a library manager. The following diagram illustrates the basic architecture of the Arduino IDE:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Text Editor    |    |  Compiler       |    |  Serial Monitor |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Write code     |    |  Verify code    |    |  View output    |
|  (sketch)       |    |  (syntax check) |    |  (serial data)  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Save/Open      |    |  Upload         |    |  Connect/       |
|  (file)         |    |  (board)        |    |  Disconnect     |
|                 |    |                 |    |  (port)         |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Preferences    |    |  Board          |    |  Baud Rate      |
|  (settings)     |    |  (selection)    |    |  (speed)        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Examples       |    |  Library        |    |  Plotter        |
|  (built-in)     |    |  (manager)      |    |  (graph)        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```