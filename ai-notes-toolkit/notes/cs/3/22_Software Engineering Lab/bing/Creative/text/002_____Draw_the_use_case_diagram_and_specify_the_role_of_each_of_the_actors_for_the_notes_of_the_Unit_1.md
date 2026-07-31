### Use Case Diagram and Actors for Software Engineering Lab

A use case diagram is a graphical representation of the interactions between a system and its external entities, such as users, other systems, or hardware devices. A use case diagram shows the functionality of a system from the perspective of the actors who use it. Actors are roles that can perform actions on the system or receive information from the system. A use case diagram consists of the following elements:

- **Actors**: Represent the external entities that interact with the system. They are depicted as stick figures or icons with names.
- **Use cases**: Represent the goals or tasks that the actors want to achieve or perform with the system. They are depicted as ovals with names.
- **Associations**: Represent the communication or interaction between actors and use cases. They are depicted as solid lines with optional arrows to indicate the direction of the interaction.
- **System boundary**: Represents the scope or boundary of the system under consideration. It is depicted as a rectangle that encloses the use cases and optionally the actors that are part of the system.
- **Relationships**: Represent the dependencies or constraints between use cases or actors. They are depicted as dashed lines with different types of arrows or symbols to indicate the type of the relationship. Some common types of relationships are:

  - **Include**: Represents a mandatory inclusion of another use case in the base use case. It is depicted as a dashed line with an open arrowhead pointing from the base use case to the included use case. The keyword "include" is written above the line.
  - **Extend**: Represents an optional extension of another use case in the base use case. It is depicted as a dashed line with an open arrowhead pointing from the extending use case to the extended use case. The keyword "extend" is written above the line. An extension point is a condition or a point in the base use case where the extension can occur. It is written in the extended use case inside brackets.
  - **Generalization**: Represents a specialization or inheritance relationship between actors or use cases. It is depicted as a solid line with a hollow triangle pointing from the child actor or use case to the parent actor or use case.
  - **Dependency**: Represents a dependency or influence relationship between actors or use cases. It is depicted as a dashed line with an open arrowhead pointing from the dependent actor or use case to the independent actor or use case. An optional stereotype or keyword can be written above the line to indicate the type of the dependency.

An example of a use case diagram for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab is shown below:

![Use case diagram example](https://i.imgur.com/4g9Xm4h.png)

The use case diagram shows the following actors and their roles:

- **Student**: A student who wants to learn and practice the concepts of software engineering. The student can access the notes, view the lab exercises, submit the lab assignments, and take the quizzes.
- **Instructor**: An instructor who teaches and guides the students on the software engineering topics. The instructor can create and update the notes, create and update the lab exercises, evaluate and grade the lab assignments, and create and update the quizzes.
- **Admin**: An admin who manages and maintains the system. The admin can create and update the user accounts, backup and restore the data, and monitor and troubleshoot the system.