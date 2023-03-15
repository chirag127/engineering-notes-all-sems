### Component Diagram for the Notes of the Unit 1 - Introduction of Software Engineering Lab

- A component diagram is a type of UML diagram that shows the physical components and dependencies of a software system  .
- A component can be a software module, a hardware device, a business unit, or any other entity that has a well-defined interface and functionality  .
- A component diagram can be used to verify that the system's required functionality is acceptable, to communicate the system's architecture to the stakeholders, and to construct executable systems through forward and reverse engineering .
- A component diagram consists of the following elements:
  - Component: A rectangle with two small rectangles on the left side, representing the component's interface and implementation. The component's name is written inside the rectangle, optionally preceded by a stereotype such as <<database>>, <<web service>>, <<user interface>>, etc. A component can have ports, which are small squares on the component's boundary, representing the points of interaction with other components .
  - Interface: A circle or a lollipop, representing the set of operations or services that a component provides or requires. An interface can have a name and a stereotype, such as <<service>>, <<facade>>, <<API>>, etc. An interface can be attached to a component by a dashed line, indicating that the component provides or requires the interface .
  - Dependency: A dashed arrow with an open arrowhead, representing the relationship between two components or interfaces that indicates that one component or interface depends on the other for its specification or implementation. A dependency can have a name and a stereotype, such as <<use>>, <<call>>, <<instantiate>>, etc .
  - Association: A solid line with an optional arrowhead, representing the relationship between two components or interfaces that indicates that they are connected or communicate with each other. An association can have a name, a stereotype, a multiplicity, and a role for each end .
  - Delegation: A dashed line with a closed arrowhead, representing the relationship between a component and a port that indicates that the component delegates the requests received by the port to another component or interface. A delegation can have a name and a stereotype, such as <<delegate>>, <<forward>>, <<route>>, etc .
  - Generalization: A solid line with a closed arrowhead, representing the inheritance relationship between two components or interfaces that indicates that one component or interface is a specialized version of the other. A generalization can have a name and a stereotype, such as <<extend>>, <<implement>>, <<realize>>, etc .

- An example of a component diagram for the notes of the unit 1 - introduction of software engineering lab is shown below. The diagram shows the components and interfaces involved in creating, storing, and accessing the notes, as well as their dependencies and associations.

```text
+-----------------+       +-----------------+       +-----------------+
| <<web service>> |       | <<database>>    |       | <<user>>        |
| Notes Service   |       | Notes DB        |       | Student         |
+-----------------+       +-----------------+       +-----------------+
| +createNote()   |       | +insertNote()   |       | +viewNote()     |
| +updateNote()   |       | +updateNote()   |       | +editNote()     |
| +deleteNote()   |       | +deleteNote()   |       | +deleteNote()   |
| +getNote()      |       | +selectNote()   |       +-----------------+
+-----------------+       +-----------------+
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
+-----------------+       +-----------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-----------------+       +-----------------+
| <<web service>> |       | <<web service>> |
| Notes API       |       | Notes UI