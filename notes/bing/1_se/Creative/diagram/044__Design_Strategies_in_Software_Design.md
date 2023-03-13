Design strategies in software design are methods or approaches to solve software design problems. They help in defining the structure, behavior, and interactions of software components. Some of the common design strategies in software design are:

- Structured design: This is a conceptualization of problems into several well-organized elements of solutions. It is mainly concerned about the solution design. It uses a top-down approach to decompose the problem into smaller and simpler subproblems. It focuses on the functional aspects of the software and ignores the data aspects. It uses graphical tools such as data flow diagrams and structure charts to represent the software design.
- Function-oriented design: This is one of the classical methods of software design, where decomposition centers on identifying the major software functions and then elaborating and refining them in a top-down manner. It also considers the data aspects of the software and uses data dictionaries and entity-relationship diagrams to model the data. It uses functional abstraction and information hiding to achieve modularity and reusability. It follows the principle of stepwise refinement to design the software.
- Object-oriented design: This is a modern method of software design, where decomposition centers on identifying the major software objects and then defining their attributes and behaviors. It uses a bottom-up approach to combine the objects into larger and more complex systems. It focuses on the data aspects of the software and encapsulates the data and the functions that operate on them into a single unit called an object. It uses graphical tools such as class diagrams and sequence diagrams to represent the software design.

The following diagram illustrates the basic architecture of a software system using each of these design strategies:

```
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|   Structured      |      |  Function-        |      |  Object-          |
|   Design          |      |  Oriented         |      |  Oriented         |
|                   |      |  Design           |      |  Design           |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|  +-------------+  |      |  +-------------+  |      |  +-------------+  |
|  |   Module 1  |  |      |  |   Function 1 |  |      |  |   Object 1  |  |
|  +-------------+  |      |  +-------------+  |      |  +-------------+  |
|        |          |      |        |          |      |        |          |
|        v          |      |        v          |      |        v          |
|  +-------------+  |      |  +-------------+  |      |  +-------------+  |
|  |   Module 2  |  |      |  |   Function 2 |  |      |  |   Object 2  |  |
|  +-------------+  |      |  +-------------+  |      |  +-------------+  |
|        |          |      |        |          |      |        |          |
|        v          |      |        v          |      |        v          |
|  +-------------+  |      |  +-------------+  |      |  +-------------+  |
|  |   Module 3  |  |      |  |   Function 3 |  |      |  |   Object 3  |  |
|  +-------------+  |      |  +-------------+  |      |  +-------------+  |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
```