## Modeling UML Use Case Diagrams and Capturing Use Case Scenarios

- UML stands for Unified Modeling Language, which is a standard way of visualizing and documenting the design of a software system.
- Use case diagrams are one of the types of UML diagrams that show the behavior and requirements of a system from the perspective of the users (or actors).
- Use case diagrams consist of the following elements:
  - Actors: represent the roles or entities that interact with the system, such as users, customers, or other systems. Actors are depicted as stick figures or icons.
  - Use cases: represent the goals or functions that the actors want to achieve by using the system, such as login, register, or purchase. Use cases are depicted as ovals with names inside.
  - Relationships: represent the connections or associations between actors and use cases, or between use cases themselves. Relationships are depicted as lines with different symbols to indicate the type of relationship, such as association, include, extend, or generalize.
- Use case diagrams are useful for:
  - Representing the goals of system-user interactions
  - Defining and organizing functional requirements in a system
  - Specifying the context and requirements of a system
  - Modeling the basic flow of events in a use case
- Use case scenarios are the textual descriptions of the steps and interactions that occur in a use case. Use case scenarios can be written in different formats, such as:
  - Brief: a simple summary of the main success scenario
  - Casual: a more detailed description of the main success scenario and some alternative scenarios
  - Fully dressed: a comprehensive and structured description of the main success scenario and all possible alternative scenarios, including preconditions, postconditions, triggers, exceptions, and extensions
- Use case scenarios are useful for:
  - Elaborating the details and variations of a use case
  - Communicating the requirements and expectations of a use case to the stakeholders and developers
  - Testing and verifying the functionality and quality of a use case
- An example of a use case diagram and a use case scenario for an online shopping system is shown below:

![Use case diagram for online shopping system](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-use-case-diagram/online-shopping-use-case-diagram.png)

Use case: Purchase items
Brief scenario: The customer browses the catalog, adds items to the shopping cart, enters the shipping and payment information, and confirms the order.
Casual scenario: The customer browses the catalog and selects some items. The system shows the details and price of each item. The customer adds the items to the shopping cart. The system updates the total amount of the cart. The customer proceeds to checkout. The system asks the customer to enter the shipping and payment information. The customer enters the information and confirms the order. The system validates the information and processes the payment. The system sends a confirmation email to the customer and updates the inventory.
Fully dressed scenario:
- Name: Purchase items
- Actor: Customer
- Preconditions: The customer has accessed the online shopping system and has a valid account.
- Postconditions: The customer has received a confirmation email and the order has been placed.
- Trigger: The customer clicks on the checkout button.
- Main success scenario:
  1. The system asks the customer to enter the shipping and payment information.
  2. The customer enters the information and confirms the order.
  3. The system validates the information and processes the payment.
  4. The system sends a confirmation email to the customer and updates the inventory.
  5. The use case ends successfully.
- Extensions:
  - 3a. The system detects an error in the information or the payment.
    - 3a1. The system displays an error message and asks the customer to correct the information or try another payment method.
    - 3a2. The customer corrects the information or tries another payment method.
    - 3a3. The use case resumes at step 3.
  - 3b. The system detects that some items are out of stock.
    - 3b1. The system displays a warning message and removes the out of stock items from the cart.
    - 3b2. The system recalculates the total amount of the cart.
    - 3b3. The use case resumes at step 2.