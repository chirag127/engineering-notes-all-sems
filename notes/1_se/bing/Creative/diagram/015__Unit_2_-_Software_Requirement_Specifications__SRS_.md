A software requirement specification (SRS) is a document that describes the purpose, functionality, interface, and performance criteria of a software system. It helps to communicate the expectations and requirements of the stakeholders, developers, and users of the system. A requirement diagram is a graphical representation of the relationships among the requirements and other model elements in a system. It can help to visualize the structure, dependencies, and traceability of the requirements. A requirement diagram can use different types of elements and relationships, such as:

- Requirement: a statement of a capability or condition that the system must satisfy. It can have a unique identifier, a name, a text description, and other properties. It is represented by a rectangle with the stereotype «requirement».
- Satisfy: a dependency relationship that indicates that a model element (such as a component, a use case, or a test case) fulfills a requirement or a set of requirements. It is represented by a dashed arrow with the stereotype «satisfy» pointing from the satisfying element to the satisfied requirement.
- Verify: a dependency relationship that indicates that a model element (such as a test case or a scenario) provides evidence that a requirement or a set of requirements have been met. It is represented by a dashed arrow with the stereotype «verify» pointing from the verifying element to the verified requirement.
- Derive: a dependency relationship that indicates that a requirement can be derived from another requirement. It is represented by a dashed arrow with the stereotype «derive» pointing from the derived requirement to the source requirement.
- Refine: a dependency relationship that indicates that a model element (such as a use case, an activity, or a state machine) provides more details or information about a requirement or a set of requirements. It is represented by a dashed arrow with the stereotype «refine» pointing from the refining element to the refined requirement.
- Contain: a composition relationship that indicates that a requirement contains other requirements as its parts. It is represented by a solid line with a black diamond at the end of the containing requirement and a white diamond at the end of the contained requirement.
- Trace: a dependency relationship that indicates a historical or logical connection between two model elements. It is represented by a dashed arrow with the stereotype «trace».

Here is an example of a requirement diagram for a software system that manages online courses:

```
+---------------------+        +---------------------+
|«requirement»        |        |«requirement»        |
|Online Course System |        |User Authentication  |
|ID: R1               |        |ID: R2               |
|Description: The     |        |Description: The     |
|system shall allow   |        |system shall allow   |
|users to enroll in   |        |users to register,   |
|and access online    |        |log in, and log out  |
|courses.             |        |of their accounts.   |
+---------------------+        +---------------------+
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |«satisfy»
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |