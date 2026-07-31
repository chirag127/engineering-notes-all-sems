## Unit 6 - Use case 1

- A use case is a description of how a system interacts with one or more external entities, called actors, to achieve a specific goal.
- A use case diagram is a graphical representation of the use cases and actors involved in a system.
- A use case diagram consists of the following elements:
  - Actors: The external entities that interact with the system. They are represented by stick figures or icons.
  - Use cases: The goals or functions that the system provides to the actors. They are represented by ovals with the use case name inside.
  - Associations: The relationships between actors and use cases. They are represented by solid lines with optional arrows to indicate the direction of communication.
  - System boundary: An optional rectangle that encloses the use cases and represents the scope of the system. It is labeled with the system name.
  - Packages: An optional grouping mechanism that can contain use cases, actors, or other packages. They are represented by tabbed rectangles with the package name inside.
  - Generalization: A relationship that indicates that one actor or use case inherits the characteristics of another actor or use case. It is represented by a dashed line with a hollow triangle pointing to the parent actor or use case.
  - Include: A relationship that indicates that one use case includes the behavior of another use case as a part of its normal execution. It is represented by a dashed line with an open arrowhead pointing to the included use case and labeled with <<include>>.
  - Extend: A relationship that indicates that one use case extends the behavior of another use case under some condition. It is represented by a dashed line with an open arrowhead pointing to the extended use case and labeled with <<extend>> and an optional extension point.

- An example of a use case diagram for an online shopping system is shown below:

```mermaid
graph LR
  Customer(Customer)
  Admin(Admin)
  System(Online Shopping System)
  Browse(Browse Products)
  Search(Search Products)
  Add(Add to Cart)
  Checkout(Checkout)
  Pay(Pay)
  Confirm(Confirm Order)
  Manage(Manage Products)
  Update(Update Product)
  Delete(Delete Product)
  Customer -- Browse
  Customer -- Search
  Customer -- Add
  Customer -- Checkout
  Customer -- Pay
  Customer -- Confirm
  Admin -- Manage
  Admin -- Update
  Admin -- Delete
  Browse ..> Search : <<extend>>
  Checkout ..> Pay : <<include>>
  Confirm ..> Pay : <<include>>
  Manage ..> Update : <<include>>
  Manage ..> Delete : <<include>>
  System((Online Shopping System)) -- Browse
  System -- Search
  System -- Add
  System -- Checkout
  System -- Pay
  System -- Confirm
  System -- Manage
  System -- Update
  System -- Delete
```