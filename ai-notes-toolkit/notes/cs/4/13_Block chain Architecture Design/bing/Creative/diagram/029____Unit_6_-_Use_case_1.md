## Unit 6 - Use case 1

- A use case is a description of how a system interacts with an actor (a user or another system) to achieve a goal.
- A use case diagram is a graphical representation of the use cases and the actors involved in a system.
- A use case diagram consists of the following elements:
  - Actors: represent the roles that interact with the system. They are drawn as stick figures with labels.
  - Use cases: represent the goals or functions that the system provides to the actors. They are drawn as ovals with labels.
  - Associations: represent the relationships between actors and use cases. They are drawn as solid lines with optional arrows to indicate the direction of communication.
  - System boundary: represents the scope or boundary of the system. It is drawn as a rectangle that encloses the use cases.
  - Packages: represent a group of related use cases or actors. They are drawn as rectangles with labels and dashed lines.
  - Generalization: represent a generalization or specialization relationship between actors or use cases. They are drawn as solid lines with a hollow triangle pointing to the parent element.
  - Include: represent a common functionality that is included by another use case. They are drawn as dashed lines with an open arrowhead pointing to the included use case and a label <<include>>.
  - Extend: represent a conditional or optional functionality that extends another use case. They are drawn as dashed lines with an open arrowhead pointing to the extending use case and a label <<extend>>.

- An example of a use case diagram for an online shopping system is shown below:

```mermaid
graph LR
  Customer
  Admin
  System[Online Shopping System]
  Customer -- Login --> System
  Customer -- Browse Products --> System
  Customer -- Add to Cart --> System
  Customer -- Checkout --> System
  Customer -- View Order History --> System
  Customer -- Rate and Review Products --> System
  Admin -- Manage Products --> System
  Admin -- Manage Orders --> System
  Admin -- Manage Customers --> System
  System -- Confirm Order --> Customer
  System -- Send Invoice --> Customer
  System -- Deliver Products --> Customer
  System -- Send Notification --> Admin
  Checkout ..> Confirm Order : <<include>>
  Checkout ..> Send Invoice : <<include>>
  Checkout ..> Deliver Products : <<include>>
  Checkout ..> Send Notification : <<include>>
  Rate and Review Products .> Browse Products : <<extend>>
  Manage Products .> Manage Orders : <<extend>>
  Manage Products .> Manage Customers : <<extend>>
```