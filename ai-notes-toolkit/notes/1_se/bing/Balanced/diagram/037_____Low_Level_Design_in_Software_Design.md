Low-level design (LLD) is a component-level design process that follows a step-by-step refinement process. This process can be used for designing data structures, required software architecture, source code and ultimately, performance algorithms.

A low-level design document (LLD) typically contains the following sections:

- Introduction: This section provides an overview of the system or component, its purpose, scope, objectives, and assumptions.
- Architecture: This section describes the overall architecture of the system or component, its components, interfaces, dependencies, and interactions.
- Modules: This section describes each module of the system or component in detail, including its name, description, inputs, outputs, functionality, algorithms, data structures, and pseudocode.
- Test cases: This section describes the test cases that will be used to verify the functionality and performance of the system or component, including the test inputs, expected outputs, and test steps.

An example of a low-level design diagram for a user authentication system is shown below:

### Low Level Design in Software Design

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Web Browser   |       |   Web Server    |       |   Database      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       | 1. Enter username     |                       |
       |    and password       |                       |
       |---------------------->|                       |
       |                       |                       |
       |                       | 2. Call API           |
       |                       |    "ValidateUser()"   |
       |                       |---------------------->|
       |                       |                       |
       |                       |                       | 3. Check if user
       |                       |                       |    exists and
       |                       |                       |    password
       |                       |                       |    matches
       |                       |                       |
       |                       |<----------------------|
       |                       |                       |
       |                       | 4. Return validation  |
       |                       |    result             |
       |<----------------------|                       |
       |                       |                       |
       | 5. Display result     |                       |
       |    to user            |                       |
       |                       |                       |
```