### Function of each use case for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab

- A use case is a description of how a user interacts with a system to achieve a goal.
- A use case diagram is a graphical representation of the use cases and the actors involved in a system.
- A use case diagram shows the relationships between the use cases and the actors, as well as the boundaries of the system.
- A use case diagram can help to:
  - Specify the context of a system
  - Capture the requirements of a system
  - Validate a system's architecture
  - Drive implementation and generate test cases
  - Communicate with stakeholders and users
- A use case diagram consists of the following elements:
  - Actors: The external entities that interact with the system, such as users, roles, or other systems. They are represented by stick figures or icons.
  - Use cases: The functionalities or services that the system provides to the actors, such as login, search, or checkout. They are represented by ovals with names inside.
  - System boundary: The scope or boundary of the system under consideration, such as a website, an app, or a module. It is represented by a rectangle that encloses the use cases.
  - Associations: The connections or interactions between the actors and the use cases, such as request, response, or notification. They are represented by solid lines with optional arrows to indicate the direction of communication.
  - Include relationships: The dependencies or subfunctions that a use case requires from another use case, such as authentication, validation, or calculation. They are represented by dashed arrows with the label <<include>> from the base use case to the included use case.
  - Extend relationships: The optional or alternative scenarios that a use case can extend from another use case, such as error handling, exception, or variation. They are represented by dashed arrows with the label <<extend>> from the extended use case to the base use case.
  - Generalization relationships: The inheritance or specialization of actors or use cases, such as user and admin, or search and advanced search. They are represented by solid lines with empty triangles pointing to the parent actor or use case.

- An example of a use case diagram for an online shopping system is shown below:

![Use case diagram for online shopping system](https://miro.medium.com/max/1400/1*7xZy0f3fZw1w0k0dZ0a4Zw.png)

- The use case diagram shows the following actors and use cases:
  - Customer: The user who can browse products, add products to cart, checkout, and make payment.
  - Admin: The user who can manage products, orders, and customers.
  - System: The external system that can process payment and confirm order.
  - Browse products: The use case that allows the customer to view the available products by category, name, or price.
  - Add product to cart: The use case that allows the customer to select a product and add it to the shopping cart.
  - Checkout: The use case that allows the customer to review the cart, enter shipping and billing information, and place the order.
  - Make payment: The use case that allows the customer to pay for the order using a credit card or other methods.
  - Process payment: The use case that allows the system to verify the payment and deduct the amount from the customer's account.
  - Confirm order: The use case that allows the system to send a confirmation email to the customer and update the order status.
  - Manage products: The use case that allows the admin to add, edit, or delete products.
  - Manage orders: The use case that allows the admin to view, update, or cancel orders.
  - Manage customers: The use case that allows the admin to view, edit, or delete customer profiles.
- The use case diagram also shows the following relationships:
  - The customer is associated with browse products, add product to cart, checkout, and make payment.