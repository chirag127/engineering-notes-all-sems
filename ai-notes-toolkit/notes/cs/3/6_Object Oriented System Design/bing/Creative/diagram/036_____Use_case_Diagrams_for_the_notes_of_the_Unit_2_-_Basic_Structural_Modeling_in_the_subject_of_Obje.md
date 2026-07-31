# Use Case Diagrams

## Definition

- A use case diagram is a graphical depiction of a user's possible interactions with a system.
- A use case diagram shows various use cases and different types of users the system has and will often be accompanied by other types of diagrams as well.
- A use case diagram is a visual summarization of interactions and relationships within a system.
- A use case diagram is a tool that maps interactions between users and systems to show the interactions between them.

## Purpose

- Use case diagrams are typically developed in the early stage of development and people often apply use case modeling for the following purposes:
  - Specify the context of a system
  - Capture the requirements of a system
  - Validate a systems architecture
  - Drive implementation and generate test cases
- An effective use case diagram can help your team discuss and represent:
  - Scenarios in which your system or application interacts with people, organizations, or external systems
  - Goals that your system or application helps those entities (known as actors) achieve
  - The scope of your system

## Elements

- The main elements of a use case diagram are:
  - Actors: An actor is a person, organization, or external system that has a role in one or more interactions with your system. Actors are represented by stick figures.
  - Use cases: A use case is a set of activities that a system performs in collaboration with one or more actors to achieve a specific goal. Use cases are represented by either circles or ellipses.
  - Relationships: A relationship is a connection between an actor and a use case, or between two use cases. Relationships are represented by lines, with optional symbols at the ends to indicate the type of relationship. The main types of relationships are:
    - Association: An association is a simple connection between an actor and a use case, or between two use cases. It indicates that the actor can participate in the use case, or that one use case can include or extend another use case. Associations are represented by solid lines, with optional arrows to indicate the direction of communication.
    - Include: An include relationship indicates that a use case is always performed as part of another use case. It is used to modularize common behaviors and reduce duplication. Include relationships are represented by dashed lines, with an open arrowhead pointing to the included use case and a label <<include>>.
    - Extend: An extend relationship indicates that a use case can optionally perform another use case, depending on a condition or an extension point. It is used to capture alternative or exceptional scenarios. Extend relationships are represented by dashed lines, with an open arrowhead pointing to the extended use case and a label <<extend>>.
    - Generalization: A generalization relationship indicates that a use case is a specialized version of another use case. It is used to capture commonalities and variations among use cases. Generalization relationships are represented by solid lines, with a closed arrowhead pointing to the general use case and a label <<generalize>>.

## Examples

- Here are some use case diagram examples and templates that you can use:
  - Retail use case diagram: This use case diagram example depicts the internal functions and employee interactions within a retail store. It shows the actors (cashier, customer, manager, supplier), the use cases (process sale, manage inventory, generate report, order goods), and the relationships among them.

![Retail use case diagram](https://venngage-wordpress.s3.amazonaws.com/uploads/2021/07/Retail-Use-Case-Diagram-Example.png)

  - Restaurant use case diagram: In this example, a restaurant’s daily operations serve as the system, the staff and customers serve as the actors, and the use cases include taking orders, preparing food, serving food, and processing payments. It also shows the include and extend relationships between some use cases.

![Restaurant use case diagram](https://venngage-wordpress.s3.amazonaws.com/uploads/2021/07/Restaurant-Use-Case-Diagram-Example.png)

  - Library use case diagram: This use case diagram example shows the interactions between a library system and its users. It shows the actors (librarian, borrower, member), the use cases (borrow book, return book, search book, register member, renew membership), and the relationships among them.

![Library use case diagram](https://venngage-wordpress.s3.amazonaws.com/uploads/2021/07/Library-Use-Case-Diagram-Example.png)

  -