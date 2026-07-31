### Interaction Diagram for the Notes of Unit 2 - Basic Structural Modeling in the Subject of Object Oriented System Design

In Object Oriented System Design, interaction diagrams are used to represent the interactions between objects in a system. The most commonly used interaction diagrams are Sequence Diagrams and Communication Diagrams. In this section, we will focus on Sequence Diagrams.

#### Sequence Diagram

A Sequence Diagram is an interaction diagram that shows the interactions between objects in a system in a time-ordered sequence. It is used to show the flow of messages between objects and the order in which they occur.

##### Notation

- Objects are represented as rectangles with the name of the object above the rectangle.
- Lifelines are represented as vertical lines that extend from the object rectangle downwards.
- Messages are represented as arrows between the lifelines.
- Activation bars are represented as horizontal lines on a lifeline that show the duration of a message.

##### Elements

- Object: Represents an instance of a class.
- Lifeline: Represents the lifespan of an object.
- Message: Represents a communication between objects.
- Activation: Represents the duration of a message.

##### Steps to Create a Sequence Diagram

1. Identify the objects involved in the interaction.
2. Determine the order in which the messages are sent.
3. Create the lifelines for each object.
4. Draw the messages between the lifelines.
5. Add activation bars to show the duration of each message.

##### Example

```
Title: Order Processing Sequence Diagram

Customer->Order: Places Order
Order->Payment: Request Payment
Payment->Bank: Process Payment
Bank-->Payment: Payment Approved
Payment-->Order: Payment Confirmed
Order->Shipping: Ship Order
Shipping-->Order: Order Shipped
```

In the above example, the customer places an order which triggers the order to request payment from the payment object. The payment object then processes the payment with the bank object. Once the payment is approved, the payment object confirms the payment with the order object. The order object then sends a message to the shipping object to ship the order. Once the order is shipped, the shipping object sends a message to the order object to confirm that the order has been shipped.

In conclusion, Sequence Diagrams are an important tool in Object Oriented System Design to represent the interactions between objects in a system. By following the steps outlined above, you can create a Sequence Diagram that accurately represents the interactions between objects in your system.