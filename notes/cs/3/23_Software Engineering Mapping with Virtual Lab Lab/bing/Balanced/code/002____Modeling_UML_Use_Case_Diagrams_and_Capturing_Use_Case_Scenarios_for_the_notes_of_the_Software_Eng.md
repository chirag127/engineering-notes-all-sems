## Modeling UML Use Case Diagrams and Capturing Use Case Scenarios

- UML stands for Unified Modeling Language, which is a standard way of visualizing and documenting the design of a software system.
- Use case diagrams are one of the types of UML diagrams that show the behavior and functionality of a system from the perspective of the users (or actors).
- Use case diagrams consist of the following elements:
  - Actors: represent the roles or entities that interact with the system, such as users, customers, or other systems. Actors are depicted as stick figures or icons.
  - Use cases: represent the goals or tasks that the actors want to achieve by using the system, such as logging in, placing an order, or generating a report. Use cases are depicted as ovals with names inside.
  - System boundary: represents the scope or boundary of the system under consideration, such as a software application, a website, or a subsystem. System boundary is depicted as a rectangle that encloses the use cases.
  - Associations: represent the relationships or interactions between the actors and the use cases, such as who initiates, participates, or benefits from a use case. Associations are depicted as solid lines connecting the actors and the use cases.
  - Generalizations: represent the inheritance or specialization relationships between actors or use cases, such as when a subclass inherits the attributes and behaviors of a superclass. Generalizations are depicted as dashed lines with a hollow triangle at the end pointing to the superclass.
  - Include: represent the common or shared parts of two or more use cases, such as when a use case always invokes another use case as part of its normal flow. Include is depicted as a dashed line with an open arrowhead at the end pointing to the included use case and labeled with <<include>>.
  - Extend: represent the optional or conditional parts of a use case, such as when a use case may invoke another use case depending on some condition or exception. Extend is depicted as a dashed line with an open arrowhead at the end pointing to the extending use case and labeled with <<extend>>.

- An example of a use case diagram for an online shopping system is shown below:

![Use case diagram example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-use-case-diagram/use-case-diagram-example.png)

- Use case scenarios are the textual descriptions of the steps and interactions that occur during the execution of a use case, such as the main flow, alternative flows, and exception flows.
- Use case scenarios can be written in various formats, such as tabular, outline, or narrative, depending on the level of detail and complexity required.
- Use case scenarios can be used to:
  - Elaborate and clarify the requirements of a system
  - Communicate and validate the requirements with the stakeholders
  - Test and verify the functionality and quality of a system
  - Generate and document the test cases and test scripts for a system

- An example of a use case scenario for the "Place an order" use case in the online shopping system is shown below in a tabular format:

| Use Case Name | Place an order |
| --- | --- |
| Actor | Customer |
| Precondition | Customer is logged in and has items in the shopping cart |
| Postcondition | Customer has placed an order and received a confirmation |
| Main Flow | 1. Customer clicks on the "Checkout" button <br> 2. System displays the order summary and the payment options <br> 3. Customer selects a payment option and enters the payment details <br> 4. System validates the payment details and processes the payment <br> 5. System generates an order number and sends a confirmation email to the customer <br> 6. Customer receives the confirmation email and the order number |
| Alternative Flow | 3a. Customer cancels the order <br> 3a1. System returns to the shopping cart page <br> 4a. System detects an error in the payment details or the payment processing <br> 4a1. System displays an error message and asks the customer to retry or cancel the order |
| Exception Flow | 5a. System fails to generate an order number or send a confirmation email <br> 5a1. System displays an error message and asks the customer to contact the customer service |