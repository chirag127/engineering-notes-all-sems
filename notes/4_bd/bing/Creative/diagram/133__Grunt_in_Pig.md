Grunt is a shell of Apache Pig that is mainly used to write Pig Latin scripts. It can also invoke shell commands using sh and fs. Grunt can be run in three modes: interactive, batch and embedded. In interactive mode, Grunt reads commands from the console and executes them. In batch mode, Grunt reads commands from a file and executes them. In embedded mode, Grunt is invoked from Java and runs commands from a string or an input stream.

The following diagram illustrates the basic architecture of Grunt in Pig:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Interactive    |    |     Batch       |    |    Embedded     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         v                    v                       v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Grunt       |    |     Grunt       |    |     Grunt       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         |                    |                       |
         v                    v                       v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Pig Latin    |    |    Pig Latin    |    |    Pig Latin    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```