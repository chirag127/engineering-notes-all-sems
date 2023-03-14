## Unit 6 - Use case 1

- Use case 1 is a scenario that describes how a system or a software interacts with one or more actors to achieve a specific goal.
- An actor is a person, a device, or another system that has a role in the interaction with the system or the software.
- A goal is a desired outcome or a benefit that the actor wants to obtain from the system or the software.
- A use case 1 diagram is a graphical representation of the use cases and the actors involved in a system or a software.
- A use case 1 diagram consists of the following elements:
  - A system boundary, which is a rectangle that encloses the use cases and represents the scope of the system or the software.
  - Use cases, which are ovals that represent the goals that the actors want to achieve from the system or the software.
  - Actors, which are stick figures that represent the roles of the external entities that interact with the system or the software.
  - Associations, which are lines that connect the actors and the use cases and indicate the communication or the participation between them.
  - Generalizations, which are lines with an empty triangle at one end that indicate a hierarchical relationship between actors or use cases, where the child inherits the properties and the behavior of the parent.
  - Include relationships, which are dashed lines with an open arrowhead at one end that indicate that a use case is a part of another use case or is always executed when the other use case is executed.
  - Extend relationships, which are dashed lines with an open arrowhead at one end that indicate that a use case is an optional or a conditional extension of another use case or is executed only under certain circumstances when the other use case is executed.

- An example of a use case 1 diagram for a library management system is shown below:

```
+-----------------------------+
| Library Management System   |
|                             |
|  +----------------------+   |
|  | Borrow Book         |<--+---+
|  +----------------------+   |   |
|                             |   |
|  +----------------------+   |   |
|  | Return Book         |<--+---+
|  +----------------------+   |   |
|                             |   |
|  +----------------------+   |   |
|  | Renew Book          |<--+---+
|  +----------------------+   |   |
|                             |   |
|  +----------------------+   |   |
|  | Search Book         |<--+---+
|  +----------------------+   |   |
|                             |   |
|  +----------------------+   |   |
|  | Reserve Book        |<--+---+
|  +----------------------+   |   |
|                             |   |
|  +----------------------+   |   |
|  | Pay Fine            |<--+---+
|  +----------------------+   |   |
|                             |   |
|  +----------------------+   |   |
|  | Manage Book         |<--+---+
|  +----------------------+   |   |
|                             |   |
|  +----------------------+   |   |
|  | Manage Member       |<--+---+
|  +----------------------+   |   |
|                             |   |
|  +----------------------+   |   |
|  | Generate Report     |<--+---+
|  +----------------------+   |   |
+-----------------------------+   |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
+-----------------+               |
| Librarian       |               |
+-----------------+               |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
+-----------------+               |
| Member          |               |
+-----------------+               |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
+-----------------+               |
| Guest           |               |
+-----------------+               |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |