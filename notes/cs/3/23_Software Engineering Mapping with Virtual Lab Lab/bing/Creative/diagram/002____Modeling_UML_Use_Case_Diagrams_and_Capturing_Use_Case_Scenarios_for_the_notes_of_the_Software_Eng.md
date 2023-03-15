## Modeling UML Use Case Diagrams and Capturing Use Case Scenarios

- A UML use case diagram is a graphical representation of the functional requirements of a system. It shows the actors (users or other systems) that interact with the system, and the use cases (goals or services) that the system provides to them  .
- A use case diagram can help to:
  - Represent the goals of system-user interactions
  - Define and organize functional requirements in a system
  - Specify the context and requirements of a system
  - Model the basic flow of events in a use case
- A use case diagram consists of the following elements:
  - **Actor**: An actor is a person, an organization, or another system that has a role in interacting with the system. An actor is represented by a stick figure with a name below it  .
  - **Use case**: A use case is a goal or a service that the system provides to an actor. A use case is represented by an oval with a name inside it  .
  - **Association**: An association is a line that connects an actor to a use case, indicating that the actor participates in the use case  .
  - **System boundary**: A system boundary is a rectangle that encloses the use cases of the system, indicating the scope of the system. A system boundary has a name on the top left corner  .
  - **Include**: An include relationship is a dashed arrow with the label «include» that connects two use cases, indicating that the base use case (the one with the arrowhead) always includes the behavior of the included use case (the one without the arrowhead)  .
  - **Extend**: An extend relationship is a dashed arrow with the label «extend» that connects two use cases, indicating that the base use case (the one without the arrowhead) may optionally extend the behavior of the extended use case (the one with the arrowhead) under some condition  .
  - **Generalization**: A generalization relationship is a solid line with a hollow triangle that connects two actors or two use cases, indicating that the child actor or use case (the one with the triangle) inherits the behavior and characteristics of the parent actor or use case (the one without the triangle)  .

- A use case diagram can be modeled using the following steps:
  - Identify the actors and use cases of the system
  - Draw the system boundary and name it
  - Place the actors and use cases inside or outside the system boundary
  - Draw the associations between actors and use cases
  - Identify any include, extend, or generalization relationships among use cases or actors
  - Label the relationships and use cases with meaningful names  

- A use case scenario is a textual description of the steps and interactions that occur in a use case. It can help to:
  - Elaborate the details of a use case
  - Specify the preconditions, postconditions, and exceptions of a use case
  - Verify the completeness and correctness of a use case diagram 
- A use case scenario can be captured using the following template:
  - **Use case name**: The name of the use case
  - **Actor**: The name of the primary actor who initiates the use case
  - **Description**: A brief summary of the use case
  - **Preconditions**: The conditions that must be true before the use case starts
  - **Postconditions**: The conditions that must be true after the use case ends
  - **Basic flow**: The normal sequence of steps and interactions that occur in the use case
  - **Alternative flows**: The alternative sequences of steps and interactions that occur in the use case when an exception or a variation happens 

- An example of a use case diagram and a use case scenario for an online shopping system is shown below:

![Use case diagram for online shopping system](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-use-case-diagram/