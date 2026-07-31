## Modeling UML Use Case Diagrams and Capturing Use Case Scenarios

- UML stands for Unified Modeling Language, which is a standard way of visualizing and documenting the design of a software system.
- Use case diagrams are one of the types of UML diagrams that show the high-level functions and scope of a system, as well as the interactions between the system and its users (or actors).
- Use case diagrams help to capture the requirements of the system, and to specify the expected behavior of the system (what) without detailing the implementation (how).
- Use case diagrams consist of the following elements:
  - Actors: represent the roles of the external entities that interact with the system, such as users, customers, or other systems. Actors are depicted as stick figures or icons.
  - Use cases: represent the goals or functions that the system can perform for the actors. Use cases are depicted as ovals with names inside.
  - Associations: represent the relationships between actors and use cases, indicating who can initiate or participate in a use case. Associations are depicted as solid lines with optional arrows to show the direction of communication.
  - System boundary: represents the scope or boundary of the system, separating the internal functions from the external environment. System boundary is depicted as a rectangle that encloses the use cases.
  - Packages: represent the logical grouping or categorization of use cases or actors. Packages are depicted as tabbed folders with names inside.
  - Generalization: represent the inheritance or specialization relationship between actors or use cases, indicating that one actor or use case inherits the characteristics or behavior of another. Generalization is depicted as a dashed line with a hollow triangle pointing to the parent actor or use case.
  - Include: represent the dependency or inclusion relationship between use cases, indicating that one use case is always performed as part of another use case. Include is depicted as a dashed line with an open arrowhead pointing to the included use case, and labeled with <<include>>.
  - Extend: represent the dependency or extension relationship between use cases, indicating that one use case can optionally extend the behavior of another use case under certain conditions. Extend is depicted as a dashed line with an open arrowhead pointing to the extended use case, and labeled with <<extend>>.

- An example of a use case diagram for an online shopping system is shown below:

![use case diagram example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-use-case-diagram/online-shopping-use-case-diagram.png)

- Use case scenarios are the textual descriptions of the steps or interactions that occur in a use case diagram, detailing the flow of events from the actor's perspective.
- Use case scenarios can be written in various formats, such as plain text, tables, or templates. A common template for use case scenarios is the following:

| Use Case Name | A brief and meaningful name for the use case |
| --- | --- |
| Actor | The primary actor who initiates or participates in the use case |
| Description | A short summary of the purpose and scope of the use case |
| Precondition | The condition that must be true before the use case can start |
| Postcondition | The condition that will be true after the use case is completed |
| Normal Flow | The main sequence of steps or interactions that occur in the use case |
| Alternative Flow | The alternative or exceptional sequence of steps or interactions that may occur in the use case |
| Extension Points | The points where the use case can be extended by another use case |

- An example of a use case scenario for the "Place Order" use case in the online shopping system is shown below:

| Use Case Name | Place Order |
| --- | --- |
| Actor | Customer |
| Description | The customer places an order for the items in the shopping cart |
| Precondition | The customer has added items to the shopping cart and logged in to the system |
| Postcondition | The order is confirmed and the payment is processed |
| Normal Flow | 1. The customer clicks on the "Checkout" button <br> 2. The system displays the order summary and the payment options <br> 3. The customer selects a payment option and enters the payment details <br> 4. The system validates the payment details and processes the payment <br> 5. The system displays the order confirmation and the delivery details <br> 6. The system sends an email notification to the customer |
| Alternative Flow | 3a. The customer cancels the order <br> 3a1. The system returns to the shopping cart page <br> 4a