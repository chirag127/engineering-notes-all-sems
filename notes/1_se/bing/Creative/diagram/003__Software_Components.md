A software component diagram is a type of UML diagram that shows the organization and dependencies of the components in a software system. A component can be a software module, a hardware device, a business unit, or any other entity that provides or requires some functionality. A component diagram can help you visualize the structure and behavior of your system at a high level.

To draw a software component diagram, you need to identify the components and interfaces in your system, and how they are connected by assembly connectors or delegation connectors. You can use different symbols to represent the components and interfaces, such as rectangles, circles, semi-circles, ports, and arrows. You can also use stereotypes to indicate the type or role of a component, such as <<database>>, <<web server>>, <<user interface>>, etc.

The following diagram illustrates the basic architecture of a web application that uses a database, a web server, and a user interface component. The diagram shows how the components are wired together by interfaces and connectors, and how the user interface component delegates some of its interfaces to an internal class.

### Software Components

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Database      |       |   Web Server    |       |   User Interface|
|                 |       |                 |       |                 |
|  <<component>>  |       |  <<component>>  |       |  <<component>>  |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  +-----------+  |       |  +-----------+  |       |  +-----------+  |
|  |           |  |       |  |           |  |       |  |           |  |
|  |  Data     |  |       |  |  Service  |  |       |  |  View     |  |
|  |           |  |       |  |           |  |       |  |           |  |
|  |  <<db>>   |  |       |  |  <<ws>>   |  |       |  |  <<ui>>   |  |
|  +-----------+  |       |  +-----------+  |       |  +-----------+  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  +-----------+  |       |  +-----------+  |       |  +-----------+  |
|  |           |  |       |  |           |  |       |  |           |  |
|  |  Query    |  |       |  |  Request  |  |       |  |  Display  |  |
|  |           |  |       |  |           |  |       |  |           |  |
|  |  <<db>>   |  |       |  |  <<ws>>   |  |       |  |  <<ui>>   |  |
|  +-----------+  |       |  +-----------+  |       |  +-----------+  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  +-----------+  |       |  +-----------+  |       |  +-----------+  |
|  |           |  |       |  |           |  |       |  |           |  |
|  |  Update   |  |       |  |  Response |  |       |  |  Input    |  |
|  |           |  |       |  |           |  |       |  |           |  |
|  |  <<db>>   |  |       |  |  <<ws>>   |  |       |  |  <<ui>>   |  |
|  +-----------+  |       |  +-----------+  |       |  +-----------+  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  +-----------+  |       |  +-----------+  |       |  +-----------+  |
|  |           |  |       |  |           |  |       |  |           |  |
|  |