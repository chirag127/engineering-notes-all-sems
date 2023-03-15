Low-level design (LLD) is a component-level design process that follows a step-by-step refinement process. This process can be used for designing data structures, required software architecture, source code and ultimately, performance algorithms.

A low-level design document (LLD) typically contains the following sections:

- Introduction: This section provides an overview of the system or component, its purpose, scope, objectives, and assumptions.
- Architecture: This section describes the high-level architecture of the system or component, its components, interfaces, dependencies, and interactions.
- Modules: This section describes the individual modules of the system or component, their functionality, inputs, outputs, parameters, and exceptions.
- Data Structures: This section describes the data structures used by the system or component, their attributes, types, and relationships.
- Algorithms: This section describes the algorithms used by the system or component, their logic, pseudocode, and complexity.
- Interfaces: This section describes the interfaces of the system or component, their specifications, protocols, and formats.
- Test Cases: This section describes the test cases for the system or component, their inputs, expected outputs, and validation criteria.

An example of a low-level design diagram for a simple calculator application is shown below:

### Low Level Design in Software Design

```
+-----------------+      +-----------------+      +-----------------+
| User Interface  |      | Business Logic  |      | Data Storage    |
+-----------------+      +-----------------+      +-----------------+
| - Display       |      | - Validate      |      | - Store         |
| - Input         |      | - Calculate     |      | - Retrieve      |
| - Output        |      | - Format        |      | - Delete        |
+-----------------+      +-----------------+      +-----------------+
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
       +---------------------->+                       |
       |                       |                       |
       |                       +---------------------->+
       |                       |                       |
       |                       |                       |
       |                       +<----------------------+
       |                       |                       |
       +<----------------------+                       |
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
+-----------------+      +-----------------+      +-----------------+
| User Interface  |      | Business Logic  |      | Data Storage    |
+-----------------+      +-----------------+      +-----------------+
```