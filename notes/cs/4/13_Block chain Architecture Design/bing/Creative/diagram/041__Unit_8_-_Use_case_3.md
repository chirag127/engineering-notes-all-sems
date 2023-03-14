A use case diagram is a visual representation of the different ways and possible scenarios of using a system. It illustrates how a user will perform actions and interact with a particular system, such as a website or an app. Use case diagrams are written in natural language, which helps users easily understand them. Additionally, they provide businesses an excellent way to communicate with customers.

A use case diagram consists of the following elements:

- Actors: The users or external entities that interact with the system. They are represented by stick figures or ovals with names.
- Use cases: The actions or functions that the actors can perform with the system. They are represented by ovals with names.
- System boundary: The scope or boundary of the system. It is represented by a rectangle that encloses the use cases.
- Relationships: The connections or associations between the actors and the use cases, or between the use cases themselves. They are represented by different types of lines, such as:

  - Association: A solid line that indicates an actor can initiate or participate in a use case.
  - Include: A dashed line with an open arrowhead that indicates a use case is included or invoked by another use case.
  - Extend: A dashed line with an open arrowhead that indicates a use case can be extended or modified by another use case under certain conditions.
  - Generalization: A solid line with a closed arrowhead that indicates a use case or an actor is a specialized or sub-type of another use case or actor.

To draw a use case diagram, you need to follow these steps:

- Identify the actors and use cases of the system.
- Draw the system boundary and place the actors and use cases inside or outside the boundary accordingly.
- Draw the relationships between the actors and the use cases, or between the use cases themselves, using the appropriate line types.
- Label the actors, use cases, and relationships with descriptive names.

To draw a use case diagram in markdown, you can use the following syntax:

- Use `@startuml` and `@enduml` to indicate the start and end of the diagram.
- Use `:actor:` to define an actor, followed by the actor name.
- Use `:usecase:` to define a use case, followed by the use case name.
- Use `rectangle` to define the system boundary, followed by the system name and the list of use cases inside the boundary.
- Use `--` to draw an association between an actor and a use case, or between two use cases.
- Use `..>` to draw an include relationship between two use cases, with the arrow pointing to the included use case.
- Use `<..` to draw an extend relationship between two use cases, with the arrow pointing to the extended use case.
- Use `<|---` to draw a generalization between two actors or two use cases, with the arrow pointing to the general or parent actor or use case.

For example, the following markdown code will generate a use case diagram for Unit 8 - Use case 3:

@startuml
:actor: Student
:actor: Teacher
:actor: Parent
:usecase: Login
:usecase: View grades
:usecase: View assignments
:usecase: Submit assignments
:usecase: Grade assignments
:usecase: Send feedback
rectangle "Online Learning System" {
  Login
  View grades
  View assignments
  Submit assignments
  Grade assignments
  Send feedback
}
Student -- Login
Teacher -- Login
Parent -- Login
Student -- View grades
Student -- View assignments
Student -- Submit assignments
Teacher -- View grades
Teacher -- View assignments
Teacher -- Grade assignments
Teacher -- Send feedback
Parent -- View grades
Parent -- View assignments
View assignments ..> Login
View grades ..> Login
Submit assignments ..> Login
Grade assignments ..> Login
Send feedback ..> Login
Submit assignments <.. View assignments
Grade assignments <.. View assignments
Send feedback <.. Grade assignments
@enduml

The output of the code will look like this:

![Use case diagram for Unit 8 - Use case 3](https://i.imgur.com/8Jy1x0f.png)