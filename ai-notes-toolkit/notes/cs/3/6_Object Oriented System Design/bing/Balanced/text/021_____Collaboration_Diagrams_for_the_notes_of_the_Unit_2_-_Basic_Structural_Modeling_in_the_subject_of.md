### Collaboration Diagrams

- Collaboration diagrams are used to show the **relationship** between the **objects** in a system.
- Collaboration diagrams are also known as **communication diagrams** in UML 2.x.
- Collaboration diagrams are similar to **sequence diagrams**, but they focus more on the **structure** of the objects rather than the **order** of the messages.
- Collaboration diagrams can be used to model the **collaborations**, **mechanisms** or the **structural organization** within a system design.
- Collaboration diagrams consist of four major components:
  - **Objects**: Objects are shown as rectangles with naming labels inside. The naming label follows the convention of object name : class name. Objects can also have **attributes** and **operations** shown in separate compartments within the rectangle.
  - **Actors**: Actors are instances that invoke the interaction in the diagram. Each actor has a name and a role, with one actor initiating the interaction. Actors are shown as **stick figures** or **rectangles** with the stereotype <<actor>>.
  - **Links**: Links are solid lines that connect objects and actors. They represent the **association** or the **communication path** between them. Links can have **multiplicity**, **roles** and **constraints** shown as labels along the line.
  - **Messages**: Messages are the information or data that is exchanged between the objects and actors. Messages are shown as **arrows** along the links, with the arrowhead indicating the direction of the message. Messages can have **sequence numbers**, **names**, **arguments** and **return values** shown as labels above or below the arrow.

- Collaboration diagrams can be created by following these steps:
  - Identify the design elements required to implement the functionality of the system or a use case.
  - Draw the objects and actors involved in the interaction as rectangles and stick figures respectively.
  - Connect the objects and actors with links to show their relationships and communication paths.
  - Add messages along the links to show the information flow and the sequence of events.
  - Add attributes, operations, roles, constraints and other details as needed to clarify the diagram.

- Collaboration diagrams can be used to show the following aspects of a system:
  - The **static structure** of the objects and their associations.
  - The **dynamic behavior** of the objects and their interactions.
  - The **alternative scenarios** and **conditional flows** of the interaction.
  - The **concurrency** and **synchronization** of the messages.
  - The **distribution** and **deployment** of the objects across different nodes or devices.