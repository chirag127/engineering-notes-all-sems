### Diagrams for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- Basic structural modeling is the process of describing the static structure of a system using diagrams that show the classes, objects, components, and deployment of the system elements .
- UML (Unified Modeling Language) is a standard notation for creating these diagrams.
- UML structural diagrams are categorized as follows:
  - Class diagram: models the static view of a system, showing the classes, interfaces, and collaborations of a system, and the relationships between them .
  - Object diagram: models the static view of a system at a specific point in time, showing the instances of classes and their values and links.
  - Component diagram: models the physical components of a system, such as software modules, libraries, files, and executables, and the dependencies between them .
  - Deployment diagram: models the physical deployment of a system, such as nodes, devices, processors, and communication links, and the allocation of components to them .
- The following are some examples of UML structural diagrams  :

  - Class diagram:

  ```
  +-----------------+        +-----------------+
  |     Student     |        |     Course      |
  +-----------------+        +-----------------+
  | -name: String   |        | -title: String  |
  | -id: int        |        | -credits: int   |
  +-----------------+        +-----------------+
  | +getName():String|       | +getTitle():String|
  | +getId():int    |       | +getCredits():int|
  +-----------------+        +-----------------+
         |  *                       *  |
         |                           |
         +---------------------------+
                   enrolled
  ```

  - Object diagram:

  ```
  +-----------------+        +-----------------+
  |     Alice       |        |     CS101       |
  +-----------------+        +-----------------+
  | -name: "Alice"  |        | -title: "CS101" |
  | -id: 123        |        | -credits: 3     |
  +-----------------+        +-----------------+
         |                           |
         +---------------------------+
                   enrolled
  +-----------------+        +-----------------+
  |     Bob         |        |     CS102       |
  +-----------------+        +-----------------+
  | -name: "Bob"    |        | -title: "CS102" |
  | -id: 456        |        | -credits: 4     |
  +-----------------+        +-----------------+
         |                           |
         +---------------------------+
                   enrolled
  ```

  - Component diagram:

  ```
  +-----------------+        +-----------------+
  |   Calculator    |        |     MathLib     |
  +-----------------+        +-----------------+
  | -result: double |        | -PI: double     |
  +-----------------+        +-----------------+
  | +add(x,y):void  |        | +sin(x):double  |
  | +sub(x,y):void  |        | +cos(x):double  |
  | +mul(x,y):void  |        | +tan(x):double  |
  | +div(x,y):void  |        | +sqrt(x):double |
  | +getResult():double|     +-----------------+
  +-----------------+
         |  *
         |
         +---------------------------+
                   uses
  ```

  - Deployment diagram:

  ```
  +-----------------+        +-----------------+
  |     Server      |        |     Client      |
  +-----------------+        +-----------------+
  | -OS: Linux      |        | -OS: Windows    |
  | -RAM: 16GB      |        | -RAM: 8GB       |
  | -CPU: 4 cores   |        | -CPU: 2 cores   |
  +-----------------+        +-----------------+
  | +Calculator     |        | +GUI            |
  +-----------------+        +-----------------+
         |                           |
         +---------------------------+
                   TCP/IP
  ```