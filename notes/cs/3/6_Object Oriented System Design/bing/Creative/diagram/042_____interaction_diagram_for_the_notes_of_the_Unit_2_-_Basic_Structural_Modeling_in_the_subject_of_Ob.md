### Interaction Diagram for the Notes of the Unit 2 - Basic Structural Modeling in the Subject of Object Oriented System Design

- Interaction diagrams are used to observe the dynamic behavior of a system .
- Interaction diagrams visualize the communication and sequence of message passing in the system.
- Interaction diagrams represent the structural aspects of various objects in the system.
- Interaction diagrams are divided into four main types of diagrams:
  - Communication diagram: shows the interactions between objects using a graph-like notation.
  - Sequence diagram: shows the interactions between objects using a vertical timeline notation.
  - Timing diagram: shows the interactions between objects using a horizontal timeline notation.
  - Interaction overview diagram: shows the interactions between objects using a combination of activity and sequence diagrams.
- Interaction diagrams are useful for modeling the order of control flow, the object architecture, the timing constraints, and the overview of a system's behavior .
- Interaction diagrams are drawn for each use case in the system.
- Interaction diagrams are based on the following elements :
  - Object: a rectangle with the name of the object and its class (optional) underlined.
  - Lifeline: a dashed vertical line that represents the existence of an object over time.
  - Activation: a thin or thick rectangle on a lifeline that represents the execution of an operation or a method by an object.
  - Message: a horizontal arrow that represents the communication between objects. The arrowhead indicates the direction of the message. The label on the arrow indicates the name and parameters of the message.
  - Return message: a dashed horizontal arrow that represents the return value of a message.
  - Self message: a message that an object sends to itself. It is represented by a looped arrow on the same lifeline.
  - Recursive message: a message that an object sends to another object of the same class. It is represented by a looped arrow on a different lifeline.
  - Create message: a message that creates a new object. It is represented by a dashed arrow with an open arrowhead pointing to the lifeline of the new object.
  - Destroy message: a message that destroys an object. It is represented by a cross on the lifeline of the object.
  - Constraint: a textual expression that specifies a condition or a restriction on the messages or the objects. It is enclosed in curly braces.
  - Comment: a textual note that provides additional information or explanation. It is enclosed in a rectangle with a dog-ear corner and attached to an element by a dashed line.

- Here is an example of a sequence diagram for the use case of placing an order in an online shopping system:

![sequence diagram example](https://www.tutorialspoint.com/uml/images/uml_sequence_diagram.jpg)

- Here is an example of a communication diagram for the same use case:

![communication diagram example](https://www.tutorialspoint.com/uml/images/uml_collaboration_diagram.jpg)

- Here is an example of a timing diagram for the use case of sending an email:

![timing diagram example](https://www.lucidchart.com/pages/assets/img/uml/interaction-diagram-timing-diagram.png)

- Here is an example of an interaction overview diagram for the use case of booking a flight:

![interaction overview diagram example](https://www.lucidchart.com/pages/assets/img/uml/interaction-diagram-interaction-overview-diagram.png)