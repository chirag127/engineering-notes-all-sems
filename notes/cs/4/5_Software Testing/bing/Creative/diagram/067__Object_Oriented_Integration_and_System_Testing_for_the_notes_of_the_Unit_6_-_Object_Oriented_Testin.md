Object Oriented Integration and System Testing is a process of testing software systems that are developed using object-oriented paradigms, such as encapsulation, inheritance, polymorphism, etc. It involves testing the individual components or classes, as well as the interactions and interfaces between them. It also verifies that the system meets the functional and non-functional requirements of the user. 

The following diagram illustrates the basic architecture of an object-oriented system and the levels of testing that can be applied to it:

```
+---------------------+      +---------------------+      +---------------------+
|                     |      |                     |      |                     |
|    System Testing   |<---->|  Subsystem Testing  |<---->|    Unit Testing     |
|                     |      |                     |      |                     |
+---------------------+      +---------------------+      +---------------------+
|                     |      |                     |      |                     |
|   Test the system   |      | Test the subsystems |      | Test the components |
|   as a whole,       |      | or groups of        |      | or classes,         |
|   including the     |      | components,         |      | including the       |
|   functional and    |      | including the       |      | methods,            |
|   non-functional    |      | interfaces and      |      | attributes,         |
|   requirements.     |      | interactions        |      | constructors,       |
|                     |      | between them.       |      | and destructors.    |
|                     |      |                     |      |                     |
+---------------------+      +---------------------+      +---------------------+
|                     |      |                     |      |                     |
|   System Under Test |      |  Subsystem Under    |      |  Component Under    |
|                     |      |       Test          |      |       Test          |
|                     |      |                     |      |                     |
+---------------------+      +---------------------+      +---------------------+
|                     |      |                     |      |                     |
|    +---------+      |      |    +---------+      |      |    +---------+      |
|    |         |      |      |    |         |      |      |    |         |      |
|    |  Class  |      |      |    |  Class  |      |      |    |  Class  |      |
|    |         |      |      |    |         |      |      |    |         |      |
|    +----+----+      |      |    +----+----+      |      |    +----+----+      |
|         |           |      |         |           |      |         |           |
|         |           |      |         |           |      |         |           |
|         |           |      |         |           |      |         |           |
|    +----+----+      |      |    +----+----+      |      |    +----+----+      |
|    |         |      |      |    |         |      |      |    |         |      |
|    |  Class  |      |      |    |  Class  |      |      |    |  Class  |      |
|    |         |      |      |    |         |      |      |    |         |      |
|    +----+----+      |      |    +----+----+      |      |    +----+----+      |
|         |           |      |         |           |      |         |           |
|         |           |      |         |           |      |         |           |
|         |           |      |         |           |      |         |           |
|    +----+----+      |      |    +----+----+      |      |    +----+----+      |
|    |         |      |      |    |         |      |      |    |         |      |
|    |  Class  |      |      |    |  Class  |      |      |    |  Class  |      |
|    |         |      |      |    |         |      |      |    |         |      |
|    +---------+      |      |    +---------+      |      |    +---------+      |
|                     |      |                     |      |                     |
+---------------------+      +---------------------+      +---------------------+
```