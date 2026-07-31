### Function of each use case for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab

- A use case is a description of how a user interacts with a system to achieve a goal.
- A use case diagram is a graphical representation of the use cases and the actors involved in a system.
- A use case diagram shows the relationships between the use cases and the actors, as well as the boundaries of the system.
- A use case diagram can help to:
  - Specify the context of a system
  - Capture the requirements of a system
  - Validate a system's architecture
  - Drive implementation and generate test cases
  - Communicate with stakeholders and users
- A use case diagram consists of the following elements:
  - Actors: The external entities that interact with the system, such as users, roles, or other systems. They are represented by stick figures or icons.
  - Use cases: The functionalities or services that the system provides to the actors. They are represented by ovals with names inside.
  - System boundary: The scope or boundary of the system under consideration. It is represented by a rectangle that encloses the use cases.
  - Associations: The connections between the actors and the use cases. They are represented by solid lines with optional multiplicity indicators.
  - Generalizations: The inheritance relationships between actors or use cases. They are represented by dashed lines with empty arrowheads.
  - Include relationships: The dependencies between use cases that indicate that one use case is always included in another use case. They are represented by dashed lines with the keyword <<include>> and an arrowhead pointing to the included use case.
  - Extend relationships: The dependencies between use cases that indicate that one use case can optionally extend another use case under certain conditions. They are represented by dashed lines with the keyword <<extend>> and an arrowhead pointing to the extended use case.
- An example of a use case diagram for an online shopping system is shown below:

![use case diagram example](https://t4tutorials.com/wp-content/uploads/2018/03/Use-Case-Diagram-Example-1.jpg)

- In this example, the actors are Customer, Administrator, and Bank. The use cases are Selection of product, Confirm order, Calculate price with tax, Payment, Print slip, Manage product, and Manage order. The system boundary is Online Shopping System. The associations are shown by solid lines between the actors and the use cases. The generalizations are shown by dashed lines with empty arrowheads between the actors and between the use cases. The include relationships are shown by dashed lines with <<include>> and arrowheads pointing to the included use cases. The extend relationship is shown by a dashed line with <<extend>> and an arrowhead pointing to the extended use case.