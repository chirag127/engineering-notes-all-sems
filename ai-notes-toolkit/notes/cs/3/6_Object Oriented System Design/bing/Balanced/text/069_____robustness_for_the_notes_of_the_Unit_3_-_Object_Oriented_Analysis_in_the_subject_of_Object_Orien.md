### Robustness for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design

- Robustness is the ability of a system to handle errors, failures, and unexpected situations without compromising its functionality or performance.
- Robustness analysis is a technique for identifying and classifying the objects that participate in a use case based on their roles and responsibilities .
- Robustness analysis helps to bridge the gap between the requirements and the design of a system, by providing a first-guess set of objects that can be refined and elaborated in the design phase .
- Robustness analysis involves the following steps:
  - Analyzing the narrative text of use cases, one sentence at a time, and identifying the nouns and verbs that represent the objects and their interactions.
  - Drawing a robustness diagram, which is similar to a UML collaboration diagram, that shows the objects and their relationships using the following stereotypes:
    - Boundary object: represents the interface between the actors and the system, such as a user interface, a file, or a device.
    - Control object: represents the use case logic and coordinates the other objects, such as a controller, a manager, or a handler.
    - Entity object: represents the data and business logic of the system, such as a database, a model, or a domain object.
  - Validating the robustness diagram by checking the following rules:
    - Every use case scenario must have at least one control object.
    - Every actor must be connected to a boundary object, not directly to a control or an entity object.
    - Every entity object must be connected to a control object, not directly to a boundary object.
    - Every message must be sent from a boundary object to a control object, from a control object to another control object, or from a control object to an entity object.
  - Refining the robustness diagram by adding, deleting, or modifying the objects and their relationships as needed.
  - Mapping the robustness diagram to a class diagram by converting the objects to classes, the messages to operations, and the relationships to associations.