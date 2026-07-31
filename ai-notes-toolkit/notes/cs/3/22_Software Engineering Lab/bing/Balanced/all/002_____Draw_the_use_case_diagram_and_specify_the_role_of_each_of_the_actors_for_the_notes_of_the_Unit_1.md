# Use Case Diagram and Actors in Software Engineering

A use case diagram is a graphical representation of the interactions between a system and its external entities, such as users, customers, or other systems. A use case diagram shows the functionality of a system from the perspective of the actors, who are the people or things that perform actions or have goals in the system. A use case diagram consists of the following elements:

- **Actors**: An actor is a role that a user or another system plays in relation to the system. An actor can be represented by a stick figure or a named rectangle. An actor can have a generalization relationship with another actor, which means that the child actor inherits the behavior and attributes of the parent actor. For example, a student actor can be a generalization of a person actor.
- **Use cases**: A use case is a description of a set of actions that the system performs to achieve a goal for an actor. A use case can be represented by an oval with a name inside. A use case can have an extension relationship with another use case, which means that the base use case can be extended by the additional behavior of the extension use case under certain conditions. For example, a login use case can be extended by a forgot password use case.
- **Associations**: An association is a line that connects an actor and a use case, indicating that the actor participates in the use case. An association can have a multiplicity, which specifies how many instances of an actor or a use case are involved in the interaction. For example, an association between a customer actor and a place order use case can have a multiplicity of 1..* on the customer side, meaning that one or more customers can place an order.
- **System boundary**: A system boundary is a rectangle that encloses the use cases that are in the scope of the system. The system boundary can have a name that identifies the system. The system boundary helps to distinguish the use cases that are part of the system from the ones that are outside the system. For example, a system boundary can separate the use cases of an online shopping system from the use cases of a payment system.

## Example of a Use Case Diagram

The following diagram shows a use case diagram for an online shopping system. The actors are customer, seller, and payment system. The use cases are browse products, search products, view product details, add product to cart, remove product from cart, place order, confirm order, cancel order, and make payment. The system boundary is online shopping system.

![Use case diagram for online shopping system](https://miro.medium.com/max/1400/1*8aT0YmZwQwL0w0y0c8yO1g.png)

## Role of Each Actor

- **Customer**: A customer is a person who visits the online shopping system to buy products. A customer can browse products, search products, view product details, add product to cart, remove product from cart, place order, confirm order, cancel order, and make payment. A customer is the primary actor for most of the use cases, as they initiate the interactions with the system.
- **Seller**: A seller is a person who sells products on the online shopping system. A seller can view the orders placed by the customers and confirm or cancel them. A seller is a secondary actor for some of the use cases, as they respond to the requests from the system or the customers.
- **Payment system**: A payment system is an external system that processes the payments made by the customers. A payment system can make payment or decline payment. A payment system is a secondary actor for the make payment use case, as it provides a service to the system.