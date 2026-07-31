# Time Diagram for the Notes of the Unit 2 - Basic Structural Modeling in the Subject of Object Oriented System Design

- Object oriented system design is a process of defining the architecture, modules, interfaces, and data for a system that uses objects and their relationships as the main components.
- Basic structural modeling is one of the aspects of object oriented system design that focuses on the static structure of the system, such as the classes, attributes, operations, and associations that exist among them.
- A time diagram, also known as a timing diagram, is a type of behavioral diagram that shows the changes in the state or condition of one or more lifelines over time.
- A lifeline is a representation of an individual participant in the interaction, such as an object, a class, an actor, or a component.
- A time diagram can be used to describe the behavior of both individual classifiers and interactions of classifiers, focusing on the time of occurrence of events that cause changes in the modeled conditions of the lifelines.
- A time diagram consists of the following elements:
  - A horizontal axis that represents the progression of time from left to right.
  - One or more vertical dashed lines that represent the lifelines involved in the interaction.
  - One or more state or condition boxes that show the state or condition of a lifeline at a given point in time.
  - One or more event occurrences that mark the points in time when a lifeline changes its state or condition.
  - One or more constraints that specify the temporal relationships or restrictions among the event occurrences.
  - One or more messages that represent the communication or interaction between the lifelines.
- A time diagram can be used for various purposes, such as:
  - To model the timing requirements and constraints of a system or a subsystem.
  - To verify the correctness and consistency of the behavior of a system or a subsystem.
  - To analyze the performance and scalability of a system or a subsystem.
  - To document the expected behavior of a system or a subsystem.
  - To communicate and collaborate with other stakeholders involved in the system development.
- An example of a time diagram for a simple online shopping system is shown below:

![Time diagram example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-timing-diagram/timing-diagram-example.png)

- The time diagram shows the interaction between the customer, the online store, and the bank over time.
- The customer lifeline has two state boxes: browsing and paying.
- The online store lifeline has three state boxes: idle, processing order, and confirming payment.
- The bank lifeline has two state boxes: idle and processing payment.
- The event occurrences are marked by small black dots on the lifelines.
- The messages are shown by horizontal arrows between the lifelines.
- The constraints are shown by brackets with labels on the horizontal axis.
- The time diagram illustrates the following scenario:
  - The customer browses the online store and selects some items to buy.
  - The customer initiates the payment process by sending a place order message to the online store.
  - The online store changes its state from idle to processing order and sends a request payment message to the bank.
  - The bank changes its state from idle to processing payment and verifies the customer's credit card information.
  - The bank sends a confirm payment message to the online store and changes its state back to idle.
  - The online store changes its state from processing order to confirming payment and sends a confirm order message to the customer.
  - The customer changes its state from browsing to paying and receives the confirmation of the order.
  - The online store changes its state back to idle and waits for the next order.