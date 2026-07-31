## Unit 2 - Creating Entity-Relationship Diagram using case tools

- An entity-relationship diagram (ERD) is a graphical representation of the data and relationships in a database system.
- A case tool is a software application that supports the development and maintenance of software systems, such as databases, by providing features such as modeling, design, code generation, testing, and documentation.
- Creating an ERD using a case tool involves the following steps:

  - Identify the entities and attributes in the database system. Entities are the objects or concepts that store data, such as customers, products, or orders. Attributes are the properties or characteristics of entities, such as name, price, or quantity.
  - Identify the relationships and cardinalities among the entities. Relationships are the associations or connections between entities, such as one-to-many, many-to-many, or one-to-one. Cardinalities are the number of occurrences of one entity that can be related to another entity, such as one, zero or more, or one or more.
  - Draw the ERD using the symbols and notation of the chosen case tool. Different case tools may use different symbols and notation to represent entities, attributes, relationships, and cardinalities. For example, some case tools use rectangles for entities, ovals for attributes, diamonds for relationships, and lines with crow's feet for cardinalities.
  - Validate and refine the ERD using the business rules and requirements of the database system. Business rules and requirements are the constraints and specifications that define the logic and functionality of the database system, such as uniqueness, integrity, security, and performance. The ERD should be checked for accuracy, completeness, consistency, and clarity, and modified if necessary.

- An example of an ERD created using a case tool is shown below:

```markdown
![ERD example](erd_example.png)

Figure 1: ERD example for a bookstore database system
```

- The ERD example shows the following entities, attributes, relationships, and cardinalities:

  - Book: an entity that stores data about the books sold by the bookstore. It has the following attributes: ISBN (primary key), title, author, publisher, price, and category. It has a one-to-many relationship with Order_Detail, meaning that one book can be ordered many times, but each order detail can only refer to one book.
  - Customer: an entity that stores data about the customers who buy books from the bookstore. It has the following attributes: customer_id (primary key), name, address, phone, and email. It has a one-to-many relationship with Order, meaning that one customer can place many orders, but each order can only belong to one customer.
  - Order: an entity that stores data about the orders placed by the customers. It has the following attributes: order_id (primary key), date, total, and status. It has a one-to-many relationship with Order_Detail, meaning that one order can have many order details, but each order detail can only belong to one order.
  - Order_Detail: an entity that stores data about the details of each order, such as the quantity and subtotal of each book ordered. It has the following attributes: order_id and ISBN (composite primary key), quantity, and subtotal. It has a many-to-many relationship with Book, meaning that many books can be ordered in many orders, and vice versa. It also has a many-to-one relationship with Order, meaning that many order details can belong to one order, but each order detail can only refer to one order.