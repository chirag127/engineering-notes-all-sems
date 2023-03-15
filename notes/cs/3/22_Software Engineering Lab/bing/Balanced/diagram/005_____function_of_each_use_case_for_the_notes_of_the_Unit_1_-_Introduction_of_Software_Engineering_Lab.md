A use case diagram is a graphical representation of the interactions between a system and its external actors. It shows the functionality of a system from the user's perspective and the relationships among different use cases. A use case diagram is one of the artifacts of the Unified Modeling Language (UML) and is used for software engineering analysis and design.

A use case diagram consists of the following elements:

- **Actors**: An actor is a person, organization, or external system that interacts with the system. Actors are represented by stick figures or icons with names.
- **Use cases**: A use case is a specific goal or task that an actor wants to achieve by using the system. Use cases are represented by ovals with names.
- **System boundary**: A system boundary is a rectangle that encloses the use cases and represents the scope of the system. The system boundary is optional and can be omitted if the diagram is simple or clear enough.
- **Relationships**: Relationships are lines that connect actors and use cases and show how they interact. There are different types of relationships, such as:

  - **Association**: An association is a solid line that indicates that an actor can initiate or participate in a use case. An association can have an optional multiplicity that shows how many instances of an actor or a use case are involved in the interaction.
  - **Include**: An include is a dashed line with an open arrowhead that indicates that a use case is a mandatory part of another use case. The included use case is executed every time the base use case is executed.
  - **Extend**: An extend is a dashed line with an open arrowhead that indicates that a use case is an optional or conditional part of another use case. The extended use case is executed only if a certain condition is met in the base use case.
  - **Generalization**: A generalization is a solid line with a closed arrowhead that indicates that a use case or an actor inherits the features of another use case or actor. The generalization relationship is used to show commonality or specialization among use cases or actors.

Here is an example of a use case diagram for an online shopping system:

![use case diagram example](https://blog.devgenius.io/content/images/2020/12/use-case-diagram.png)

The use case diagram shows the following use cases and actors:

- **Customer**: A customer is an actor that can browse products, add products to cart, view cart, check out, and make payment.
- **Admin**: An admin is an actor that can manage products, view orders, and generate reports.
- **Online Shopping System**: The online shopping system is the system boundary that contains the use cases of the system.
- **Browse Products**: Browse products is a use case that allows a customer to search and view products by category, name, or price.
- **Add Product to Cart**: Add product to cart is a use case that allows a customer to select a product and add it to the shopping cart.
- **View Cart**: View cart is a use case that allows a customer to see the products and the total amount in the shopping cart.
- **Check Out**: Check out is a use case that allows a customer to confirm the order and proceed to payment. It includes the use cases of calculate price with tax and make payment.
- **Calculate Price with Tax**: Calculate price with tax is a use case that calculates the final price of the order with the applicable tax rate.
- **Make Payment**: Make payment is a use case that allows a customer to choose a payment method and enter the payment details.
- **Manage Products**: Manage products is a use case that allows an admin to add, edit, or delete products in the system.
- **View Orders**: View orders is a use case that allows an admin to see the orders placed by the customers and their status.
- **Generate Reports**: Generate reports is a use case that allows an admin to create and download reports on sales, inventory, or customers.

The use case diagram also shows the following relationships:

- **Association**: The customer and the admin are associated with the use cases they can initiate or participate in.
- **Include**: The check out use case includes the calculate price with tax and make payment use cases, which means they are mandatory parts of the check out process.
- **Extend**: The make payment use case extends the check out use case, which means it is an optional or conditional part of the check out process. The extension point is labeled as "payment required", which indicates the condition for the extension.
- **Generalization**: The customer and the admin are generalizations of the actor, which means they inherit the features