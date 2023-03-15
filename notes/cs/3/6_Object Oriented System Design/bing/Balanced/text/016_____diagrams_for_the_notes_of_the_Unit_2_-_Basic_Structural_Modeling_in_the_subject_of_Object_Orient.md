### Diagrams for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- Basic structural modeling is the process of describing the static structure of a system using diagrams that represent the elements and the relationships between them.
- The Unified Modeling Language (UML) is a standard graphical notation for modeling object-oriented systems.
- UML defines four types of structural diagrams: class diagram, object diagram, component diagram, and deployment diagram.
- Class diagram is the most widely used structural diagram. It shows the classes, interfaces, and collaborations of a system, and the attributes, operations, and associations between them .
- Object diagram is a snapshot of the instances of the classes and their links at a specific point in time. It is used to illustrate a particular scenario or example of a system.
- Component diagram shows the physical components of a system, such as files, libraries, executables, and subsystems. It is used to model the implementation and deployment aspects of a system .
- Deployment diagram shows the configuration of the hardware and software elements that are used to run a system. It is used to model the distribution and communication of a system .
- The following are some examples of structural diagrams:

  - Class diagram:

    ```
    +-----------------+        +-----------------+
    |    Employee     |        |    Department   |
    +-----------------+        +-----------------+
    | -name: String   |        | -name: String   |
    | -salary: double |        | -budget: double |
    +-----------------+        +-----------------+
    | +getName():String|       | +getName():String|
    | +getSalary():double|     | +getBudget():double|
    | +setSalary(double):void| | +setBudget(double):void|
    +-----------------+        +-----------------+
             |                         |
             | worksIn                 |
             +-------------------------+
    ```

  - Object diagram:

    ```
    +-----------------+        +-----------------+
    |    Alice        |        |    Sales        |
    +-----------------+        +-----------------+
    | -name: "Alice"  |        | -name: "Sales"  |
    | -salary: 5000   |        | -budget: 100000 |
    +-----------------+        +-----------------+
             |                         |
             | worksIn                 |
             +-------------------------+
    ```

  - Component diagram:

    ```
    +-----------------+        +-----------------+
    |    Calculator   |        |    MathLib      |
    +-----------------+        +-----------------+
    | -input: String  |        | -PI: double     |
    | -output: double |        | -E: double      |
    +-----------------+        +-----------------+
    | +calculate():void|       | +sin(double):double|
    | +display():void  |       | +cos(double):double|
    +-----------------+        +-----------------+
             |                         |
             | uses                     |
             +-------------------------+
    ```

  - Deployment diagram:

    ```
    +-----------------+        +-----------------+
    |    Client       |        |    Server       |
    +-----------------+        +-----------------+
    | -OS: Windows 10 |        | -OS: Linux      |
    | -RAM: 8 GB      |        | -RAM: 16 GB     |
    +-----------------+        +-----------------+
    | +Calculator.exe |        | +MathLib.so     |
    +-----------------+        +-----------------+
             |                         |
             | requests                |
             +-------------------------+
    ```