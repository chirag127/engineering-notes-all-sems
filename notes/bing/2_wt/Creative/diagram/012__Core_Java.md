Core Java is the basic and core part of the Java programming language that is used for creating or developing a general-purpose application. Core Java architecture consists of three main components: JVM, JRE, and JDK.

### Core Java

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|      JDK        |      |      JRE        |      |      JVM        |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Java Compiler  |      |  Java Libraries |      |  Class Loader   |
|                 |      |                 |      |                 |
|  Java Debugger  |      |  Java Runtime   |      |  Runtime Memory |
|                 |      |  Environment    |      |                 |
|  Java Tools     |      |                 |      |  Execution      |
|                 |      |                 |      |  Engine         |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Java Source    |      |  Java Bytecode  |      |  Machine Code   |
|  Code (.java)   |----->|  (.class)       |----->|  (.exe)         |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

JDK stands for Java Development Kit. It is a software development environment that contains the Java compiler, debugger, tools, and libraries. It is used to create Java applications and applets.

JRE stands for Java Runtime Environment. It is a software package that contains the Java libraries, the Java runtime, and other components that are required to run Java applications. It is a subset of JDK.

JVM stands for Java Virtual Machine. It is a software component that converts the Java bytecode into machine code and executes it on the underlying hardware. It provides platform independence and memory management for Java applications. It consists of a class loader, a runtime memory area, and an execution engine.