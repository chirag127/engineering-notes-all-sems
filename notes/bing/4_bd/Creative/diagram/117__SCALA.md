Scala is a general-purpose programming language that supports multiple paradigms, such as object-oriented, functional, concurrent, and reactive programming. Scala runs on the Java Virtual Machine (JVM) and interoperates with Java code and libraries.

The architecture of Scala is based on the following principles:

- Scala is designed to be expressive and concise, allowing programmers to write less code and achieve more functionality.
- Scala is statically typed, meaning that the types of variables and expressions are checked at compile time, preventing many runtime errors and improving performance.
- Scala is extensible, meaning that programmers can define new types, operators, and syntax using features such as implicit conversions, type classes, and macros.
- Scala is scalable, meaning that it can handle both small and large programs, from scripting to enterprise applications, using features such as traits, pattern matching, and futures.

The following diagram illustrates the basic architecture of a Scala program:

### SCALA

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Scala Code    | -> |   Scala Compiler  | -> |   Scala Library  |
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
       v                      v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Java Code     | -> |   Java Compiler  | -> |   Java Library  |
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
       v                      v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Bytecode      | -> |   JVM           | -> |   OS            |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram shows that Scala code is first compiled by the Scala compiler into Java code, which is then compiled by the Java compiler into bytecode, which is then executed by the JVM on the operating system. The Scala library provides a rich set of data structures and functions that are compatible with the Java library. The Scala compiler and library are themselves written in Scala, demonstrating the expressiveness and scalability of the language.