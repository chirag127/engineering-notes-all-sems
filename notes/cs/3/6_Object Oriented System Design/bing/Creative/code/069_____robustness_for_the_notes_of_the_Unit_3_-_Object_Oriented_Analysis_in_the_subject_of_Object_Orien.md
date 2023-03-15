# Robustness for the notes of the Unit 3 - Object Oriented Analysis

- Robustness is the ability of a system to handle errors, failures, and unexpected situations without compromising its functionality or performance.
- Robustness analysis is a technique for identifying and classifying the objects that participate in a use case scenario, based on their roles and responsibilities.
- Robustness analysis helps to bridge the gap between the requirements and the design of a system, by providing a first-guess set of objects that can be refined and elaborated in the design phase.
- Robustness analysis involves the following steps:
  - Analyzing the narrative text of use cases, one sentence at a time, and identifying the nouns and verbs that represent the objects and actions in the scenario.
  - Classifying the objects into three stereotypes: boundary, control, and entity, based on their roles and interactions with other objects.
    - Boundary objects represent the interfaces between the actors and the system, such as user interfaces, input/output devices, or external systems.
    - Control objects represent the use case logic and coordinate the other objects, such as controllers, mediators, or coordinators.
    - Entity objects represent the persistent information and business rules of the system, such as data structures, databases, or business objects.
  - Drawing a robustness diagram, which is similar to a UML collaboration diagram, that shows the objects and their associations, messages, and lifelines.
  - Validating the robustness diagram by checking the consistency, completeness, and correctness of the objects and their interactions, and by tracing the messages to the use case text.
  - Refining the robustness diagram by adding, deleting, or modifying the objects and their relationships, and by applying design principles and patterns to improve the quality of the system.
- Robustness analysis is an informal and iterative technique that can be applied at different levels of abstraction and detail, depending on the complexity and scope of the system.
- Robustness analysis can help to discover missing, redundant, or ambiguous requirements, to identify potential design problems or risks, and to facilitate communication and collaboration among the stakeholders of the system.