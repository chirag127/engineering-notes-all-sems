## Unit 6 - Use case 1

- A use case is a description of how a system interacts with one or more external entities, called actors, to achieve a specific goal.
- A use case diagram is a graphical representation of the use cases and actors involved in a system.
- A use case diagram consists of the following elements:
  - Actors: The external entities that interact with the system. They are represented by stick figures or icons.
  - Use cases: The goals or functions that the system provides to the actors. They are represented by ovals with names inside.
  - Associations: The relationships between actors and use cases. They are represented by solid lines with optional arrows to indicate the direction of communication.
  - System boundary: An optional rectangle that encloses the use cases and represents the scope of the system. It has a name on the top left corner.
  - Packages: An optional way to group related use cases or actors. They are represented by tabbed rectangles with names on the top.
  - Generalization: A relationship that indicates that one actor or use case inherits the characteristics of another actor or use case. It is represented by a dashed line with a hollow triangle pointing to the parent actor or use case.
  - Include: A relationship that indicates that one use case includes the behavior of another use case as a part of its normal execution. It is represented by a dashed line with an open arrowhead pointing to the included use case and a label <<include>>.
  - Extend: A relationship that indicates that one use case extends the behavior of another use case under certain conditions. It is represented by a dashed line with an open arrowhead pointing to the extended use case and a label <<extend>> with an optional extension point.

- An example of a use case diagram for an online shopping system is shown below:

![Use case diagram for online shopping system](https://www.uml-diagrams.org/examples/online-shopping-use-case-diagram-example.png)

- The use case diagram shows the following elements:
  - Actors: Customer, Administrator, and Bank
  - Use cases: View Items, Search Items, Add Item to Shopping Cart, Remove Item from Shopping Cart, Check Out, Process Payment, Ship Order, Manage Orders, Manage Items, and Manage Users
  - Associations: Customer is associated with View Items, Search Items, Add Item to Shopping Cart, Remove Item from Shopping Cart, and Check Out. Administrator is associated with Manage Orders, Manage Items, and Manage Users. Bank is associated with Process Payment.
  - System boundary: Online Shopping System
  - Packages: None
  - Generalization: None
  - Include: Check Out includes Process Payment and Ship Order
  - Extend: View Items extends Search Items with an extension point Filter by Category