# Use cases for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- A use case is an abstraction of interrelated events or interaction sequences that describe what a system does from the user perspective .
- A use case model shows a view of the system functionality and the actors who interact with it .
- A use case diagram is a visual representation of a use case model using UML notation .
- A use case diagram consists of the following elements:
  - Actors: external entities that interact with the system, such as users, other systems, or devices. Actors are represented by stick figures or icons.
  - Use cases: the functionality that the system provides to the actors, such as login, search, or checkout. Use cases are represented by ovals with names inside.
  - Associations: the relationships between actors and use cases, indicating who can initiate or participate in a use case. Associations are represented by solid lines.
  - System boundary: an optional rectangle that encloses the use cases and represents the scope of the system. The system boundary is labeled with the system name.
  - Packages: optional compartments that group related use cases or actors. Packages are represented by dashed rectangles with names on top.
  - Generalization: a relationship between actors or use cases that indicates inheritance or specialization. Generalization is represented by a solid line with a hollow triangle pointing to the parent actor or use case.
  - Include: a relationship between use cases that indicates one use case is always performed as part of another use case. Include is represented by a dashed line with an open arrowhead pointing to the included use case and labeled with <<include>>.
  - Extend: a relationship between use cases that indicates one use case is optionally performed as an extension of another use case. Extend is represented by a dashed line with an open arrowhead pointing to the extended use case and labeled with <<extend>> and an optional extension point.
- A use case diagram can be used for the following purposes:
  - To capture the functional requirements of a system or a software program.
  - To communicate the scope and functionality of a system to stakeholders.
  - To identify the actors and their roles in the system.
  - To discover and analyze the commonality and variability among use cases.
  - To facilitate the design and implementation of the system using object-oriented principles.