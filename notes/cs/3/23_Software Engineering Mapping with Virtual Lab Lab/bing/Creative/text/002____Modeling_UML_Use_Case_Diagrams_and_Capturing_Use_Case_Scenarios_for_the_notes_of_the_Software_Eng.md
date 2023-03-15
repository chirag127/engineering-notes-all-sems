## Modeling UML Use Case Diagrams and Capturing Use Case Scenarios

- UML stands for Unified Modeling Language, which is a standard way of visualizing and documenting the design of a software system.
- Use case diagrams are one of the types of UML diagrams that show the behavior and requirements of a system from the perspective of the users or actors.
- Use cases are the goals or tasks that the users want to achieve by interacting with the system. They describe **what** the system does, not **how** it does it.
- Use case diagrams consist of the following elements:
  - Actors: The external entities that interact with the system. They can be people, organizations, or other systems. They are represented by stick figures or icons.
  - Use cases: The functions or services that the system provides to the actors. They are represented by ovals with names inside.
  - System boundary: The scope or boundary of the system under consideration. It is represented by a rectangle that encloses the use cases.
  - Associations: The relationships between the actors and the use cases. They are represented by solid lines with optional multiplicity indicators.
  - Generalizations: The relationships that indicate that one actor or use case inherits the characteristics of another actor or use case. They are represented by dashed lines with empty arrowheads.
  - Include relationships: The relationships that indicate that one use case includes the behavior of another use case as a part of its normal execution. They are represented by dashed lines with the keyword "include" and an arrowhead pointing to the included use case.
  - Extend relationships: The relationships that indicate that one use case extends the behavior of another use case under certain conditions. They are represented by dashed lines with the keyword "extend" and an arrowhead pointing to the extended use case.
  - Packages: The logical grouping of related elements in a use case diagram. They are represented by tabbed rectangles with names inside.

- An example of a use case diagram for an online shopping system is shown below:

![Use case diagram example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-use-case-diagram/use-case-diagram-example.png)

- Capturing use case scenarios is the process of describing the steps or interactions that occur between the actors and the system for each use case.
- Use case scenarios can be captured in different ways, such as:
  - Textual descriptions: The simplest way of capturing use case scenarios is by writing them in natural language, using a template or a format that specifies the name, description, preconditions, postconditions, main flow, alternative flows, and exceptions of each use case.
  - Activity diagrams: A graphical way of capturing use case scenarios is by using activity diagrams, which show the sequence of actions and decisions that occur within a use case. They use symbols such as circles, arrows, diamonds, and bars to represent the elements of a use case scenario.
  - Sequence diagrams: Another graphical way of capturing use case scenarios is by using sequence diagrams, which show the interactions and messages that occur between the actors and the system for a use case. They use symbols such as boxes, lines, arrows, and lifelines to represent the elements of a use case scenario.

- An example of a textual description for the use case "Place Order" in the online shopping system is shown below:

| Name | Place Order |
| --- | --- |
| Description | The customer places an order for the items in the shopping cart. |
| Preconditions | The customer has logged in and has items in the shopping cart. |
| Postconditions | The order is confirmed and the payment is processed. |
| Main flow | 1. The customer clicks on the "Checkout" button. <br> 2. The system displays the order summary and the payment options. <br> 3. The customer selects a payment option and enters the payment details. <br> 4. The system validates the payment details and processes the payment. <br> 5. The system confirms the order and sends a confirmation email to the customer. |
| Alternative flows | 3a. The customer cancels the order. <br> 3a1. The system returns to the shopping cart page. <br> 4a. The payment details are invalid or the payment is declined. <br> 4a1. The system displays an error message and asks the customer to enter the payment details again. |
| Exceptions | 2a. The shopping cart is empty. <br> 2a1. The system displays a message that the shopping cart is empty and redirects the customer