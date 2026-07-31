### Robustness for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design

- Robustness analysis is a technique for identifying and classifying objects in a system based on their roles and interactions in the use cases .
- Robustness analysis helps to bridge the gap between the requirements and the design of a system, and to ensure that the system is consistent, complete, and correct .
- Robustness analysis involves the following steps:
  - Analyze the narrative text of each use case and identify the objects that participate in the use case.
  - Classify the objects into three stereotypes: boundary, control, and entity.
    - Boundary objects represent the interfaces between the actors and the system, such as user interfaces, input/output devices, etc.
    - Control objects represent the use case logic and coordinate the other classes, such as controllers, mediators, coordinators, etc.
    - Entity objects represent the persistent information and business rules of the system, such as data structures, databases, files, etc.
  - Draw a robustness diagram for each use case, showing the actors, the boundary, control, and entity objects, and the messages exchanged between them .
  - Refine the robustness diagram by adding attributes, operations, and associations to the objects, and by checking the consistency and completeness of the diagram.
  - Map the robustness diagram to a class diagram, by identifying the classes, their attributes, operations, and associations, and by applying design principles and patterns.
- Robustness analysis is an iterative and incremental process, that can be performed at different levels of abstraction and detail, and that can be integrated with other modeling techniques, such as use case diagrams, sequence diagrams, state diagrams, etc .