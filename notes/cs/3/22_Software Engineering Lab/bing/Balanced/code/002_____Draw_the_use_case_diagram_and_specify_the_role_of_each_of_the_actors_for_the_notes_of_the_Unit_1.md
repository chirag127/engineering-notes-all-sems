### Use Case Diagram and Actors in Software Engineering

A use case diagram is a graphical representation of the interactions between a system and its external entities, such as users, customers, or other systems. A use case diagram shows the functionality of a system from the perspective of the actors who use it. Actors are the roles that the external entities play in relation to the system. A use case diagram consists of the following elements:

- **Actors**: The external entities that interact with the system. They are represented by stick figures or icons with names.
- **Use cases**: The actions or services that the system provides to the actors. They are represented by ovals with names.
- **Associations**: The relationships between actors and use cases. They are represented by solid lines with optional multiplicity indicators.
- **System boundary**: The scope or boundary of the system under consideration. It is represented by a rectangle that encloses the use cases.
- **Relationships**: The dependencies or extensions between use cases. They are represented by dashed lines with keywords such as include, extend, or generalize.

An example of a use case diagram for an online shopping system is shown below:

![use case diagram example](https://miro.medium.com/max/1400/1*0r0Jx7y7f0yY6wW8cZs0jQ.png)

The actors in this diagram are:

- **Customer**: The person who browses, selects, and orders products from the online store.
- **Administrator**: The person who manages the inventory, prices, and orders of the online store.
- **Payment System**: The external system that processes the payment transactions for the online store.
- **Delivery System**: The external system that handles the delivery of the ordered products to the customer.

The use cases in this diagram are:

- **Browse Products**: The customer can view the available products and their details on the online store.
- **Select Products**: The customer can add or remove products from their shopping cart.
- **Order Products**: The customer can place an order for the products in their shopping cart and provide their delivery and payment information.
- **Confirm Order**: The system confirms the order and sends a confirmation email to the customer.
- **Manage Inventory**: The administrator can add, update, or delete products and their details on the online store.
- **Manage Prices**: The administrator can set or change the prices of the products on the online store.
- **Manage Orders**: The administrator can view, modify, or cancel the orders placed by the customers on the online store.
- **Process Payment**: The payment system validates and processes the payment transaction for the order.
- **Deliver Products**: The delivery system delivers the ordered products to the customer's address.

The associations in this diagram are:

- The customer is associated with the use cases Browse Products, Select Products, and Order Products, indicating that the customer can perform these actions on the system.
- The administrator is associated with the use cases Manage Inventory, Manage Prices, and Manage Orders, indicating that the administrator can perform these actions on the system.
- The payment system is associated with the use case Process Payment, indicating that the system interacts with the payment system to process the payment transaction.
- The delivery system is associated with the use case Deliver Products, indicating that the system interacts with the delivery system to deliver the products.

The relationships in this diagram are:

- The use case Order Products includes the use cases Confirm Order, Process Payment, and Deliver Products, indicating that these use cases are mandatory and essential parts of the ordering process.
- The use case Confirm Order extends the use case Print Slip, indicating that the system can optionally print a slip for the order as an additional feature.