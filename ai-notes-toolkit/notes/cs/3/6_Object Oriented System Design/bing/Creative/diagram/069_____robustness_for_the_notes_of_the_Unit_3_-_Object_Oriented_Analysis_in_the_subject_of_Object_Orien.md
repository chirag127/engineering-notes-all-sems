### Robustness

- Robustness is the ability of a system to handle errors, failures, and unexpected situations without compromising its functionality or performance.
- Robustness analysis is a technique for identifying and classifying the objects that participate in a use case scenario, based on their roles and responsibilities.
- Robustness analysis helps to bridge the gap between the textual description of use cases and the detailed design of the system, by providing a visual representation of the interactions between the objects and the actors.
- Robustness analysis also helps to verify the completeness and consistency of the use cases, by checking if all the objects and messages required for the scenario are present and correct.
- Robustness analysis uses a subset of UML notation, called robustness diagrams, to model the objects and their interactions. Robustness diagrams are similar to collaboration diagrams, but with three stereotypes of objects: boundary, control, and entity.
- Boundary objects represent the interfaces between the actors and the system, such as user interfaces, sensors, or external systems.
- Control objects represent the logic and coordination of the use case scenario, such as controllers, mediators, or coordinators.
- Entity objects represent the data and business logic of the system, such as entities, value objects, or services.
- Robustness analysis can be performed in five steps:
  - Identify the actors and the use case scenario to be analyzed.
  - Draw the boundary objects for each actor and the system, and connect them with association links.
  - Analyze the use case text, one sentence at a time, and identify the control and entity objects that are involved in each step of the scenario.
  - Draw the control and entity objects, and connect them with the boundary objects and other objects using message links, indicating the direction and sequence of the messages.
  - Review and refine the robustness diagram, checking for completeness, consistency, and clarity.