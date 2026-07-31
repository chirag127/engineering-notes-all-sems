# Function of each use case for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab

- A use case is a description of how a user interacts with a system to achieve a goal.
- A use case diagram is a graphical representation of the use cases and the actors involved in a system.
- A use case diagram shows the relationships between the use cases and the actors, as well as the boundaries of the system.
- A use case diagram can help to:
  - Specify the context and the requirements of a system
  - Validate the system architecture and design
  - Drive the implementation and testing of the system
  - Communicate the system functionality to the stakeholders
- A use case diagram consists of the following elements:
  - Actors: The external entities that interact with the system, such as users, roles, or other systems. Actors are represented by stick figures or icons.
  - Use cases: The actions or services that the system provides to the actors to achieve their goals. Use cases are represented by ovals with names inside.
  - System boundary: The scope or boundary of the system under consideration. The system boundary is represented by a rectangle that encloses the use cases.
  - Associations: The connections between the actors and the use cases that indicate who can initiate or participate in a use case. Associations are represented by solid lines.
  - Include relationships: The dependencies between the use cases that indicate that one use case is always performed as part of another use case. Include relationships are represented by dashed arrows with the keyword "include".
  - Extend relationships: The dependencies between the use cases that indicate that one use case can optionally extend the behavior of another use case under certain conditions. Extend relationships are represented by dashed arrows with the keyword "extend".
  - Generalization relationships: The inheritance relationships between the actors or the use cases that indicate that one actor or use case is a specialized version of another actor or use case. Generalization relationships are represented by solid arrows with empty arrowheads.

- An example of a use case diagram for an online shopping system is shown below:

![Use case diagram for online shopping system](https://miro.medium.com/max/1400/1*6Z1lY9X0yQ2y8t0yZfYw9w.png)

- The use case diagram shows the following functions of the online shopping system:
  - The customer can browse products, add products to the shopping cart, remove products from the shopping cart, view the shopping cart, check out, and make payment.
  - The administrator can manage products, manage orders, and manage customers.
  - The payment system can process payments and confirm payments.
  - The use case "browse products" includes the use case "search products" as a mandatory part of its functionality.
  - The use case "check out" includes the use case "calculate price with tax" as a mandatory part of its functionality.
  - The use case "check out" extends the use case "print slip" as an optional part of its functionality, depending on whether the customer chooses to print a slip or not.
  - The use case "make payment" includes the use case "payment" as a mandatory part of its functionality, which is provided by the payment system actor.
  - The customer actor is a generalization of the registered customer and the guest customer actors, which are specialized versions of the customer actor with different attributes and privileges.