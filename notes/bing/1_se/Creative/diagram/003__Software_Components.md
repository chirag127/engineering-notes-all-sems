A software component diagram is a type of UML diagram that shows the structure and dependencies of the components of a software system. A component is a modular unit that provides a specific functionality or a set of functionalities. A component can be a software module, a library, a framework, a hardware device, or a business unit.

A software component diagram consists of the following elements:

- Components: Represented by rectangles with two small rectangles on the left side. The name of the component is written inside the rectangle. Optionally, the component can have a stereotype, such as <<database>>, <<web service>>, <<user interface>>, etc. to indicate its type or role.
- Interfaces: Represented by circles or lollipops. They show the services that a component provides or requires. The name of the interface is written next to the circle. Optionally, the interface can have a stereotype, such as <<SOAP>>, <<REST>>, <<JDBC>>, etc. to indicate its protocol or technology.
- Dependencies: Represented by dashed arrows with an open arrowhead. They show the relationships between components or interfaces. The arrow points from the dependent element to the independent element. Optionally, the dependency can have a stereotype, such as <<use>>, <<call>>, <<create>>, etc. to indicate its nature or purpose.

### Software Components

The following is an example of a software component diagram for an online shopping system. It shows the components and interfaces of the system, as well as their dependencies.

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Web Browser   |       |  Web Server    |       |  Database      |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
| <<user         |       | <<web          |       | <<database     |
| interface>>    |       | service>>      |       | >>             |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  HTTP         |       |  HTTP          |       |  SQL           |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
| <<REST>>       |       | <<REST>>       |       | <<JDBC>>       |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Product       |       |  Product       |       |  Product       |
|  Catalog       |       |  Catalog       |       |  Catalog       |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
| <<use>>        |       | <<use>>        |       | <<use>>        |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |