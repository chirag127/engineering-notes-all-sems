Reverse engineering of software is the process of analyzing the software to determine its components and their relationships, and to recreate the original source code from the binary code . The process of reverse engineering is accomplished by making use of some tools that are categorized into debuggers or disassemblers, hex editors, monitoring and decompile tools. Reverse engineering can be performed from any stage of the product cycle, not necessarily from the functional end product.

### Reverse Engineering (RE) of Software

The following diagram shows a simplified overview of the reverse engineering process:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Binary Code    |    |  Disassembly    |    |  Decompilation  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
       V                      V                      V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Debugging      |    |  Hex Editing    |    |  Monitoring     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
       V                      V                      V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Source Code    |    |  Design         |    |  Documentation  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```